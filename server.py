''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using emotion_detection()
        function. The output returned shows the labels and its confidence 
        scores for the provided text.
    '''
    # Retrieve the text to analyse from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the emotions scores from response
    anger_score = response.get('anger')
    disgust_score = response.get('disgust')
    fear_score = response.get('fear')
    joy_score = response.get('joy')
    sadness_score = response.get('sadness')
    dominant_emotion_name = response.get('dominant_emotion')

    # Check if the anger_score is None, indicating an error or invalid input
    if anger_score == 'None':
        return "Invalid text! Please try again!"

    # Return a formatted string with the emotion labels and scores
    return f"""For the given statement, the system response is
        'anger': {anger_score},
        'disgust': {disgust_score},
        'fear': {fear_score},
        'joy': {joy_score}
        and 'sadness': {sadness_score}. 
        The dominant emotion is {dominant_emotion_name}."""

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
