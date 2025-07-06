import requests  # Import the requests library to handle HTTP requests
import json

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

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)



    # Access the 'emotionPredictions' list
    emotion_predictions = formatted_response.get('emotionPredictions')

    # If the response status code is 200, extract the label and score from the response
    if response.status_code == 200:
        # Access the first item in the 'emotionPredictions' list
        first_prediction = emotion_predictions[0]

        # Access the 'emotion' dictionary within that item
        emotion_scores = first_prediction.get('emotion')

        # Extract the individual scores
        anger_score = emotion_scores.get('anger')
        disgust_score = emotion_scores.get('disgust')
        fear_score = emotion_scores.get('fear')
        joy_score = emotion_scores.get('joy')
        sadness_score = emotion_scores.get('sadness')

        # Construct the output dictionary
        emotion_dictionary = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }

        # --- Logic to find the dominant emotion ---

        # Find the key (emotion name) with the maximum value
        # The dictionary's .items() method is used, which gives (key, value) pairs.
        # The 'key=lambda item: item[1]' tells the max() function to compare based on the value (item[1])
        # rather than the key (item[0]).
        dominant_emotion_name = max(emotion_dictionary.items(), key=lambda item: item[1])[0]

        # Add the dominant_emotion to the dictionary
        emotion_dictionary['dominant_emotion'] = dominant_emotion_name
    
    # If the response status code is 400, set same dictionary, but all values to None
    elif response.status_code == 400:
        # Construct the output dictionary
        emotion_dictionary = {
            'anger': 'None',
            'disgust': 'None',
            'fear': 'None',
            'joy': 'None',
            'sadness': 'None'
        }

    # Return the customized emotion dictionary
    return emotion_dictionary
