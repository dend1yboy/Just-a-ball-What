from .. import loader, utils
from telethon.tl.types import Message
import random


@loader.tds
class BallByDend1y(loader.Module):
    strings = {"name": "Ball by dend1y"}

    async def trycmd(self, message: Message):
        tryrandom = random.choice(["Всё возможно", "Да", "Определённо", "Точно нет."])
        args = utils.get_args_raw(message)
        await utils.answer(
            message, f"<b>{tryrandom} | {args}</b>" if args else f"<b>{tryrandom}</b>"
        )
