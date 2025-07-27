import requests # Import the requests library to handle HTTP requests

def emotion_detector(text_to_analyze): # Define a function named emotion_detector that takes a string input (text_to_analyze)
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'# URL of the emotion detector service
    input_json = { "raw_document": { "text": text_to_analyze } } # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Set the headers required for the API request
    response = requests.post(URL, json = input_json, headers=header) # Send a POST request to the API with the text and headers
    return response.text # Return the response text from the API