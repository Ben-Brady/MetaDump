import os
import json
from pathlib import Path

import discord
from discord.ext import commands, tasks
from ffprobe import FFProbe
from PIL import Image
from PIL.ExifTags import TAGS


class Cog(commands.Cog):
    def __init__(self, bot, channel) -> None:
        self.bot = bot
        self.channel = channel

    def in_right_channel(self):
        def predicate(ctx: commands.Context):
            return ctx.channel.id == self.channel
        return commands.check(predicate)

    @commands.Cog.listener()
    async def on_message(self, msg: discord.message):
        if not msg.attachments:
            return

        Attach: discord.Attachment = msg.attachments[0]

        _, fType = os.path.splitext(Attach.filename)
        FileLocation = f"./Store/{msg.id}.{fType}"

        with open(FileLocation, 'wb') as fObj:
            fObj.write(await Attach.read())
        try:
            if Attach.content_type.startswith('video'):
                Meta = FFProbe(FileLocation).metadata
                Meta = json.dumps(Meta, sort_keys=True, indent=4)
                await msg.reply(Meta)

            elif Attach.content_type.startswith('image'):
                Meta = ""
                exifdata = Image.open(FileLocation).getexif()
                for id in exifdata:
                    tag_name = TAGS.get(id, id)
                    data = exifdata.get(id)

                    if isinstance(data, bytes):
                        data = data.decode()

                    Meta += f"{tag_name:25} : {data}\n"
                if Meta == "":
                    Meta = "No Data"
                await msg.reply(Meta)

        finally:
            os.remove(FileLocation)
