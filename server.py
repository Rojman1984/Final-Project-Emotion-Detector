"""
Emotion Detection App Server

This script defines a Flask-based server for performing emotion detection on user-provided text.
It uses a single function from the EmotionDetection package to get scores and the dominant emotion.

Author: [RolandoOrtiz]
"""

from flask import Flask, render_template, request

# We only need to import the single, powerful emotion_detector function
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Analyze the user-provided text for emotions and return a result string.
    """
    # 1. Get the text from the URL query parameter 'textToAnalyze'
    text_to_analyze = request.args.get('textToAnalyze')

    # 2. Add a check for empty input for better error handling
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please provide some text to analyze."

    # 3. Call the emotion_detector function ONCE. It does all the work.
    response = emotion_detector(text_to_analyze)

    # 4. Check if the function returned a valid response or an error state (None)
    if response is None or response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!"

    # 5. Format the successful response string
    return (
        f"For the given statement, the system response is 'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is <strong>{response['dominant_emotion']}</strong>."
    )

@app.route("/")
def render_index_page():
    """ 
    This function initiates the render of the main application page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Standard way to run a Flask app
    app.run(host="0.0.0.0", port=5000)
    