import os
import time

with open("./gui/emoticon_faces/smile.txt", "r") as file:
    smile = file.read()

with open("./gui/emoticon_faces/blink.txt", "r") as file:
    blink = file.read()

with open("./gui/emoticon_faces/music.txt", "r") as file:
    music = file.read()

with open("./gui/emoticon_faces/sleep.txt", "r") as file:
    sleeping = file.read()

with open("./gui/emoticon_faces/tardis.txt", "r") as file:
    tardis = file.read()

with open("./gui/emoticon_faces/thinking.txt", "r") as file:
    thinking = file.read()

def display_face(face):
    os.system("clear")
    for line in face.splitlines():
        print(line)

if __name__ == "__main__":
    total_faces = [smile, blink, music, sleeping, tardis, thinking]
    for face in total_faces:
        display_face(face)
        time.sleep(3)