# Database
This directory is where Gladiator Bot saves and interact with persistent storage.  Storage is saved in a sqlite3 database and database.py is the primary interface to it.

## Database Structure
The database contains the following data:

- Channels
  - Channel : text (snowflake)
  - Type : text (match | admin | all)
- Roles
  - Name : text (snowflake | name)
  - Rank : text (banned, user, mod, admin, owner)
- Users
  - User : text (snowflake)
  - Name : text
  - Join : text (datetime)
  - Rank : text (banned, user, mod, admin, owner)
  - Points : int
  - Win : int
  - Loss : int
  - Draw : int
- Match
  - Start : text (datetime)
  - Attacker : text (snowflake)
  - Defender : text (snowflake)
- Match History
  - Start : text (datetime)
  - Attacker : text (snowflake)
  - Defender : text (snowflake)
  - End : text (datetime)
  - Winner: text (snowflake)
  - Points: int
- Log
  - User : text (snowflake)
  - Name : text (name)
  - Command : text (command)
  - Ok : bool
