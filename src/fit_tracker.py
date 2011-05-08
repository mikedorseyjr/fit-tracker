import os


from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from src.models import fit_base
from src import rest

class MainPage(webapp.RequestHandler):
    def get(self):
        exercises_query = fit_base.Exercise.all().order('-name')
        exercises = exercises_query.fetch(10)

        template_values = {
            'exercises': exercises,
            }

        path = os.path.join(os.path.dirname(__file__), 'html/index.html')
        self.response.out.write(template.render(path, template_values))
        
application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/rest/.*', rest.Dispatcher)],
                                     debug=True)
# configure the rest dispatcher to know what prefix to expect on request urls
rest.Dispatcher.base_url = "/rest"

# add all models from the current module, and/or...
rest.Dispatcher.add_models_from_module(fit_base)
def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()