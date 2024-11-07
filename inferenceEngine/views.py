from django.shortcuts import render
from abc import ABC, abstractmethod
from typing import List, TypeVar, Optional
from .models import Rule
from .lang_parser import RuleParser

# Define type variables for input and output data
INPUT_DATA = TypeVar('INPUT_DATA')
OUTPUT_RESULT = TypeVar('OUTPUT_RESULT')

class InferenceEngine(ABC):
    def run(self, list_of_rules, input_data):
        """
        Run inference engine on set of rules for given data.
        """
        if not list_of_rules:
            return None

        # STEP 1 (MATCH): Match the facts and data against the set of rules.
        conflict_set = self.match(list_of_rules, input_data)

        # STEP 2 (RESOLVE): Resolve the conflict and give the selected one rule.
        resolved_rule = self.resolve(conflict_set)
        if not resolved_rule:
            return None

        # STEP 3 (EXECUTE): Run the action of the selected rule on the given data and return the output.
        return self.execute_rule(resolved_rule, input_data)

    # def __init__(self, rule_parser: RuleParser):
    #     self.rule_parser = rule_parser

    # def run(self, list_of_rules: List[Rule], input_data: INPUT_DATA) -> Optional[OUTPUT_RESULT]:
    #     """
    #     Run inference engine on set of rules for given data.
    #     """
    #     if not list_of_rules:
    #         return None

    #     # STEP 1 (MATCH): Match the facts and data against the set of rules.
    #     conflict_set = self.match(list_of_rules, input_data)

    #     # STEP 2 (RESOLVE): Resolve the conflict and give the selected one rule.
    #     resolved_rule = self.resolve(conflict_set)
    #     if not resolved_rule:
    #         return None

    #     # STEP 3 (EXECUTE): Run the action of the selected rule on the given data and return the output.
    #     return self.execute_rule(resolved_rule, input_data)

    # def match(self, list_of_rules: List[Rule], input_data: INPUT_DATA) -> List[Rule]:
    #     """
    #     Use pattern matching (here, linear matching) to filter the list of rules based on the condition.
    #     """
    #     return [
    #         rule for rule in list_of_rules
    #         if self.rule_parser.parse_condition(rule.condition, input_data)
    #     ]

    # def resolve(self, conflict_set: List[Rule]) -> Optional[Rule]:
    #     """
    #     Resolve the conflict and return the first matching rule.
    #     """
    #     if conflict_set:
    #         return conflict_set[0]
    #     return None

    # def execute_rule(self, rule: Rule, input_data: INPUT_DATA) -> OUTPUT_RESULT:
    #     """
    #     Execute the selected rule's action on the input data.
    #     """
    #     output_result = self.initialize_output_result()
    #     return self.rule_parser.parse_action(rule.action, input_data, output_result)

    # @abstractmethod
    # def initialize_output_result(self) -> OUTPUT_RESULT:
    #     """
    #     Initialize the output result. This method should be implemented by subclasses.
    #     """
    #     pass

    # @abstractmethod
    # def get_rule_namespace(self):
    #     """
    #     Get the rule namespace. This method should be implemented by subclasses.
    #     """
    #     pass
