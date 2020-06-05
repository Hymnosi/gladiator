# Gladiator Bot
Gladiator Bot is a discord 1v1 matchmaking system that implements an ELO rating for each registered user.  It utilizes an sqlite database as a backend to maintain record of matches and outcomes thereof.  Logging is done in separate from the database to maintain database stability in the event of catastrophic failure.

## Configuration
Configuration is done via config.ini.  The configuration can be updated while running by sending `!reload` to the bot via direct message.  


## Commands
