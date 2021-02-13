from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from .models import Group
from .models import BaseGroup

class MyPage(Page):
    pass

class Intro(Page):
    pass

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

class Contribution(Page):
    form_model = 'player'
    form_fields = ['contribution']


    pass

page_sequence = [MyPage, Contribution, Results]
