# 🖐️ AI Gesture-Based Virtual Mouse

A real-time computer vision application that allows users to control their mouse using hand gestures via webcam.

Built using OpenCV, MediaPipe, and PyAutoGUI.

---

## 🚀 Features

- 🖱️ Move cursor using index finger
- 🤏 Pinch gesture (thumb + index) for click & drag
- ✌️ Index + middle finger gesture for scrolling
- Real-time hand tracking
- Smooth cursor movement

---

## 🧠 Technologies Used

- Python
- OpenCV
- MediaPipe
- PyAutoGUI

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-gesture-mouse-control.git
cd ai-gesture-mouse-control
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python main.py
```

Press **ESC** to exit.

---

## 📋 Requirements

Create a `requirements.txt` file with:

```
opencv-python
mediapipe
pyautogui
```

---

## 🧩 How It Works

- MediaPipe detects 21 hand landmarks.
- Index finger controls cursor position.
- Pinch distance triggers click events.
- Gesture distance triggers scrolling.
- PyAutoGUI maps hand coordinates to screen coordinates.

---

## ⚡ Future Improvements

- Gesture smoothing with Kalman Filter
- Adjustable sensitivity
- Multi-hand support
- Custom gesture mapping
- GUI settings panel



## 📌 Author

Raj Y. Kangralkar  
AI Engineer | Computer Vision Enthusiast
