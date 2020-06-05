import db
import cfg
import discord
from discord.ext import commands
import elo

db.init('database/test.db')
cfg = cfg.init('config.toml')

bot = commands.Bot(
    case_insensitive=True,
    command_prefix=cfg['bot']['prefix'],
    description=cfg['bot']['description'],
    owner_id=cfg['bot']['description']
)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} - {bot.user.id}')
    return

bot.run(cfg['bot']['token'], bot=True, reconnect=True)