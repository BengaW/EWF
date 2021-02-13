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


class Constants(BaseConstants):
    name_in_url = 'public_goods_simple'
    players_per_group = 3
    num_rounds = 1



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    total_contribution = models.CurrencyField()

    def vars_for_template(self):
        players = self.get_players()
        contributions = [p.contribution for p in players]
        self.total_contribution = sum(contributions)
        a = sum(contributions)
        return dict(
            a=a,
        )

    def set_payoffs(self):
        contributions = [p.contribution for p in self.get_players()]
        self.total_contribution = sum(contributions)


class Player(BasePlayer):
    contribution = models.CurrencyField(
        min=0, max=100, label="How much will you contribute?"
    )
