from openai import OpenAI

client = OpenAI(api_key='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')
qq = input("me: ")
response = client.chat.completions.create(
  model="gpt-3",
  prompt=qq,
  temperature=0.7,
  max_tokens=64,
  top_p=1
)