from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Benedikt Wagner'

doc = """
Nur zum testen.
"""


class Constants(BaseConstants):
    name_in_url = 'testapp'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.IntegerField()

    def set_payoffs(self):
        self.total_contribution = sum([p.contribution for p in self.get_players()])

    pass


class Player(BasePlayer):
    contribution = models.IntegerField()

    pass
