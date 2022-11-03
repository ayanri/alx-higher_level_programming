#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        a = fct(*args)
        return a
    except Exception as exception:
        import sys
        print("Exception: {}".format(exception), file=sys.stderr)
        return None
