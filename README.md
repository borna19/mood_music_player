# 🎵 Mood Music Player

## Project Overview

The Mood Music Player is an AI-powered application that detects the user's mood using facial expression recognition and automatically recommends songs that match the detected emotion. The system uses a webcam to capture facial expressions, analyzes them using OpenCV and MediaPipe, and fetches music recommendations through the Spotify API.

This project is built using Python, OpenCV, MediaPipe, Flask, HTML, CSS, Bootstrap, and Spotify API.

---

## Features

- Real-Time Face Detection
- Mood Detection Using Facial Expressions
- Automatic Music Recommendations
- Spotify API Integration
- Mood-Based Playlist Suggestions
- User-Friendly Interface
- Responsive Design
- Live Webcam Support

---

## Technologies Used

- Python
- Flask
- OpenCV
- MediaPipe
- Spotify API
- HTML5
- CSS3
- Bootstrap 5

---

## Project Structure

Mood-Music-Player/

├── static/

│ ├── css/

│ ├── js/

│ └── images/

├── templates/

│ ├── index.html

│ ├── result.html

│ └── playlist.html

├── model/

│ └── mood_detection.py

├── app.py

├── spotify_config.py

├── requirements.txt

└── README.md

---

## Installation Steps

### 1. Clone the Repository

git clone https://github.com/borna19/mood_music_player.git

cd mood-music-player

### 2. Create a Virtual Environment

python -m venv venv

### 3. Activate the Virtual Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate

### 4. Install Required Packages

pip install -r requirements.txt

### 5. Install Dependencies

pip install flask

pip install opencv-python

pip install mediapipe

pip install spotipy

### 6. Create Spotify Developer Account

1. Visit Spotify for Developers.
2. Create a new application.
3. Copy the Client ID and Client Secret.
4. Configure the Redirect URI.

### 7. Configure Spotify API Credentials

Create a file named `spotify_config.py` and add:

```python
SPOTIFY_CLIENT_ID = "your_client_id"
SPOTIFY_CLIENT_SECRET = "your_client_secret"
REDIRECT_URI = "http://localhost:5000/callback"
```

### 8. Run the Application

```bash
python app.py
```

### 9. Open Browser

```text
http://127.0.0.1:5000
```

---

## Working Process

1. User opens the application.
2. Webcam captures the user's face.
3. OpenCV detects facial features.
4. MediaPipe analyzes facial landmarks.
5. The system predicts the user's mood.
6. Spotify API fetches songs related to the detected mood.
7. Recommended songs and playlists are displayed.

---

## Supported Moods

- Happy 😊
- Sad 😔
- Angry 😠
- Neutral 😐
- Surprised 😲
- Relaxed 😌

---

## Future Enhancements

- Deep Learning-Based Emotion Detection
- Personalized Playlist Generation
- Multiple User Profiles
- Voice Emotion Recognition
- Real-Time Music Playback
- Song Like/Dislike Feature
- Mood History Tracking
- Mobile Application Support

---

## Author

Developed by: Barnali Bhowmik

---

## License

This project is created for educational and learning purposes. Feel free to modify and improve it as needed.

⭐ If you find this project useful, please give it a star.
