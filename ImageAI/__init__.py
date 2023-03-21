import logging
import openai
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:

    request_body = req.get_json()


    # Authenticate with openAI API secret
    # Call the openAI API
    try:
            openai.api_key = request_body['api_secret']
            response = openai.Image.create(
            prompt = request_body['prompt']
            , n = request_body['n']
            , size = request_body['size']
            )
    except:
        logging.info(request_body)
        return func.HttpResponse("Bad request. Malformed request body for OpenAI Image create api",status_code=400)
        

    # Get image
    response = response['data'][0]['url']

    # Provide the response back to http client
    return func.HttpResponse(response,status_code=200)