import asyncio

from samt import Bot, Answer, Context, Mode

marv = Bot()


@marv.default_answer
def default():
    return 'unknown', Context.get('message').text


@marv.answer("/start")
async def start():
    return Answer('greeting', Context.get('user'))


@marv.answer("Guten Tag")
def guten_tag():
    a = Answer('greeting', Context.get('user'))
    a.language_feature = False
    return a


if __name__ == "__main__":
    marv.listen()
