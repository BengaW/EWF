from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Introduction(Page):
    pass


class Userfit(Page):
    form_model = 'player'
    form_fields = ['knows_amazon', 'buys_from_amazon']


class Round0(Page):
    form_model = 'player'
    form_fields = ['decision0']
    price_difference1 = 0


class Round1(Page):
    form_model = 'player'
    form_fields = ['decision10']
    price_difference1 = 50


class Round2(Page):
    form_model = 'player'
    form_fields = ['decision20']
    price_difference2 = 50


class Round3(Page):
    form_model = 'player'
    form_fields = ['decision30']


class Round4(Page):
    form_model = 'player'
    form_fields = ['decision40']


class Round5(Page):
    form_model = 'player'
    form_fields = ['decision50']


class Round6(Page):
    form_model = 'player'
    form_fields = ['decision60']


class Results(Page):
    def js_vars(player):
        decision_counts = player.group.decision_counts
        return dict(
            decision_counts=decision_counts
        )


page_sequence = [Introduction, Userfit, Round0, Round1, Round2, Round3, Results]
