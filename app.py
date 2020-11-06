from chalice import Chalice, CustomAuthorizer

from chalicelib.config.constants import SERVICE_NAME, AUTHORIZER_NAME, AUTHORIZER_HEADER
from chalicelib.config.settings import dne_api_key_authorizer_url

app = Chalice(app_name=SERVICE_NAME)

authorizer = CustomAuthorizer(
    name=AUTHORIZER_NAME,
    header=AUTHORIZER_HEADER,
    authorizer_uri=dne_api_key_authorizer_url,
    ttl_seconds=175
)


@app.route('/')
def index():
    return {'hello': 'world'}
