#!/usr/bin/python
# -*- coding: utf-8 -*-
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

import pathfix # pyflakes:ignore

from pytz import common_timezones_set        

class MainPage(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Pytz is loaded..... proof:')
        self.response.out.write('Pytz common timezones: %s' % common_timezones_set)

application = webapp.WSGIApplication(
                                     [('/', MainPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
