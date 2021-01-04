import mongoengine

from src.data.rule.rule_model import RuleModel


class RuleUnDonePastDueTradesCount(mongoengine.Document, RuleModel):

    meta = {
        'db_alias': 'core',
        'collection': 'rulesUnDonePastDueTradesCounts'
    }
