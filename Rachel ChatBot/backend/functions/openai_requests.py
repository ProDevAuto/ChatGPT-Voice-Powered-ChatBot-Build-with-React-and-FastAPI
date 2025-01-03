import openai
from openai import OpenAI

client = OpenAI(api_key=config("OPEN_AI_KEY"))
from decouple import config

from functions.database import get_recent_messages


# Retrieve Enviornment Variables
# TODO: The 'openai.organization' option isn't read in the client API. You will need to pass it when you instantiate the client, e.g. 'OpenAI(organization=config("OPEN_AI_ORG"))'
# openai.organization = config("OPEN_AI_ORG")


# Open AI - Whisper
# Convert audio to text
def convert_audio_to_text(audio_file):
    try:
        transcript = client.audio.transcribe("whisper-1", audio_file)
        message_text = transcript.text
        return message_text
    except Exception as e:
        print(f"Error during audio transcription: {e}")
        return None


# Open AI - Chat GPT
# Convert audio to text
def get_chat_response(message_input):

  messages = get_recent_messages()
  user_message = {"role": "user", "content": message_input + " Only say two or 3 words in Spanish if speaking in Spanish. The remaining words should be in English"}
  messages.append(user_message)
  print(messages)

  try:
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=messages)
    message_text = response.choices[0].message.content
    return message_text
  except Exception as e:
    print(e)
    return
