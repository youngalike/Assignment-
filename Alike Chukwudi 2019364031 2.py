import speech_recognition as sr
from time import sleep


def take():
    r = sr.Recognizer()

    # Filename/path is your audio file
    audioFile = sr.AudioFile("c:/Users/chudd/Documents/harvard.wav") 
    with audioFile as source:
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
        print("Dectecting speech...")
        sleep(3)
        print("Transcribing...")
        

    try:
        query = r.recognize_google(audio, language='en-Us')
        sleep(0.5)
        print("\n")
        print(query)
        

    except Exception as e:
        print("An error occured. Please check your internet connection")

        return "None"

    return query

query = take()
sleep(1)
print("* Transcribed Successfully , Quitting the program now *")
sleep(2)
