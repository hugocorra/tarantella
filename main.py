#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import jinja2
import webapp2
import logging

from google.appengine.api import users
from google.appengine.ext import ndb

from models import Settings


JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def render_to_response(request_handler, template, dictionary):
    dictionary['users'] = users
    template = JINJA_ENVIRONMENT.get_template(template)
    request_handler.response.write(template.render(dictionary))


class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        render_to_response(self, 'templates/index.html', template_values)


class SettingsHandler(webapp2.RequestHandler):
    def get(self):
        key = ndb.Key(Settings, users.get_current_user().user_id())
        settings = key.get()

        

        if settings is None:
            logging.info('uhsaudhsauhduashduashduahu {}'.format(settings))
            settings = Settings()
            settings.put()

        template_values = {'settings': settings}
        render_to_response(self, 'templates/settings.html', template_values)

    def post(self):
        key = ndb.Key(Settings, users.get_current_user().user_id())
        settings = key.get()

        logging.info('settings {}'.format(settings))
        settings.tarantella = int(self.request.get('tarantella'))
        settings.short_break = int(self.request.get('short_break'))
        settings.long_break = int(self.request.get('long_break'))
        Settings().put()

        self.redirect('/settings')


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/settings', SettingsHandler)
], debug=True)
