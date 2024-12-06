from openai import OpenAI

#This program takes the file made using the training-file-creator and uploads it to openai for verification, conversion, and use.

client = OpenAI(api_key="")

client.files.create(
  file=open("file-training.jsonl", "rb"),
  purpose="fine-tune"
)