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

LOCATIONS = {
    'Taqueria Jalisco (J/K)': {
        'availability': ALL_DAYS,
    },
    'Buckley\'s': {
        'availability': (FRIDAY,),
        'description': '?',
    },
    'Chipotle': {
        'availability': ALL_DAYS,
        'description': 'The best restaurant known to mankind.'
    },
    'Subway': {
        'availability': ALL_DAYS,
        'description': 'The secrets of sandwiches that have been passed '
                       'down for centuries, condensed and culminated into '
                       'this restaurant.'
    },
    'Curb Jumper': {
        'availability': (MONDAY, WEDNESDAY),
        'description': "Sliders, burgers and fries."
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
        'description': 'I have no idea what they serve, really.'
    },
    'Sam Choy\'s Poke': {
        'availability': (WEDNESDAY,),
        'description': 'Pokes! Delicous Yakitori bowls.'
    },
    'Plum': {
        'availability': (WEDNESDAY, FRIDAY),
        'description': 'Vegetarian food if you\'re into that kind of thing!'
    },
    'Off the Rez': {
        'availability': (THURSDAY,),
        'description': 'Indian Tacos'
    },
    'Buns': {
        'availability': (FRIDAY,),
        'description': 'Exactly what it sounds like.'
    },
    'Nosh': {
        'availability': (FRIDAY,),
        'description': 'Good British food, fish and chips, mushy peas.'
    },
    'Ferry Noodle House': {
        'availability': ALL_DAYS,
        'description': 'Order online at http://www.ferrynoodlehouseseattle.com'
    },
    'Okinawa': {
        'availability': ALL_DAYS,
        'description': 'The most trusted teriyaki around.'
    },
    'Specialty\'s': {
        'availability': ALL_DAYS,
        'description': 'Precision crafted sandwiches.'
    },
    'Mel\'s': {
        'availability': ALL_DAYS,
        'description': 'A little bit farther than Specialty\'s'
    },
    'Melange': {
        'availability': (WEDNESDAY,),
        'description': 'Everybody\'s favorite chicken parm.'
    },
    'The Metropolitan Grill': {
        'availability': (SATURDAY, SUNDAY,),
        'description': 'You\'re working too hard! Treat yourself.'
    },
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

    def _show_random_restaurant(self):
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        weekday = date.today().isoweekday()
        self.response.out.write(template.render(path,
                                {'restaurant': make_decision(weekday)}))

    def get(self):
        self._show_random_restaurant()

    def post(self):
        self._show_random_restaurant()

application = webapp.WSGIApplication(
                                     [
                                        ('/', MainPage),
                                     ],
                                     debug=True)


def main():
    run_wsgi_app(application)


if __name__ == "__main__":
    main()
