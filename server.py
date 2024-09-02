''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    
    response = emotion_detector(text_to_analyze)

   
    return f"""For the given statement, the system response is 'anger' : {response['anger']}, 
    'disgust': {response['disgust']},
    'fear': {response['fear']},
    'joy': {response['joy']}, 
    'sadness': {response['sadness']}. 
    The dominant emotion is <b>{response['dominant_emotion']}</b>"""


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

