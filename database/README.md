# Database
This directory is where Gladiator Bot saves and interact with persistent storage.  Storage is saved in a sqlite3 database and database.py is the primary interface to it.

## Database Requirements
The database contains the following data:

- Channels
  - Channel : text (snowflake)
  - Type : text (match | admin | all)
- Roles
  - Role : text (snowflake | name)
  - Rank : text (banned, user, mod, admin)
- Users
  - User : text (snowflake)
  - Name : text (username)
  -  
- Match
- Match History