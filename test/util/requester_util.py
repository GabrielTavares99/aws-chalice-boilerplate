import json

from chalice.config import Config
from chalice.local import LocalGateway

from app import app


class ResquesterUtil:

    @staticmethod
    def do_request(method, path, body, headers):
        lg = LocalGateway(app, Config(chalice_stage='homolog'))
        return lg.handle_request(method=method,
                                 path=path,
                                 headers=headers,
                                 body=json.dumps(body))
