class Config(object):
    SECRET_KEY = 'code4awesome'


class ProdConfig(Config):
    DEBUG = True
    DATABASE = 'mysql://root:Lcqtdwj19891204@localhost:3306/favorites'



class DevConfig(Config):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    DATABASE = 'mysql://root:root@localhost:3306/favorites'


