"""
A Flask web application for emotion detection.

This application provides endpoints for analyzing text and determining
the associated emotions using the EmotionDetection module.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize Flask application
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emo_detector():
    """
    Endpoint to analyze text and detect emotions.

    Query Parameters:
        textToAnalyze (str): The text to analyze for emotions.

    Returns:
        str: A response string with emotion scores and the dominant emotion,
             or an error message for invalid input.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze:
        return "No text provided! Please include textToAnalyze query parameter."

    response = emotion_detector(text_to_analyze)

    anger = response.get('anger', 0)
    disgust = response.get('disgust', 0)
    fear = response.get('fear', 0)
    joy = response.get('joy', 0)
    sadness = response.get('sadness', 0)
    dominant_emotion = response.get('dominant_emotion')

    if not dominant_emotion:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy}, and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Render the index HTML page.

    Returns:
        str: The rendered HTML template for the index page.
    """
    return render_template('index.html')


if __name__ == "__main__":
    # Run the application on the default host and port
    app.run(host="0.0.0.0", port=5000)
