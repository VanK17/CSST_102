#@title 2. **Evaluate Logical Statements (Example)**

#@markdown # **Input Data:**
first_val = "True" #@param ["True"] {allow-input: false}
second_val = "False" #@param ["False"] {allow-input: false}
third_val = "True" #@param ["True"] {allow-input: false}
#@markdown - Expected result: FALSE

# Logical expression and corresponding truth values
expr = "(first and second) or not third"
truth_values = {'first': True, 'second': False, 'third': True}

# Process the logical expression
print("Result of Expression:", evaluate_expression(expr, truth_values))  # Expected result: False