#Parameters for Azure OpeaAI API configuration
class OpeanAICompletion:
        API_TYPE = "Azure"
        API_BASE = "https://oai-gptdemo-dev-eastus-01.openai.azure.com/"
        API_VERSION = "2022-12-01"
        GPT_ENGINE = "gpt-davinci003-demo-eastus-01"

        #Parameters for Azure's OpenAI completion API
        TOP_P = 0.5
        FREQUENCY_PENALTY = 0
        PRESENCE_PENALTY =  0
        BEST_OF = 1

