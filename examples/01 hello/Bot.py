from samt import Bot

bot = Bot()


@bot.answer("Hello")
@bot.answer("/start")
@bot.answer("Hallo")
def start():
    return "Hello, new user, how can I help you?"


if __name__ == "__main__":
    bot.listen()
