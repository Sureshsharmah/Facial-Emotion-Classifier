# Facial-Emotion-Classifier

A deep learning web application that classifies facial expressions as Happy or Sad using TensorFlow and Flask.

![Demo](demo.gif) <!-- Replace with actual demo gif if available -->

## Features ✨

- 🖼️ Upload images for instant emotion classification
- 🎯 Accurate binary classification (Happy/Sad)
- 📊 Displays prediction confidence percentages
- 🚀 Lightweight Flask backend with TensorFlow model
- 🔍 Shows image resolution information

## Tech Stack 💻

- **Backend**: Python, Flask
- **Deep Learning**: TensorFlow, Keras
- **Frontend**: HTML, CSS, JavaScript
- **Image Processing**: Keras Image Preprocessing

## Installation & Setup ⚙️

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/happy-sad-classifier.git
   cd happy-sad-classifier
Create a virtual environment

bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies

bash
pip install -r requirements.txt
Run the application

bash
python app.py
Access the app
Open your browser and visit http://localhost:5000

Project Structure 📂
happy-sad-classifier/
├── static/            # CSS, JS, and other static files
├── templates/         # HTML templates
│   └── index.html
├── uploads/           # Temporary upload directory
├── app.py             # Flask application
├── requirements.txt   # Dependencies
└── README.md
Model Details 🤖
Architecture: Custom CNN

Input Size: 256x256 pixels

Output: Binary classification (Happy/Sad)

Accuracy: [Your model accuracy]% on test set

Usage Guide 📝
Click "Choose File" to select an image

The image should clearly show a face

Click "Predict" to get the classification

View results including:

Predicted emotion

Confidence percentage

Image resolution

Contributing 🤝
Contributions are welcome! Please open an issue or submit a pull request.

License 📜
This project is licensed under the MIT License - see the LICENSE file for details.

Screenshots 📸
Homepage <!-- Replace with actual screenshot -->
Result <!-- Replace with actual screenshot -->


### Additional Recommendations:

1. Create a `requirements.txt` file with:
flask
tensorflow
numpy
pillow


2. Add a `.gitignore` file with:
venv/
pycache/
uploads/
*.pyc
.DS_Store

