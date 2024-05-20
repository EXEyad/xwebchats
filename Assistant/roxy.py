from openai import OpenAI

client = OpenAI(api_key='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')

# Initialize OpenAI API key

def generate_code(prompt):
    response = client.completions.create(engine="davinci-codex", prompt=prompt, max_tokens=150, n=1, stop=None, temperature=0.5)
    return response.choices[0].text.strip()


while True:
    command = input('Ask Me: ')
    if command:
        if "exit" in command.lower():
            print("Goodbye!")
            break
        elif "code" in command.lower():
            print("What would you like me to code?")
            code_prompt = input()
            if code_prompt:
                print("Generating code...")
                code = generate_code(code_prompt)
                print(f"Generated code:\n{code}")
                print("\n\nHere is the code.")
            else:
                print("I didn't get that. Please try again.")
        else:
            print("I can only help with coding tasks right now. Please ask me to generate code.")