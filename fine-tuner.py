from openai import OpenAI

#Using an API from OpenAI, this program will take the training_file which resulted from the training-file-uploader.py and that was uploaded to openai's platform and use it to start a fine tuning job for our chat-based GPT.

client = OpenAI(api_key="")

client.fine_tuning.jobs.create(
  training_file="file-zUx9vnPDEkub9x7ABiZ5MwnG", 
  model="gpt-4o-mini-2024-07-18"
)