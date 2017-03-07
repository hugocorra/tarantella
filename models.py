# -*- coding: utf-8 -*-
from google.appengine.ext import ndb
from google.appengine.api import users

#from utils import DictWithURL


class Settings(ndb.Model):
    user = ndb.UserProperty()
    tarantella = ndb.IntegerProperty(default=25)
    short_break = ndb.IntegerProperty(default=5)
    long_break = ndb.IntegerProperty(default=30)

    # @classmethod
    # def ancestor(cls):
    #     return ndb.Key(Settings, users.get_current_user().user_id())

