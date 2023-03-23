import logging
import openai
import os
from requests.exceptions import HTTPError
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    
    
    # Authenticate with openAI API secret
    # Validate request body
    # Call the openAI API
     try:
               request_body = req.get_json()
               logging.info(str(request_body))
               openai.api_key = os.environ["OpenAIDALLE"]
               response = openai.Image.create(
                    prompt = request_body['prompt']
                    , n = request_body['n']
                    , size = request_body['size']
               )
     except HTTPError as http_e:
          response = f"Http error occured {http_e}"
          return  func.HttpResponse(response,status_code = http_e.response.status_code)
     except Exception as e:
          response = str(e)
          statusCode = 200
          if response.lower() == "'prompt'" or response.lower() == "'n'" or response.lower() == "'size'":
             statusCode = 400
             response = "Request Body Exception: " + response  + " parameter is missing from JSON!"
          elif response.__contains__("is not of type"):
             statusCode = 400
             response = "Request Body Exception: " + response
          elif response.__contains__("does not contain valid JSON data"):
             statusCode = 400
             response = "Request Body Exception: " + response 
          else:
             statusCode = 500
             response = "Response Exception: " + response 
          logging.error(response)
          return  func.HttpResponse(response, status_code = statusCode)

     # Get image
     response = response['data'][0]['url']

     # Provide the response back to http client
     return func.HttpResponse(response,status_code=200)