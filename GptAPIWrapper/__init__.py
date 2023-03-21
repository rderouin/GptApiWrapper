import logging
import openai
import os
import azure.functions as func

# Sample Request 
# {"api_secret":"<openai secret>","model":"text-davinci-003","prompt": "give me a slogan cookie company", "max_tokens":1000,"temperature"=0}

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Get parameters from request body
    openai.api_type = "Azure"
    openai.api_base = "https://oai-gptdemo-dev-eastus-01.openai.azure.com/"
    openai.api_version = "2022-12-01"
    openai.api_key = os.environ["OpenAI"]
    request_body = req.get_json()


    # Authenticate with openAI API secret
    # Call the openAI API
    try:

            response = openai.Completion.create(
            engine = "gpt-davinci003-demo-eastus-01"
            , prompt = request_body['prompt']
            , max_tokens = request_body['max_tokens']
            , temperature = request_body['temperature']
            , top_p = 0.5
            , frequency_penalty = 0
            , presence_penalty = 0
            , best_of = 1
            , stop = None
            )
    except:
        logging.info('OpenAI API request failed')
        return func.HttpResponse("Bad request. Malformed request body for OpenAI Completion create api",status_code=400)
        

    # Format the response
    response = response.choices[0].text.strip()

    # Provide the response back to http client
    return func.HttpResponse(response,status_code=200)