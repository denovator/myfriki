# -*- coding: utf-8 -*-
class Config(object):
    SECRET_KEY = "asdfjlsadjflkjlwkqjerljlasdjfl"
    debug = False


class Production(Config):
    debug = True
    CSRF_ENABLED = False
    ADMIN = "seunghojung0114@gmail.com"
    SQLALCHEMY_DATABASE_URI = "mysql+gaerdbms:///flaskr?instance=mochafac:flaskr-instance"
    migration_directory = "migrations"
