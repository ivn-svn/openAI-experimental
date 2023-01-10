import apikey 
import openai
import json
import speech_recognition as sr


openai.api_key = apikey.apikey_var
response = openai.Completion.create(engine="davinci", prompt="Hello, my name is Bob. I am a software developer, and I love to write code. What about you?", temperature=0.5)


class OpenAIObject:
    def __init__(self, value):
        self.value = value

def openai_object_handler(obj):
    if isinstance(obj, OpenAIObject):
        return {"value": obj.value}
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")


obj = OpenAIObject("Hello, World!")

json_string = json.dumps(obj, default=openai_object_handler)
# Parse JSON into an object with attributes corresponding to dict keys.
# Print the generated text
print("JSON STRING")
print(json_string)
loaded_json = json.loads(json_string)
print(response)
response = json.dumps(response, default=openai_object_handler)

loaded_json1 = json.loads(response)

print(loaded_json["value"])
print(loaded_json1["choices"][0]["text"])


r = sr.Recognizer()
with sr.Microphone() as source:
  while True:
    try:
      print("Say something!")
      audio = r.listen(source)

      text = r.recognize_google(audio)
      print(text)
      response = openai.Completion.create(engine="davinci", prompt=text, temperature=0.5)
      response = json.dumps(response, default=openai_object_handler)
      loaded_json2 = json.loads(response)

      print(loaded_json2["choices"][0]["text"])
    except:
      pass