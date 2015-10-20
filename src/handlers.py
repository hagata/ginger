# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
import webapp2

import json
import logging
import os
import jinja2

from google.appengine.api import memcache  # For XsrfHandler.  Remove if unused.
from google.appengine.api import users

from base import constants
# from base import handlers

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class RootHandler(webapp2.RequestHandler):
  def get(self):
    template_values = {}
    template = JINJA_ENVIRONMENT.get_template('index.html')
    self.response.write(template.render(template_values))

class StaticHandler(webapp2.RequestHandler):
  def get(self):
    self.redirect('/static/index.html')

# class StaticHandler(handlers.BaseHandler):

#   def get(self):
#     self.redirect('/static/index.html')

# class CspHandler(handlers.BaseAjaxHandler):

#   def post(self):
#     try:
#       report = json.loads(self.request.body)
#       logging.warn('CSP Violation: %s' % (json.dumps(report['csp-report'])))
#       self.render_json({})
#     except:
#       self.render_json({'error': 'invalid CSP report'})

# class XssHandler(handlers.BaseHandler):

#   def get(self):
#     if not constants.IS_DEV_APPSERVER:
#       self.render('debug_only.tpl')
#       return
#     autoescape = self.request.get('autoescape') != 'off'
#     string = self.request.get('string', '')
#     template = {'string': string,
#                 'autoescape': autoescape,
#                 'show_autoescape': bool(string)}
#     # DANGER: Disable CSP and the built-in XSS blocker in modern browsers for
#     # demonstration purposes.  DO NOT DUPLICATE THIS IN PRODUCTION CODE.
#     self.response.headers['X-XSS-Protection'] = '0'
#     self.response.headers['content-security-policy'] = ''
#     self.render('xss.tpl', template)

#   def post(self):
#     self.get()

# class XsrfHandler(handlers.AuthenticatedHandler):

#   def _GetCounter(self):
#     counter = memcache.get('counter')
#     if not counter:
#       counter = 0
#       memcache.set('counter', counter)
#     return counter

#   def get(self):
#     if not constants.IS_DEV_APPSERVER:
#       self.render('debug_only.tpl')
#       return
#     counter = self._GetCounter()
#     self.render('xsrf.tpl', {'email': self.current_user.email(),
#                              'counter': counter})

#   def post(self):
#     if not constants.IS_DEV_APPSERVER:
#       self.render('debug_only.tpl')
#       return
#     counter = self._GetCounter() + 1
#     memcache.set('counter', counter)
#     self.render('xsrf.tpl', {'email': self.current_user.email(),
#                              'counter': counter})

#   def DenyAccess(self):
#     self.redirect(users.create_login_url(self.request.path))

#   def XsrfFail(self):
#     counter = self._GetCounter()
#     self.render('xsrf.tpl', {'email': self.current_user.email(),
#                              'counter': counter,
#                              'xsrf_fail': True})


# class XssiHandler(handlers.BaseHandler):

#   def get(self):
#     if not constants.IS_DEV_APPSERVER:
#       self.render('debug_only.tpl')
#       return
#     self.render('xssi.tpl')

#   def post(self):
#     self.get()
