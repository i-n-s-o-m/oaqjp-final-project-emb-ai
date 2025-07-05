import requests  # Import the requests library to handle HTTP requests

# Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector(text_to_analyse):
    
    # URL of the emotion predict service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Create a dictionary with the text to be analysed
    myobject = { "raw_document": { "text": text_to_analyse } }
    
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Send a POST request to the API with the text and header
    response = requests.post(url, json = myobject, headers=header)

    # Return the response text from the API
    return response.text_to_analyse
    
