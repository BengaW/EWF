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
import csv


author = 'Benedikt Wagner'

doc = """
Experimentelle Wirtschaftsforschung Abgabe
"""


class Constants(BaseConstants):
    name_in_url = 'EWF_1'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):

    pass


class Group(BaseGroup):
    total_other = models.IntegerField()


    
    pass


class Player(BasePlayer):
    result = models.IntegerField()
    number_of_participants = models.IntegerField()
    mean_correct = models.IntegerField()


    decision0 = models.BooleanField(
        choices=[
            [False, 'Amazon'],
            [True, 'Other'],
        ]
    )
    decision10 = models.BooleanField(
        choices=[
            [False, 'Amazon'],
            [True, 'Other'],
        ]
    )
    decision20 = models.BooleanField(
        choices=[
            [False, 'Amazon'],
            [True, 'Other'],
        ]
    )
    decision30 = models.BooleanField(
        choices=[
            [False, 'Amazon'],
            [True, 'Other'],
        ]
    )
    decision40 = models.BooleanField(
        choices=[
            [False, 'Amazon'],
            [True, 'Other'],
        ]
    )
    decision50 = models.BooleanField(
        choices=[
            [False, 'Amazon'],
            [True, 'Other'],
        ]
    )
    decision60 = models.BooleanField(
        choices=[
            [False, 'Amazon'],
            [True, 'Other'],
        ]
    )

    knows_amazon = models.BooleanField()
    buys_from_amazon = models.BooleanField()

    pass


