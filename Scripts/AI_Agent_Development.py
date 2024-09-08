#@title **4. AI Agent Development**

#@markdown ## **Choose Scenario:**
context = "personal" #@param ["personal", "professional"] {allow-input: true}

class DecisionAssistant:
    def __init__(self, context):
        """
        Initialize the decision-making assistant with a specific context.

        :param context: str, the context for making decisions.
        """
        self.context = context

    def determine_action(self, inputs):
        """
        Decide on an action based on the provided inputs and context.

        :param inputs: dict, a dictionary of input factors and their values.
        :return: str, the determined action based on the context.
        """
        if self.context == "personal":
            if inputs['urgent_task']:
                return "Prioritize Task"
            elif inputs['available_time']:
                return "Relax"
            else:
                return "Check Schedule"
        elif self.context == "professional":
            if inputs['meeting_scheduled']:
                return "Prepare for Meeting"
            elif inputs['deadline_approaching']:
                return "Complete Work"
            else:
                return "Plan Next Steps"