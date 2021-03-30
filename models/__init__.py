#!/usr/bin/python3
"""This module initialize the models package"""
from os import getenv


# getenv: returns the value of the environment variable key if it exists
# otherwise returns the default value
storage_type = getenv("HBNB_TYPE_STORAGE")

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
