from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
import urllib3

if urllib3.__version__ < '2':
    from urllib3.util.ssl_ import create_urllib3_context
else:
    from urllib3.util import create_urllib3_context


class SslContextAdapter(HTTPAdapter):
    def __init__(self, **kwargs):
        ctx = create_urllib3_context()
        ctx.load_default_certs()
        ciphers = ctx.get_ciphers()
        ciphers += 'HIGH:!DH:!aNULL'
        ctx.set_ciphers(ciphers)
        self.context = ctx
        super().__init__(**kwargs)

    def init_poolmanager(self, connections, maxsize, **kwargs):
        self.poolmanager = PoolManager(
            num_pools=connections,
            maxsize=maxsize,
            ssl_context=self.context,
            **kwargs)