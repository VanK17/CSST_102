#@title **1. Logical Operations (Alternative Example)**
#@markdown # **Input Values:**
first_value = "True" #@param ["True"] {allow-input: false}
p_input = first_value
second_value = "False" #@param ["False"] {allow-input: false}
q_input = second_value

#@markdown - ### Expected Results:
#@markdown  - AND : False
#@markdown  - OR : True
#@markdown  - NOT first_value : False
#@markdown  - IMPLIES : False

# Convert the string inputs to booleans
p = p_input == "True"
q = q_input == "True"

# Output results of logical operations
print("AND Result:", logical_and(p, q))        # False
print("OR Result:", logical_or(p, q))          # True
print("NOT first_value:", logical_not(p))      # False
print("IMPLIES Result:", logical_implies(p, q))# False