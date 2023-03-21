import logging
import openai
import os
from shared_code import constants as c #(relative)
import azure.functions as func

# Sample Request 
# {"api_secret":"<openai secret>","model":"text-davinci-003","prompt": "give me a slogan cookie company", "max_tokens":1000,"temperature"=0}

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Get parameters from request body
    openai.api_type = c.apiType
    openai.api_base = c.apiBase
    openai.api_version = c.apiVersion
    openai.api_key = os.environ["OpenAI"]
    request_body = req.get_json()


    # Authenticate with openAI API secret
    # Call the openAI API
    try:

            response = openai.Completion.create(
            engine = c.model
            , prompt = request_body['prompt']
            , max_tokens = request_body['max_tokens']
            , temperature = request_body['temperature']
            , top_p = c.topP
            , frequency_penalty = c.frequencyPenalty
            , presence_penalty = c.presensePenalty
            , best_of = c.bestOf
            , stop = None
            )
    except:
        logging.info('OpenAI API request failed')
        return func.HttpResponse("Bad request. Malformed request body for OpenAI Completion create api",status_code=400)
        

    # Format the response
    response = response.choices[0].text.strip()

    # Provide the response back to http client
    return func.HttpResponse(response,status_code=200)