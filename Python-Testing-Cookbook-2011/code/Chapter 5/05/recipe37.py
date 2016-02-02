from pyccuracy.actions import ActionBase
from pyccuracy.errors import *

class LoggedInAction(ActionBase):
    regex = r'(And )?I am logged in with username [\"](?P<username>.+)[\"] and password [\"](?P<password>.+)[\"]$'

    def execute(self, context, username, password):
        self.execute_action(u'I go to "http://localhost:8000/admin"', context)

        logged_in = False
        try:
            self.execute_action(\
              u'And I see that current page contains "id_username"', context)
        except ActionFailedError:
            logged_in = True

        if not logged_in:
            self.execute_action(u'And I fill "username" textbox with "%s"' % username, context)
            self.execute_action(u'And I fill "password" textbox with "%s"' % password, context)
            self.execute_action(u'And I click "login" button', context)

