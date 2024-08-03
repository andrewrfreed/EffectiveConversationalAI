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
Alternately, you can create a Watson Machine Learning instance directly from https://cloud.ibm.com/catalog/services/watson-machine-learning

### watsonx Assistant
Create a watsonx Assistant instance.  This tutorial (https://ibm.github.io/vending-machine-instructions/exercise-01/) walks through the steps.  Note that you can use any names you like, such as in steps 3 & 8.
Alternately, you can create a watsonx Assistant instance directly from https://cloud.ibm.com/catalog/services/watsonx-assistant

## Configuring the code
Make sure you have opened your watsonx Assistant instance.  You can find it from https://cloud.ibm.com/resources in the AI/Machine Learning section.  After you've click "Launch watsonx Assistant" be sure you have created a new Assistant.  Now you're ready to configure the Assistant (chatbot) to run the Chapter 2 code!

Our tutorial steps are based on the general steps from IBM watsonx language model starter kit (https://github.com/watson-developer-cloud/assistant-toolkit/tree/master/integrations/extensions/starter-kits/language-model-watsonx). Click through that guide for more details on the high-level steps below.
1. Find/create an API key and a project ID for watsonx (these may have been created by default)
2. Use the Watson Assistant you created in the previous section
3. Connect your assistant to watsonx using an Integration and the watsonx-openapi.json file.  Configure it to use the API key from watsonx.ai. ([Screenshot when done](images/configure-watsonx-extension.png))
4. Upload the sample assistant code from CakeBot-action.json (this overwrites your 'empty' assistant).(Upload [screenshot 1](images/upload-assistant-step-1.png) and [screenshot 2](images/upload-assistant-step-2.png))
5. In Actions menu, find "Show me a recipe for", go to step 4 and change the project_id parameter to your watsonx project ID. ([List Actions screenshot](images/list-of-actions.png) and [Set project ID screenshot](images/set-project-id.png))
6. Use the Preview option to start asking questions to your chatbot! ([Screenshot: FAQ](images/preview-page-1.png) and [Screenshot: Generative AI](images/preview-page-2.png))
