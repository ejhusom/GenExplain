import os
from autogen import ConversableAgent

class EvaluatorAgent(ConversableAgent):
    def __init__(self, name="EvaluatorAgent", system_message="I evaluate the quality of explanations generated by other agents.", **kwargs):
        # Initialize with the name and system message, along with other configurations
        super().__init__(name=name, system_message=system_message, **kwargs)
        self.evaluation_log = []  # Store the results of each evaluation

    def evaluate_explanation(self, explanation):
        """Evaluate the given explanation using an LLM.
        
        Args:
            explanation (str): The explanation to evaluate.

        Returns:
            dict: A dictionary containing the evaluation feedback.
        """
        # Craft the prompt to instruct the LLM on how to evaluate the explanation
        prompt = f"""
        You are an AI agent tasked with evaluating the quality of the following explanation. Please assess it based on clarity, relevance, and completeness. Provide your feedback and suggestions for improvement if necessary.

        Explanation:
        {explanation}

        Please provide your evaluation in the following format:
        - Clarity: [Your assessment here]
        - Relevance: [Your assessment here]
        - Completeness: [Your assessment here]
        - Suggestions: [Your suggestions for improvement, if any]
        """

        # Send the prompt to the LLM for evaluation
        response = self.generate_reply({"role": "system", "content": prompt})
        evaluation_result = response["content"]

        # Log the evaluation result
        self.evaluation_log.append({
            "explanation": explanation,
            "evaluation": evaluation_result
        })

        return evaluation_result

    def generate_reply(self, msg):
        """Override this method to handle incoming messages and evaluate explanations."""
        if msg.get('role') == 'system' and msg.get('content') == 'evaluate_explanation':
            explanation = msg.get('explanation', "")
            evaluation_result = self.evaluate_explanation(explanation)
            return {"role": "system", "content": f"Evaluation Result: {evaluation_result}"}
        
        # If the message is something else, you can add additional conditions here
        return super().generate_reply(msg)  # Default to the base class behavior

    def get_evaluation_log(self):
        """Retrieve the full log of evaluations performed."""
        return self.evaluation_log

    def is_termination_msg(self, msg):
        """Override if you want to define specific termination criteria."""
        return False

if __name__ == "__main__":
    # Example instantiation of the EvaluatorAgent
    evaluator = EvaluatorAgent(
        llm_config={"config_list": [{"model": "gpt-4", "api_key": os.environ.get("OPENAI_API_KEY")}]},
        human_input_mode="NEVER"  # Never ask for human input.
    )

    # Simulating evaluation of an explanation
    sample_explanation = "At 10:05, an AI_Action event occurred with details: {'action': 'move', 'direction': 'north'}."
    evaluation_result = evaluator.evaluate_explanation(sample_explanation)
    print(evaluation_result)

