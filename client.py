from openai import OpenAI

#client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="sk-proj-nGNtFnC3W96PQYbSRl1fT3BlbkFJIlofUlFnAAflosVENNoC",
 )

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant name siri in general tasks like alexk and google cloud"},
    {"role": "user", "content": "what is coding."}
  ]
)

print(completion.choices[0].message)