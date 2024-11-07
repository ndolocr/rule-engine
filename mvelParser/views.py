from django.shortcuts import render

# Create your views here.
class MVELParser:
    def parse_mvel_expression(self, action, condition, input_objects):
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
            result = eval(condition, {}, input_objects)
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
            logger.error(f"Cannot parse MVEL expression: {expression} Error: {str(e)}")
            return False