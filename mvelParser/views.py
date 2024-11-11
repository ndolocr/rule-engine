import re

# Create your views here.
class MVELParser:
    def convert_mvel_to_python(self, expression):
        """
        This function takes MVEL Expressions from the 
        database and converts them into python understable statments.

        MVEL-style syntax isn’t directly compatible with Python’s eval. Specifically:

        1. MVEL Syntax Compatibility: MVEL uses operators like && 
        for logical "AND" and == for equality, which need to be replaced with and and == in Python.
        
        2. Dynamic Data Reference: Expressions such as 
        input.dr.transactionType == 'AirtelMoney' need to be adjusted so Python can properly access 
        nested dictionary values (e.g., input['dr']['transactionType']).
        
        3. Undefined Variables: Placeholder variables 
        like $(bank.target_done) need to be replaced with actual data from your input_objects.

        """
        # Convert dot notation to dictionary-style access
        expression = re.sub(r"(\w+)\.(\w+)\.(\w+)", r"\1['\2']['\3']", expression)
        expression = re.sub(r"(\w+)\.(\w+)", r"\1['\2']", expression)
        expression = expression.replace("&&", "and").replace("||", "or")

        return expression

    def parse_mvel_expression(self, action, conditions, input_objects):
        """
        Parses and evaluates an expression using the provided input objects.
        
        Args:
            expression (str): The MVEL-like expression to evaluate.
            input_objects (dict): A dictionary of input variables for the expression.

        Returns:
            bool: The result of evaluating the expression as a boolean.
        """
        try:
            # Use eval with input_objects as the context
            # Note: `eval` has security risks and should be used cautiously. 
            # Use an alternative if more security is required.
            print(f"MVEL Expression ====> {conditions}")
            python_expression = self.convert_mvel_to_python(conditions)
            print(f"GOT PYTHON EXPRESSION ===> {python_expression}")

            result = eval(python_expression, {}, input_objects)
            print(f"RESULT ==> {result}")

            if result:
                match = re.search(r'\((\d+)\)', action)
                if match:
                    score = int(match.group(1))
                    print(f"Score --> {score}")
                return score
            else:
                return 0
        except Exception as e:
            print(f"Error: --> {e}")
            return False

    