# APPLICATION ID
# 1146475132668354610

# PUBLIC KEY
# 76d5e99ad596f1f04c162c186ddc0f74e2e995cf9511b1ca319adaf43650d212

import discord
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")
# 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

token = os.environ['SECRET']
token = "MTE0NjQ3NTEzMjY2ODM1NDYxMA.Gyrq6P.5kgr_hFYuqfX7txMFTQ8wPyu3EwgZkIM1pJssE"

chat = ""


class MyClient(discord.Client):

  async def on_ready(self):
    print(f'Logged on as {self.user}!')

  async def on_message(self, message):
    global chat
    chat += f"{message.author}: {message.content} \n"
    print(f'Message from {message.author}: {message.content}')
    if self.user != message.author:
      if self.user in message.mentions:
        channel = message.channel
        try:
          response = openai.Completion.create(model="text-davinci-003",
                                              prompt=f"{chat} \nATIII-GPT: ",
                                              temperature=1,
                                              max_tokens=256,
                                              top_p=1,
                                              frequency_penalty=0,
                                              presence_penalty=0)
          messageToSend = response.choice[0].text
        except openai.error.RateLimitError as e:
          messageToSend = "Rate limit exceeded. Please check your plan and billing details. And then try again"
        except Exception as e:
          print("An error occurred:", str(e))
        await channel.send(messageToSend)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)
