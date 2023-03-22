import logging
import openai
import os
import requests
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:

    request_body = req.get_json()


    # Authenticate with openAI API secret
    # Call the openAI API
    try:
            openai.api_key = os.getenv("OpenAIDALLE")
            response = openai.Image.create(
            prompt = request_body['prompt']
            , n = request_body['n']
            , size = request_body['size']
            )
    except Exception as e:
        logging.info(request_body)
        return func.HttpResponse("Bad request: "+ str(e),status_code=500)
        

    # Get image
    response = response['data'][0]['url']

    # Provide the response back to http client
    return func.HttpResponse(response,status_code=200)