import os

from chalice import CORSConfig

ENV = os.environ.get('ENV', 'dev')
PROD = 'prod'

DEFAULT_RESPONSE_HEADERS = {
    'Content-Type': 'application/json'
}
DEFAULT_HEADER = {
    'Content-Type': 'application/json'
}
# DATABASE
DATABASE = {
    'host': os.environ.get('DB_HOST', 'localhost'),
    'user': os.environ.get('DB_USER', 'root'),
    'password': os.environ.get('DB_PASSWORD', ''),
    'db': os.environ.get('DB_NAME', ''),
    'port': os.environ.get('DB_PORT', 3306),
    'charset': 'utf8mb4',
    'cursorclass': None
}

CORS_ALLOWED_ORIGIN = '*'
CORS_CONFIG = CORSConfig(
    allow_origin=CORS_ALLOWED_ORIGIN,
    allow_headers=[
        'Accept',
        'Accept-Language',
        'Access-Control-Allow-Credentials',
        'Access-Control-Allow-Headers',
        'Access-Control-Allow-Origin',
        'Access-Control-Allow-Methods',
        'Access-Control-Request-Headers',
        'Authorization',
        'Cache-Control',
        'Credentials',
        'crossDomain',
        'Content-Language',
        'Content-Length',
        'Content-Type',
        'Host'
        'Origin',
        'User-Agent',
        'X-Auth-Token',
        'X-Amz-Date',
        'X-Api-Key',
        'X-Amz-Security-Token',
        'X-Requested-With'
    ],
    max_age=600,
    expose_headers=[
        'Access-Control-Allow-Origin',
        'Set-Cookie'
    ],
    allow_credentials=False
)

dne_api_key_authorizer_url = os.environ.get('AUTHORIZER_URL')
