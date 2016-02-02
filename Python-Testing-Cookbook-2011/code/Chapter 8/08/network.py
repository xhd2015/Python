from springpython.database.core import *

class Event(object):
    def __init__(self, hostname, condition, severity):
        self.hostname = hostname
        self.condition = condition
        self.severity = severity
        self.id = -1

    def __str__(self):
        return "(ID:%s) %s:%s - %s" % (self.id, self.hostname, self.condition, self.severity)

class EventCorrelator(object):
    def __init__(self, factory):
        self.dt = DatabaseTemplate(factory)

    def __del__(self):
        del(self.dt)

    def process(self, event):
        stored_event, is_active = self.store_event(event)

        affected_services, affected_equip = self.impact(event)

        updated_services = [
            self.update_service(service, event) 
            for service in affected_services]
        updated_equipment = [
            self.update_equipment(equip, event) 
            for equip in affected_equip]

        return (stored_event, is_active, updated_services, updated_equipment)
        
    def store_event(self, event):
        try:
            max_id = self.dt.query_for_int("""select max(ID) 
                                              from EVENTS""")
        except DataAccessException, e:
            max_id = 0

        event.id = max_id+1

        self.dt.update("""insert into EVENTS 
                          (ID, HOST_NAME, SEVERITY, EVENT_CONDITION)
                          values 
                          (?,?,?,?)""",
                       (event.id, event.hostname, 
                        event.severity, event.condition))

        is_active = \
                 self.add_or_remove_from_active_events(event)

        return (event, is_active)

    def add_or_remove_from_active_events(self, event):
        """Active events are current ones that cause equipment 
           and/or services to be down."""

        if event.severity == 1:
            self.dt.update("""delete from ACTIVE_EVENTS
                              where EVENT_FK in (
                                  select ID 
                                  from   EVENTS 
                                  where  HOST_NAME = ? 
                                  and    EVENT_CONDITION = ?)""", 
                           (event.hostname,event.condition))
            return False
        else:
            self.dt.execute("""insert into ACTIVE_EVENTS
                               (EVENT_FK) values (?)""", 
                            (event.id,))
            return True

    def impact(self, event):
        """Look up this event has impact on either equipment 
           or services."""

        affected_equipment = self.dt.query(\
                       """select * from EQUIPMENT 
                          where HOST_NAME = ?""",
                       (event.hostname,),
                       rowhandler=DictionaryRowMapper())

        affected_services = self.dt.query(\
                       """select SERVICE.*
                          from   SERVICE
                          join   SERVICE_MAPPING SM
                          on (SERVICE.ID = SM.SERVICE_FK)
                          join   EQUIPMENT
                          on (SM.EQUIPMENT_FK = EQUIPMENT.ID)
                          where  EQUIPMENT.HOST_NAME = ?""",
                          (event.hostname,),
                          rowhandler=DictionaryRowMapper())

        return (affected_services, affected_equipment)

    def update_service(self, service, event):
        if event.severity == 1:
            self.dt.update("""delete from SERVICE_EVENTS
                              where EVENT_FK in (
                                  select ID 
                                  from EVENTS 
                                  where HOST_NAME = ? 
                                  and EVENT_CONDITION = ?)""", 
                           (event.hostname,event.condition))
        else:
            self.dt.execute("""insert into SERVICE_EVENTS
                               (EVENT_FK, SERVICE_FK) 
                               values (?,?)""", 
                            (event.id,service["ID"]))

        try:
            max = self.dt.query_for_int(\
                            """select max(EVENTS.SEVERITY) 
                               from SERVICE_EVENTS SE
                               join EVENTS
                               on (EVENTS.ID = SE.EVENT_FK)
                               join SERVICE
                               on (SERVICE.ID = SE.SERVICE_FK)
                               where SERVICE.NAME = ?""", 
                           (service["NAME"],))
        except DataAccessException, e:
            max = 1

        if max > 1 and service["STATUS"] == "Operational":
            service["STATUS"] = "Outage"
            self.dt.update("""update SERVICE 
                              set STATUS = ? 
                              where ID = ?""", 
                           (service["STATUS"], service["ID"]))

        if max == 1 and service["STATUS"] == "Outage":
            service["STATUS"] = "Operational"
            self.dt.update("""update SERVICE 
                              set STATUS = ? 
                              where ID = ?""", 
                           (service["STATUS"], service["ID"]))

        if event.severity == 1:
            return {"service":service, "is_active":False}
        else:
            return {"service":service, "is_active":True}

    def update_equipment(self, equip, event):
        try:
            max = self.dt.query_for_int(\
                       """select max(EVENTS.SEVERITY) 
                          from ACTIVE_EVENTS AE
                          join EVENTS
                          on (EVENTS.ID = AE.EVENT_FK)
                          where EVENTS.HOST_NAME = ?""", 
                       (event.hostname,))
        except DataAccessException:
            max = 1

        if max != equip["STATUS"]:
            equip["STATUS"] = max
            self.dt.update("""update EQUIPMENT 
                              set STATUS = ?""", 
                           (equip["STATUS"],))

        return equip
