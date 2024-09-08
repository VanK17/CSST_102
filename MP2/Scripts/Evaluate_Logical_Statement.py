#@title **2. Evaluate Logical Statements**

import re

def evaluate_expression(logic_expr, var_mapping):
    """
    Evaluates a logical expression by replacing variables with their corresponding
    boolean values and adjusting the logical operators to match Python's syntax.

    :param logic_expr: str, the logical expression to be evaluated (e.g., "A AND B OR NOT C").
    :param var_mapping: dict, a mapping of variables (e.g., 'A', 'B') to their boolean values (True/False).
    :return: bool, the result of evaluating the logical expression.
    """
    # Replace each variable in the expression with its corresponding boolean value
    for key, value in var_mapping.items():
        # Use regular expressions to ensure that only full variable names are replaced
        logic_expr = re.sub(rf'\b{key}\b', str(value), logic_expr)

    # Convert logical operators from string format to Python's syntax
    logic_expr = logic_expr.replace('AND', 'and').replace('OR', 'or').replace('NOT', 'not')

    try:
        # Evaluate the modified expression and return the result
        return eval(logic_expr)
    except Exception as ex:
        # Handle any errors during evaluation and provide feedback
        print(f"Error during evaluation: {ex}")
        return None