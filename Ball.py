from .. import loader, utils
from telethon.tl.types import Message
import random


@loader.tds
class TrySampMod(loader.Module):
    strings = {"name": "TrySamp"}

    async def trycmd(self, message: Message):
        tryrandom = random.choice(["Всё возможно", "Да", "Определённо", "Точно нет."])
        args = utils.get_args_raw(message)
        await utils.answer(
            message, f"<b>{tryrandom} | {args}</b>" if args else f"<b>{tryrandom}</b>"
        )