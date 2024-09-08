#@title **4. AI Agent Development (Example Usage)**
#@markdown # **Define the Inputs:**

# Define input for "urgent_task" in the personal context
task_urgent = "False"  #@param ["True", "False"] {allow-input: true}

# Define input for "available_time" in the personal context
time_available = "True" #@param ["True", "False"] {allow-input: true}

# Initialize the decision-making assistant
assistant = DecisionAssistant(context)

# Set inputs based on the chosen context
if context == "personal":
    inputs = {'urgent_task': task_urgent == "True", 'available_time': time_available == "True"}

# Determine and display the assistant's decision
print("Assistant's Decision:", assistant.determine_action(inputs))