
from cofig import DevelopmentConfig
from server import create_app


app = create_app(DevelopmentConfig)
