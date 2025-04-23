from flask import Flask, request, jsonify, render_template
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

# Disable OneDNN optimization if causing issues
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

app = Flask(__name__)

# Load the model
model = load_model(r"D:\Projects\DL Projects\Happy & Sad Prediction\image_classification_model.h5", compile=False)

# Define image classes
classes = ['Sad', 'Happy']  # Binary classification: 0 = Sad, 1 = Happy

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'})
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
        
    # Create uploads directory if it doesn't exist
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
        
    # Save the uploaded file
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)
        
    try:
        # Preprocess the image - IMPORTANT: use 256x256 to match model input
        img = image.load_img(file_path, target_size=(256, 256))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = img_array / 255.0  # Normalize to match training
        
        # Make prediction
        prediction = model.predict(img_array)[0][0]  # Get the raw sigmoid output (0-1)
        
        # For binary classification with sigmoid, the output is a probability between 0 and 1
        # where values closer to 1 indicate the positive class (Happy)
        happy_prob = float(prediction)
        sad_prob = float(1 - prediction)
        
        # Determine the predicted class
        predicted_class = 'Happy' if happy_prob >= 0.5 else 'Sad'
        
        # Format probabilities as percentages
        happy_percentage = int(happy_prob * 100)
        sad_percentage = int(sad_prob * 100)
        
        # Get image dimensions
        img_width, img_height = img.size
        resolution = f"{img_width} x {img_height}"
        
        # Clean up the uploaded file
        os.remove(file_path)
        
        return jsonify({
            'prediction': predicted_class,
            'confidence': happy_percentage if predicted_class == 'Happy' else sad_percentage,
            'happy_percentage': happy_percentage,
            'sad_percentage': sad_percentage,
            'resolution': resolution
        })
        
    except Exception as e:
        if os.path.exists(file_path):
            os.remove(file_path)
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    # Create an 'uploads' folder if not exists
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)

