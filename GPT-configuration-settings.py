from openai import OpenAI

#The following code is what will be used to start integrating our current prompt and settings into our flask application.

client = OpenAI(api_key="")

response = client.chat.completions.create(
  model="ft:gpt-4o-mini-2024-07-18:personal::ADXHfnAj",
  messages=[
    {
      "role": "system",
      "content": [
        {
          "text": "You are a helpful assistant that assists with everything Python (coding) and only python. You were designed to help the Computer Science Students of Morgan State University help debug, create code, and become better coders.",
          "type": "text"
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=2048,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  response_format={
    "type": "text"
  }
)