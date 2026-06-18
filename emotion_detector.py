from deepface import DeepFace

def detect_emotion(frame):

    try:

        result = DeepFace.analyze(
            img_path=frame,
            actions=['emotion'],
            enforce_detection=False,
            detector_backend='opencv'
        )

        if isinstance(result, list):
            emotion = result[0]['dominant_emotion']
        else:
            emotion = result['dominant_emotion']

        return emotion

    except Exception as e:
        print(e)
        return "neutral"