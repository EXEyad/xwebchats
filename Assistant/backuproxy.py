import speech_recognition as sr
import pyttsx3
from openai import OpenAI

client = OpenAI(api_key='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')

# Initialize OpenAI API key

def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        print("Sorry, my speech service is down.")
        return None

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def generate_code(prompt):
    response = client.completions.create(engine="davinci-codex",
    prompt=prompt,
    max_tokens=150,
    n=1,
    stop=None,
    temperature=0.5)
    return response.choices[0].text.strip()

def main():
    while True:
        command = listen()
        if command:
            if "exit" in command.lower():
                speak("Goodbye!")
                break
            elif "code" in command.lower():
                speak("What would you like me to code?")
                code_prompt = listen()
                if code_prompt:
                    speak("Generating code...")
                    code = generate_code(code_prompt)
                    print(f"Generated code:\n{code}")
                    speak("Here is the code.")
                else:
                    speak("I didn't get that. Please try again.")
            else:
                speak("I can only help with coding tasks right now. Please ask me to generate code.")

if __name__ == "__main__":
    main()
