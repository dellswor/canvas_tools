# core.py
#
# This is the core library for canvas_tools and contains functions that will be
# used across several scripts.
#

from canvasapi import Canvas
import sys,os

if __name__=="__main__":
    print("The core should never be run directly! Please see the README.txt for information on how to use canvas_tools.",file=sys.stderr)
    #exit(1)

class MisconfigurationException(Exception):
    '''Exception to be thrown if some configuration thing is missing.'''
    pass

def _initialize():
    global _CONN
    global _API_KEY
    global _API_URL
    # bail out if this has already been initialized... defined as having the
    # _API_KEY set.
    try:
        # The API_KEY is set... we're done here.
        t = _API_KEY
        return
    except NameError as e:
        pass
    except Exception as e:
        print("Critical error initializing the core!",file=sys.stderr)
        raise e
    # If we get here, we're ready to init
    _API_KEY = os.getenv("CANVAS_KEY")
    _API_URL = os.getenv("CANVAS_URL")
    if _API_KEY is None or _API_URL is None:
        print("Environment is incorrectly configured!",file=sys.stderr)
        raise MisconfigurationException()
    # Credentials loaded from the env... clear them incase something untrusted
    # runs later in this environment...
    os.unsetenv("CANVAS_KEY")
    os.unsetenv("CANVAS_URL")
    # "init" the _CONN
    _CONN = None
    
def get_canvas_connection():
    global _CONN
    global _API_KEY
    global _API_URL

    if _CONN is None:
        _CONN = Canvas(_API_URL, _API_KEY)
    return _CONN

# Initialize the core for use
_initialize()
