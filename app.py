import cv2
import mediapipe as mp
import time
from collections import Counter

from emotion_detector import detect_emotion
from spotify_player import play_song

mp_face = mp.solutions.face_detection
face_detection = mp_face.FaceDetection()

cap = cv2.VideoCapture(0)

last_emotion    = ""
song_end_time   = 0        # When the current song finishes
song_playing    = False    # Is a song currently playing?

BUFFER_SIZE = 20
emotion_buffer  = []

while True:

    success, frame = cap.read()
    if not success:
        break

    frame     = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_detection.process(rgb_frame)

    current_time = time.time()

    # ---- Check if current song has finished ----
    if song_playing and current_time >= song_end_time:
        print("Song finished. Resetting buffer for next detection.")
        song_playing   = False
        last_emotion   = ""       # Allow same emotion to re-trigger
        emotion_buffer = []       # Fresh buffer after song ends

    # ---- Only detect emotion when no song is playing ----
    if not song_playing:
        emotion = detect_emotion(frame)

        emotion_buffer.append(emotion)
        if len(emotion_buffer) > BUFFER_SIZE:
            emotion_buffer.pop(0)

        stable_emotion = Counter(emotion_buffer).most_common(1)[0][0]

        status_text = f"Detecting: {stable_emotion}"

        # Trigger song once buffer is full and emotion changed
        if len(emotion_buffer) == BUFFER_SIZE and stable_emotion != last_emotion:
            duration_sec = play_song(stable_emotion)
            last_emotion  = stable_emotion
            song_end_time = current_time + duration_sec
            song_playing  = True
            emotion_buffer = []   # Reset buffer after triggering

    else:
        stable_emotion = last_emotion
        remaining      = int(song_end_time - current_time)
        status_text    = f"Playing [{stable_emotion}] - {remaining}s left"

    # ---- Display status on frame ----
    cv2.putText(
        frame,
        status_text,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.9,
        (0, 255, 0),
        2
    )

    cv2.imshow("AI Mood Spotify Player", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()