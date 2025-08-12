import cv2
import numpy as np
import tensorflow as tf
import sys
import io
import time

# Ensure UTF-8 encoding for console output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ====== CONFIG ======
MODEL_PATH = r"C:\Users\rohan\OneDrive\Desktop\Collage projects 🤡\emotion recognization\facialemotionmodel.h5"
EMOTION_LABELS = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
FACE_PROTO = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
# ====================

# ====== GPU CONFIG ======
physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    try:
        tf.config.experimental.set_memory_growth(physical_devices[0], True)
        print("✅ GPU detected & memory growth set.")
    except Exception as e:
        print(f"⚠️ GPU memory growth setting failed: {e}")

# ====== LOAD MODEL ======
try:
    model = tf.keras.models.load_model(MODEL_PATH)
    print("✅ Emotion model loaded successfully.")
except Exception as e:
    print(f"❌ Failed to load model: {e}")
    sys.exit(1)

# ====== LOAD FACE DETECTOR ======
face_detector = cv2.CascadeClassifier(FACE_PROTO)

# ====== FUNCTIONS ======
def preprocess_face(face_img):
    """Resize, normalize and reshape the face image for the model."""
    resized_face = cv2.resize(face_img, (48, 48))
    normalized_face = resized_face / 255.0
    return np.reshape(normalized_face, (1, 48, 48, 1))

def predict_emotion(face_img):
    """Predict emotion from the preprocessed face image."""
    preds = model.predict(face_img, verbose=0)
    max_idx = np.argmax(preds[0])
    confidence = preds[0][max_idx]
    return EMOTION_LABELS[max_idx], confidence

# ====== MAIN LOOP ======
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)

if not cap.isOpened():
    print("❌ Cannot open webcam.")
    sys.exit(1)

print("🎥 Press 'Q' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to read frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        preprocessed = preprocess_face(face_roi)
        emotion, conf = predict_emotion(preprocessed)

        # Draw bounding box
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # Label with emotion + confidence
        cv2.putText(frame, f"{emotion} ({conf*100:.1f}%)",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.9, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("Modern Emotion Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
