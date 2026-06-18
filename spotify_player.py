import webbrowser
import random

happy_songs = [
    "https://open.spotify.com/track/4uLU6hMCjMI75M1A2tKUQC",
    "https://open.spotify.com/track/1HNkqx9Ahdgi1Ixy2xkKkL"
]

sad_songs = [
    "https://open.spotify.com/track/7qEHsqek33rTcFNT9PFqLf",
    "https://open.spotify.com/track/0VjIjW4GlUZAMYd2vXMi3b"
]

angry_songs = [
    "https://open.spotify.com/track/6habFhsOp2NvshLv26DqMb"
]

neutral_songs = [
    "https://open.spotify.com/track/3AJwUDP919kvQ9QcozQPxg"
]


def play_song(emotion):

    if emotion == "happy":
        song = random.choice(happy_songs)

    elif emotion == "sad":
        song = random.choice(sad_songs)

    elif emotion == "angry":
        song = random.choice(angry_songs)

    else:
        song = random.choice(neutral_songs)

    print(f"Opening Spotify Song for {emotion}")

    webbrowser.open(song)