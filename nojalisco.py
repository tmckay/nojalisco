import os
from datetime import date
from random import randint
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

#LOCATIONS = ['Taqueria Jalisco', 'CJ\'s Eatery', 'Rice \'n Spice', 'Barracuda Taqueria', 'Local 360', 'The Lucky Diner', 'Boat Street Cafe', 'The 5 Point Cafe', 'Buckley\'s in Belltown', 'Sushi Wave', 'Sushi Mori', 'Belltown Pub', 'Golden Singha Thai Cuisine', 'Uptown China Restaurant', 'Mama\'s Mexican Kitchen', 'Taco Del Mar']

LOCATIONS = ['Taqueria Jalisco (J/K)', 'CJ\'s Eatery', 'Rice \'n Spice', 'Local 360', 'The Lucky Diner', 'The 5 Point Cafe', 'Buckley\'s in Belltown', 'Sushi Wave', 'Sushi Mori', 'Belltown Pub', 'Golden Singha Thai Cuisine', 'Mama\'s Mexican Kitchen', 'Taco Del Mar']

def make_decision():
    # randint = a >= x <= b
    potential = LOCATIONS[randint(0, len(LOCATIONS)-1)]

    # only display Buckley's if it's Friday
    if 'Buckley\'s' in potential and date.today().isoweekday() != 5:
        return make_decision()

    return potential

class MainPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, {}))

    def post(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, {'restaurant': make_decision()}))

application = webapp.WSGIApplication(
                                     [
                                        ('/', MainPage),
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
