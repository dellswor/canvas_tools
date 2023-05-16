# canvas_cache.py
#
# The Canvas datamodel, as exposed by the API, combine with API latencies makes
# direct use of the API painful for many questions. The caching layer exists
# to make a local copy of Canvas data for much faster access.
# 

import psycopg

from core import get_canvas_connection

if __name__=="__main__":
    print("The canvas_cache should not be run directly!",file=sys.stderr)
    exit(1)

_DATABASE_NAME = 'canvastools'
# By default, access to the cache uses the running user's name
_DATABASE_USER = os.getLogin()

def _initialize():
    global _cache_age

_initialize()
