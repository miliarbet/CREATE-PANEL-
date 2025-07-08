from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Buat bot-nya
bot = ChatBot("AsistenDhilzz")

# Latih bot
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")  # bisa juga 'indonesia' kalau ada corpusnya

# Chat
while True:
    try:
        user_input = input("Lo: ")
        response = bot.get_response(user_input)
        print("AI: ", response)
    except (KeyboardInterrupt, EOFError):
        break
