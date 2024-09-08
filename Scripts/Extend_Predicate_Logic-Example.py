#@title **3. Extend Predicate Logic (Example)**

#@markdown # **Set of Values:**
item1 = 10 #@param ["10"] {allow-input: false}
item2 = 20 #@param ["20"] {allow-input: false}
item3 = 30 #@param ["30"] {allow-input: false}
item4 = 40 #@param ["40"] {allow-input: false}
item5 = 50 #@param ["50"] {allow-input: false}

# Create a list from the individual items
values = [item1, item2, item3, item4, item5]

# Define a condition to apply
check_condition = lambda n: n > 35

#@markdown - ### Expected Results:
#@markdown  - FOR ALL: FALSE
#@markdown  - EXISTS: TRUE

# Evaluate the condition for all and some elements
print("FOR ALL:", check_forall(check_condition, values)) # False
print("EXISTS:", check_exists(check_condition, values))  # True