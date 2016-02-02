from twill.parse import execute_string
from twill.errors import TwillAssertionError

def twill_test(func):
    def run_test(*args):
        try:
            execute_string(func.__doc__, no_reset = False)
        except TwillAssertionError, err:
            if args and hasattr(args[0], 'fail'):
                args[0].fail(str(err))
            else:
                raise
    return run_test
