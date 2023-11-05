import pigeon.middleware.conversion.mime.parsers
import pigeon.middleware.conversion.mime.generators
import pigeon.default.errors

# VERBOSITY
VERBOSITY = 2

# ADDRESS
ADDRESS = ''
PORT = 8080

# ALLOWED HOSTS
ALLOWED_HOSTS = [None]
# ALLOWED METHODS
ALLOWED_METHODS = ['POST', 'GET', 'HEAD', 'POST', 'PUT', 'OPTIONS']

# VIEWS
VIEWS = {}
# TYPED VIEWS (INCLUDE CONTENT TYPE)
TYPED_VIEWS = {}
# ERRORS (VIEWS BUT FOR ERRORS)
ERRORS = {
    000: pigeon.default.errors.fallback,
}

# ACCESS-CONTROL
CORS_ALLOWED_ORIGINS = []
CORS_ALLOW_CRED = False
CORS_ALLOWED_HEADERS = ['Content-Type']
CORS_ALLOWED_METHODS = ['POST', 'GET', 'HEAD', 'POST', 'PUT', 'OPTIONS']
CORS_MAX_AGE = 1200

# STATICFILES
STATIC_URL_BASE = None
STATIC_FILES_DIR = None

# MEDIAFILES
MEDIA_URL_BASE = None
MEDIA_FILES_DIR = None

# TEMPLATING
TEMPLATES_DIR = None

# HTTPS
USE_HTTPS = False
CERTIFICATE_PATH = None
PRIVATE_KEY_PATH = None
PRIVATE_KEY_PASSWD = None

# MIME
MIME_PARSERS = {
    'application/json': pigeon.middleware.conversion.mime.parsers.JSONParser,
    'application/x-www-form-urlencoded': pigeon.middleware.conversion.mime.parsers.UrlencodedFormParser,
    'multipart/form-data': pigeon.middleware.conversion.mime.parsers.MultiPartFormParser,
}

# GENERATORS
MIME_GENERATORS = {
    'application/json': pigeon.middleware.conversion.mime.generators.JSONGenerator,
}

# REQUEST PREPROCESSOR
#MIDDLEWARE_PROCESSORS = {
#    '1.1': pigeon.middleware.processing.Owl,
#}
