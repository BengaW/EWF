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

    @property
    def decision_counts(self):
        total_decision_counts = []
        for player in self.get_players():
            decisions = player.get_decisions()
            if len(total_decision_counts) < 1:
                total_decision_counts = decisions
            else:
                for i, decision in enumerate(decisions):
                    total_decision_counts[i] += decision
        return total_decision_counts


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

    def get_decisions(self):
        # Erklaerung: map(function, iterierbares_objekt) wendet die funktion auf jedes elemnt im iterierbarem objekt an. Lambda sind 'anonyme' funktionen, wir koennten aber auch normale funktionen stattdessen benutzten. Seit Python3 gibt die map(...)-funktion keine ausgewertete liste der funktions-ergebnisse (von lambda) mehr zuruck, sondern map-objekt-referenzen (warum ist an dieser stelle egal). Um an eine Liste zu kommen muessen wir daher list(map(...)) anwenden.
        return list(map(lambda x: int(x or 0), self.get_decision_fields()))

    def get_decision_fields(self):
        return [self.decision0, self.decision10, self.decision20, self.decision30, self.decision40, self.decision50, self.decision60]
