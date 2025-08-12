# 🎭 Real-Time Facial Emotion Detection

![Emotion Detection Demo](https://via.placeholder.com/640x360.png?text=Emotion+Detection+Demo)

---

## 🚀 Project Overview

This project performs **real-time facial emotion recognition** using your webcam. It leverages a pre-trained **TensorFlow/Keras** model (`facialemotionmodel.h5`) alongside **OpenCV** for video capture and face detection to classify emotions in real-time.

---

## ✨ Features

- 🎥 Real-time emotion detection from webcam video feed  
- 😠 Supports 7 emotions: Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral  
- 📊 Displays confidence scores for predictions  
- ⚡ GPU acceleration support for faster inference (if available)  
- 🐍 Easy-to-run Python script with minimal setup  

---

## 📁 Project Structure

```
emotion_detection/
├── facialemotionmodel.h5       # Pre-trained emotion recognition model
├── emotion_detection.py        # Main Python script
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## 🎯 Requirements

- Python 3.8 or higher  
- Functional webcam  
- The `facialemotionmodel.h5` model file (included or downloaded separately)  

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/emotion_detection.git
cd emotion_detection
```

2. (Optional) Create and activate a virtual environment:

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the main script to start detecting emotions in real-time:

```bash
python emotion_detection.py
```

- Press **`Q`** at any time to quit the webcam window.

---

## 😊 Supported Emotions

| Emotion  | Icon  |
|----------|-------|
| Angry    | 😠    |
| Disgust  | 🤢    |
| Fear     | 😨    |
| Happy    | 😄    |
| Sad      | 😢    |
| Surprise | 😲    |
| Neutral  | 😐    |

---

## ⚠️ Troubleshooting

| Issue                      | Solution                                                                 |
|----------------------------|--------------------------------------------------------------------------|
| Model not loading?          | Verify the `MODEL_PATH` in `emotion_detection.py` points to `facialemotionmodel.h5`. |
| Webcam not opening?         | Change `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)` or other indices. |
| TensorFlow warnings/errors? | Usually harmless; ensure compatible TensorFlow and Python versions.     |

---

## 📜 License

This project is intended for **educational purposes only**.

---

## 📸 Example Output

![Emotion Detection Screenshot](https://via.placeholder.com/640x360.png?text=Live+Emotion+Detection)

---

Thanks for checking out the project! Feel free to contribute or raise issues.
