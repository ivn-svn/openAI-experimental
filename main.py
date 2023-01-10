import os
import apikey 
import openai

openai.api_key = apikey.apikey_var



response = openai.Completion.create(engine="davinci", prompt="Hello, my name is Bob. I am a software developer, and I love to write code. What about you?", temperature=0.5)

# Print the generated text
print(response.text)
