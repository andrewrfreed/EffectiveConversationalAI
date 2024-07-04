
def get_prompt(guidance, transcript):
   prompt=f'''
INSTRUCTION:
You are a user trying to find the your claim status.
{guidance}
Continue the conversation with a likely response.

CONVERSATION:
{transcript}
User: '''
   return prompt

def call_chatbot(message):
    ## Replace this with an actual call to your chatbot provider.
    ## Implementation details vary by platform

    ## For Watson Assistant, initialize an Assistant then use message() function
    #https://cloud.ibm.com/apidocs/assistant-v2?code=python#createassistant
    #https://cloud.ibm.com/apidocs/assistant-v2?code=python#messagestateless

    ## To play the role of the chatbot, use this line instead
    return input('Enter the bot response: ')

    ## Hardcoding responses for demo only!
    canned_responses = {}
    canned_responses[""] = "How can I help you?"
    canned_responses["Hi, I'd like to check the status of a medical claim."] = "I can help you with that. What is your member ID?"
    canned_responses["Yes, my member ID is 123456."] = "What is your claim date?"
    canned_responses["My claim date is May 4, 2024."] = "What is your claim amount?"
    canned_responses["The claim amount was $1000."] = '''Thank you. I have all the information I need. Let me check the status of your claim.
The status of your claim is approved and the amount of $1000 has been paid.'''

    return canned_responses.get(message, "error")

def call_llm(message):
    ## Replace this with an actual call to your LLM provider.
    ## Implementation details vary by platform

    # Example call to watsonx.ai - initiate a Model then call generate()
    # https://ibm.github.io/watson-machine-learning-sdk/model.html#ibm_watson_machine_learning.foundation_models.Model
    # https://ibm.github.io/watson-machine-learning-sdk/model.html#ibm_watson_machine_learning.foundation_models.Model.generate

    ## Hardcoding responses for demo only!
    if "What is your claim amount?" in message:
       return "The claim amount was $1000."
    if "What is your claim date?" in message:
       return "My claim date is May 4, 2024."
    if "I can help you with that. What is your member ID?" in message:
       return "Yes, my member ID is 123456."
    if "How can I help you?" in message:
       return "Hi, I'd like to check the status of a medical claim."

    return ""

def run_test(guidance):
   print(f"Running test with:\n{guidance}\n")
   bot_response = call_chatbot("")
   transcript = f"System: {bot_response}"
   for i in range(4):
      prompt=get_prompt(guidance, transcript)
      user_response=call_llm(prompt)
      transcript += f"\nUser: {user_response}"
      bot_response=call_chatbot(user_response)
      transcript += f"\nSystem: {bot_response}"
   print(f"Transcript:\n{transcript}")

if __name__ == "__main__":
   guidance='''You are trying to find out if one of your medical claims was paid.
You know your member ID 123456, claim date of May 4, 2024, and the claim amount of $100.'''
   run_test(guidance)
