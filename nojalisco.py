import os
from datetime import date
from random import randint
from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

MONDAY = 1
TUESDAY = 2
WEDNESDAY = 3
THURSDAY = 4
FRIDAY = 5
SATURDAY = 6
SUNDAY = 7
ALL_DAYS = [x for x in range(8) if x != 0]

#LOCATIONS = ['Taqueria Jalisco', 'CJ\'s Eatery', 'Rice \'n Spice', 'Barracuda Taqueria', 'Local 360', 'The Lucky Diner', 'Boat Street Cafe', 'The 5 Point Cafe', 'Buckley\'s in Belltown', 'Sushi Wave', 'Sushi Mori', 'Belltown Pub', 'Golden Singha Thai Cuisine', 'Uptown China Restaurant', 'Mama\'s Mexican Kitchen', 'Taco Del Mar']

#LOCATIONS = ['Taqueria Jalisco (J/K)', 'CJ\'s Eatery', 'Rice \'n Spice', 'Local 360', 'The Lucky Diner', 'The 5 Point Cafe', 'Buckley\'s in Belltown', 'Sushi Wave', 'Sushi Mori', 'Belltown Pub', 'Golden Singha Thai Cuisine', 'Mama\'s Mexican Kitchen', 'Taco Del Mar']

LOCATIONS = {
    'Buckley\'s': {
        'availability': (FRIDAY,)
    },
    'Chipotle': {
        'availability': ALL_DAYS,
        'description': 'the best restaurant known to mankind'
    },
    'Subway': {
        'availability': ALL_DAYS,
        'description': 'the secrets of sandwiches that have been past down for centuries, condensed and culminated into this restaurant'
    },
    'Curb Jumper': {
        'availability': (MONDAY, WEDNESDAY),
        'description': "sliders, burgers and fries"
    },
    'Marination': {
        'availability': (TUESDAY,),
        'description': 'Hawaiin-Korean cuisine'
    },
    'Jemil\'s': {
        'availability': (TUESDAY,),
        'description': 'Cajun cooking, with ro-boys'
    },
    'Barking Frog': {
        'availability': (TUESDAY, THURSDAY),
        'description': 'I have no idea what they serve, really'
    },
    'Sam Choy\'s Poke': {
        'availability': (WEDNESDAY,),
        'description': 'Pokes!'
    },
    'Plum': {
        'availability': (WEDNESDAY, FRIDAY),
        'description': 'Vegetarian food!'
    },
    'Off the Rez': {
        'availability': (THURSDAY,),
        'description': 'Indian Tacos'
    },
    'Buns': {
        'availability': (FRIDAY,),
        'description': 'Buns?'
    },
    'Nosh': {
        'availability': (FRIDAY,),
        'description': 'good British food.'
    }
}


def make_decision(weekday):
    # randint = a >= x <= b
    choices = LOCATIONS.keys()
    choice = None
    while choice is None:
        potential = choices[randint(0, len(choices)-1)]
        if weekday in LOCATIONS[potential]['availability']:
            choice = potential

    return {
        'name': choice,
        'description': LOCATIONS[choice].get('description', '')
    }


class MainPage(webapp.RequestHandler):
    def get(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, {}))

    def post(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, {'restaurant': make_decision(date.today().isoweekday())}))

application = webapp.WSGIApplication(
                                     [
                                        ('/', MainPage),
                                     ],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
