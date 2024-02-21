# Does not work in multiplayer. Only singleplayer

This is a Barony checkpoint script coded in python. This does not require any modded version of the game, and can be used across all versions unless they change savefile contents. 

# How it works

The script will keep all savefile contents in memory and once one gets deleted IE all players die in a game, you keep the savefile. However, I noticed this does not work in multiplayer as all players need their own savefile version of the save and must match host's savegame. This led me to creating a modified version of Barony in which this is prevented (Prevents host from telling clients to delete the savefile). This can be found here: https://github.com/Sat727/Barony-Checkpoint.


# How to setup

In the "Config" File, you will see a variable named "path" this is the path to your ROOT folder of the game. From there, the script will do the rest of the work. Happy gaming!
