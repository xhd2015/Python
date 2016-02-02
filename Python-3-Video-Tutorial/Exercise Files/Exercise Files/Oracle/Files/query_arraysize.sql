set echo on

drop table bigtab;
create table bigtab (mycol varchar2(20));
begin
  for i in 1..20000
  loop
   insert into bigtab (mycol) values (dbms_random.string('A',20));
  end loop;
end;
/

show errors

commit;

exit
