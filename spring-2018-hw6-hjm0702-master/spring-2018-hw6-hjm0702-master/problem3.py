from collections import namedtuple
from collections import OrderedDict
from functools import wraps
import urllib.request
import urllib.error

def lru_cache(maxsize = 128):
    _Cacheinfo = namedtuple('CacheInfo', 'hits, misses, maxsize, currsize')

    def real_decorator(func):
        cache = OrderedDict()
        hits = 0
        misses = 0
        kwargs_mark = object()

        @wraps(func)
        def inner(*args, **kwargs):
            nonlocal hits, misses
            key = args
            if kwargs:
                key += (kwargs_mark,) + tuple(sorted(kwargs.items()))

            if key in cache.keys():
                hits = hits +1
                result = cache[key]
            else:
                result = func(*args, **kwargs)
                if len(cache) < maxsize :
                    cache[key] = result
                    misses = misses +1
                else:
                    cache.popitem(last = False)
                    cache[key]=result
                    misses = misses +1
            return result

        def cache_info():
            return _Cacheinfo(hits, misses, maxsize, min(misses,maxsize))

        inner.cache_info = cache_info
        return inner
    return real_decorator

if __name__ == "__main__":
    @lru_cache(maxsize = 32)
    def get_pep(num):
        'Retrieve text of a Python Enhancement Proposal'
        resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
        try:
            with urllib.request.urlopen(resource) as s:
                return s.read()
        except urllib.error.HTTPError:
            return 'Not Found'

    for n in 8, 8, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
        pep = get_pep(n)
        print(n, len(pep))

    print(get_pep.cache_info())
