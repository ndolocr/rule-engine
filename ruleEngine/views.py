from django.shortcuts import render
from KnowledgeBase.rulesRepository import RulesRepository

# Create your views here.
class RuleEngine:
    def __init__(self):
        self.rules_object = RulesRepository()

    def run(self, rule_namespace, input_data: object) -> object:
        """
        Runs the inference engine with rules fetched from the knowledge base.

        Args:
            inference_engine (InferenceEngine): The inference engine to apply the rules.
            input_data (object): The input data to be processed by the inference engine.

        Returns:
            object: The result of the inference engine processing.
        """
        
        # Fetch rules from knowledge base for the given namespace
        all_rules_by_namespace = self.rules_object.find_by_rule_namespace(rule_namespace)
        
        # Run the inference engine with the fetched rules and input data
        result = inference_engine.run(all_rules_by_namespace, input_data)
        
        return result