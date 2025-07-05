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

    # Check if the list exists and is not empty
    if emotion_predictions and len(emotion_predictions) > 0:
        # Access the first item in the 'emotionPredictions' list
        first_prediction = emotion_predictions[0]

        # Access the 'emotion' dictionary within that item
        target_emotion_scores = first_prediction.get('emotion')

        # Now, extract the individual scores (if needed) or use the dictionary directly
        anger_score = target_emotion_scores.get('anger')
        disgust_score = target_emotion_scores.get('disgust')
        fear_score = target_emotion_scores.get('fear')
        joy_score = target_emotion_scores.get('joy')
        sadness_score = target_emotion_scores.get('sadness')

        # Construct the output dictionary
        output_dictionary = {
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
        dominant_emotion_name = max(output_dictionary.items(), key=lambda item: item[1])[0]

        # Add the dominant_emotion to the dictionary
        output_dictionary['dominant_emotion'] = dominant_emotion_name

        # Return the customized output dictionary
        return output_dictionary
    else:
        return {'Error': 'Could not find emotionPredictions or it was empty in the source dictionary.'}

    
