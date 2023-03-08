import os
import openai
import config 
openai.api_key = config.OPENAI_API_KEY

def openAIQuery(query):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=query,
        temperature=0.7,
        max_tokens=214,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0)
    if "choices" in response:
        if len (response["choices"]) > 0:
            answer = response["choices"][0]["text"]
        else:
            answer = "No answer found"
    else:
        answer = "No answer found"
    return answer
query = "Apple Iphone 12"
openAIQuery(query)