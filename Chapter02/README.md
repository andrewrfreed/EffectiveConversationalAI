# Running the sample code in watsonx.ai and watsonx Assistant

This folder has the resources you need for running the code demonstrated in Chapter 2.  There are two primary steps:
1. Create an account and resources on the IBM cloud
2. Configure the resources to run the tutorial

## Creating your resources
You will need three things:
1. An account on the IBM Cloud
2. An instance of Watson Machine Learning instance (for watsonx.ai)
3. An instance of watsonx Assistant

### IBM Cloud account
Create an IBM Cloud account at https://cloud.ibm.com/ (look for the "Create an account" option)

### Watson Machine Learning
Create a Watson Machine Learning instance for watsonx.ai.  This video (https://youtu.be/QLr6MoOV6Hg) walks through the steps.  Be sure to capture the API key and project ID.

### watsonx Assistant
Create a watsonx Assistant instance.  This tutorial (https://ibm.github.io/vending-machine-instructions/exercise-01/) walks through the steps.  Nnote that you can use any names you like, such as in steps 3 & 8.

## Configuring the code
Our tutorial is based on the general steps from IBM watsonx language model starter kit (https://github.com/watson-developer-cloud/assistant-toolkit/tree/master/integrations/extensions/starter-kits/language-model-watsonx)
1. Create an API key and a project ID for watsonx
2. Use the Watson Assistant you created in the previous section
3. Connect your assistant to watsonx using an Integration and the watsonx-openapi.json file.  Configure it to use the API key from watsonx.ai
4. Upload the sample assistant code from CakeBot-action.json (this overwrites your 'empty' assistant)
5. In Actions menu, find "Show me a recipe for", go to step 4 and change the project_id parameter to your watsonx project ID.
6. Use the Preview option to start asking questions to your chatbot!
