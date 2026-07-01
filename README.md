<div align="center">

# 🚗 SafeDrive AI
### Real-Time Driver Drowsiness & Distraction Detection System

![Python](https://img.shields.io/badge/Python-3.11-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Face_Mesh-orange)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object_Detection-red)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-success)

---

### Intelligent Driver Monitoring System using Computer Vision and Artificial Intelligence

**Developed by**

# 👩‍💻 Reshma Basha

</div>

---

# 📌 Overview

SafeDrive AI is a real-time Driver Monitoring System (DMS) that uses Artificial Intelligence and Computer Vision to detect driver fatigue and distracted driving.

The system continuously monitors the driver's face using a webcam or dashcam and analyzes multiple behavioural indicators such as:

- 👁 Eye Closure
- 😴 Drowsiness
- 😮 Yawning
- 📱 Mobile Phone Usage
- 🧠 Driver Attention Level
- 🚗 Head Movement

When risky behaviour is detected, the system calculates a risk score, generates an alert, and records the event.

---

# 🎯 Objectives

- Reduce accidents caused by drowsy driving
- Detect distracted driving
- Monitor driver attention in real-time
- Provide alerts before dangerous situations occur
- Generate driving event logs

---

# ✨ Features

## 👁 Driver Monitoring

- Eye Detection
- Blink Detection
- Eye Aspect Ratio (EAR)
- Eye Closure Detection

---

## 😴 Fatigue Detection

- Yawning Detection
- Mouth Aspect Ratio (MAR)
- Continuous Eye Closure Monitoring
- Driver Drowsiness Detection

---

## 📱 Mobile Phone Detection

- YOLOv8 Object Detection
- Cell Phone Detection
- Confidence Score
- Real-time Bounding Box

---

## 🎯 Head Pose Estimation

- Looking Left
- Looking Right
- Looking Up
- Looking Down
- Forward Detection

---

## 🧠 AI Risk Engine

The system calculates an intelligent Driver Risk Score using multiple AI models.

Risk factors include

- Eye Closure
- Yawning
- Phone Usage
- Head Position

---

## 🚨 Alert System

- Alarm Trigger
- Driver Warning
- Console Alerts
- Event Logging

---

## 📊 Dashboard

Displays

- FPS
- Attention Score
- Eye Status
- EAR
- MAR
- Blink Count
- Yawn Count
- Phone Detection
- Confidence
- Driver Status
- Risk Meter
- Session Timer

---

# 🏗 System Architecture

```
                 Webcam
                    │
                    ▼
             OpenCV Camera
                    │
                    ▼
          MediaPipe Face Mesh
                    │
    ┌───────────────┼───────────────┐
    │               │               │
    ▼               ▼               ▼
 Blink        Yawn Detection   Head Pose
 Detection
                    │
                    ▼
          YOLOv8 Phone Detector
                    │
                    ▼
             AI Risk Engine
                    │
      ┌─────────────┴─────────────┐
      │                           │
      ▼                           ▼
 Alarm System               CSV Logger
                    │
                    ▼
              UI Dashboard
```

---

# 📂 Project Structure

```
SafeDrive-AI

│── app.py
│── config.py
│── requirements.txt
│── README.md

├── core
│   ├── camera.py
│   └── vision_engine.py

├── detectors
│   ├── eye_detector.py
│   ├── blink_detector.py
│   ├── yawn_detector.py
│   ├── head_pose.py
│   └── phone_detector.py

├── engine
│   ├── alarm.py
│   ├── logger.py
│   ├── risk_engine.py
│   └── ui_engine.py

├── assets
├── models
├── dashboard
├── data
└── logs
```

---

# 🛠 Technologies Used

- Python 3.11
- OpenCV
- MediaPipe
- YOLOv8
- NumPy
- Ultralytics

---

# 💻 Installation Guide

## Windows

### Step 1

Install Python 3.11

https://www.python.org/downloads/

---

### Step 2

Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/SafeDrive-AI.git

cd SafeDrive-AI
```

---

### Step 3

Create Virtual Environment

```bash
python -m venv venv
```

---

### Step 4

Activate Environment

```bash
venv\Scripts\activate
```

---

### Step 5

Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 6

Run Application

```bash
python app.py
```

---

# 🐧 Linux Installation

Supported

- Ubuntu
- Kali Linux
- Parrot OS
- Debian

---

## Step 1

Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/SafeDrive-AI.git

cd SafeDrive-AI
```

---

## Step 2

Create Virtual Environment

```bash
python3 -m venv venv
```

---

## Step 3

Activate Environment

```bash
source venv/bin/activate
```

---

## Step 4

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 5

Run Application

```bash
python app.py
```

---

# 📱 How to Use

1. Launch the application.

2. Allow webcam access.

3. Sit in front of the camera.

4. The dashboard will display:

- Eye Status
- Blink Count
- Head Position
- Yawning
- Phone Detection
- Attention Score

5. When dangerous behaviour is detected

- Alarm triggers
- Driver status changes
- Event is logged

---

# 📊 Dashboard Information

| Feature | Description |
|----------|-------------|
| FPS | Camera Speed |
| EAR | Eye Aspect Ratio |
| MAR | Mouth Aspect Ratio |
| Eyes | Open / Closed |
| Blink Count | Number of Blinks |
| Yawn Count | Number of Yawns |
| Head Pose | Driver Direction |
| Phone | Mobile Detection |
| Confidence | Detection Confidence |
| Risk | Driver Risk Percentage |
| Attention | Driver Attention Score |
| Session | Running Time |

---

# 📁 Event Logs

Detected events are stored automatically.

```
logs/events.csv
```

Example

```
Timestamp,Risk Score,Driver Status,Reason

2026-07-01 10:21:42,75,DROWSY,Phone Usage

2026-07-01 10:24:53,65,WARNING,Looking Down

2026-07-01 10:28:31,80,DROWSY,Eyes Closed
```

---

# 🚀 Future Improvements

- Face Recognition
- Driver Identification
- Seatbelt Detection
- Smoking Detection
- Emotion Recognition
- Night Vision Support
- Cloud Dashboard
- Mobile Application
- Raspberry Pi Deployment

---

# 📸 Screenshots

Add screenshots here

```
screenshots/dashboard.png

screenshots/phone_detection.png

screenshots/drowsiness.png
```

---

# 🤝 Contributing

Contributions are welcome.

Fork the repository and create a pull request.

---

# 📜 License

This project is developed for educational and research purposes.

---

# 👩‍💻 Author

## **Reshma Basha**

Artificial Intelligence & Data Science Student

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: https://linkedin.com/in/YOUR_PROFILE

---

# ⭐ Support

If you found this project useful,

Please ⭐ Star the repository.

---

<div align="center">

## 🚗 Drive Safe • Stay Alert • Save Lives

Made with ❤️ using Artificial Intelligence

</div>
