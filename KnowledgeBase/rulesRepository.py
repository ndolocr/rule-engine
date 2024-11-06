from KnowledgeBase.models import Rule

class RulesRepository:
    def __init__(self):
        # This could be an instance variable for database access or a specific manager, if needed
        pass

    def find_by_rule_namespace(self, rule_namespace: str):
        """
        Fetch rules by rule namespace.
        """
        return Rule.objects.filter(rule_namespace=rule_namespace)

    def find_all(self):
        """
        Fetch all rules.
        """
        return Rule.objects.all()
