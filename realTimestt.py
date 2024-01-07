# Author: Mohammad Arman - Github: Armancollab
# Date: 2024-01-07
# Version: 1.0.0
# Description: A program that converts speech to text in real time using Google Speech Recognition API


import speech_recognition as sr
import os

text_outputs = []
recognizer = sr.Recognizer()


def listen_microphone(timeout=5):
    with sr.Microphone() as source:
        lanCode = input("Enter your language code (default: en-US): ")
        if lanCode == "":
            lanCode = "en-US"

        print("Say something...")
        # Adjust for ambient noise = reduce noise
        recognizer.adjust_for_ambient_noise(source)
        while True:
            # Listen for speech until the user says "stop"
            audio = recognizer.listen(source, timeout=timeout)
            try:
                text = recognizer.recognize_google(audio, language=lanCode)
                print(f"Text: {text}")
                if text.lower() == "stop":
                    print("Stopping...")
                    break
                text_outputs.append(text)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")


def menu():
    os.system("cls")
    print("Real Time Speech to Text\n")
    print("1. Start Program")
    print("2. See the list of language codes")
    print("3. Exit Program")

    while True:
        choice = input("\nEnter your choice: ")
        if choice == "1":
            print("Initializing...")
            listen_microphone()

        elif choice == "2":
            print("en-US: English (United States)\nfa-IR: Persian (Iran)\nfr-FR: French (France)\nja-JP: Japanese (Japan)\nko-KR: Korean (South Korea)\nzh-CN: Chinese (China)\nzh-HK: Chinese (Hong Kong)\nzh-TW: Chinese (Taiwan)\nCheck the complete list here: https://cloud.google.com/speech-to-text/docs/languages")

        elif choice == "3":
            saveFile = input(
                "Before exiting, would you like to save the current session? (y/n): ")
            if saveFile.lower() == "y":
                fileName = input("Enter the file name (.txt): ")
                with open(fileName, "w") as file:
                    file.write("\n".join(text_outputs))
                print("File saved")
            else:
                print("File was not saved\nExiting...")
            exit()

        else:
            print("Invalid input")


if __name__ == "__main__":
    menu()
