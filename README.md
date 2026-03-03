# Trials-Rising-Steam-Deck-Patch
Disabling Easy Anti-Cheat in trialsrising.exe so that the game works on Linux + Steam Deck


## Usage:
Run this script on the Linux device that Trials: Rising is installed on with:

`python3 patch.py`

If the patcher says it couldn't find the file, you can specify the path to `trialsrising.exe` as a command line argument, like so:

`python3 patch.py /path/to/trialsrising.exe`


---

**Updated 2026-03-03**: Simplified and improved the process! It should now work for both Steam and Uplay versions of the game.

The patching process no longer relies on checksums, so it should continue to work even if the game is updated. 

Fun fact: as a byproduct of disabling EasyAntiCheat, this patch allows you to play the game on macOS! I use [Crossover](https://www.codeweavers.com/crossover), but other Wine-based solutions should work as well. 

### I highly recommend using GE-Proton-9-1 for this game if you're on Steam Deck
You can find instructions for how to do this [here](https://www.rockpapershotgun.com/how-to-install-proton-ge-on-the-steam-deck)

I tried a ton of different flavors and versions of Proton, and lots of them crash, some of them are capped at 30fps, and the controller doesn't work on others. GE-Proton-9-1 had none of these issues.

If you're struggling to reach 60fps consistently, go to the Trials video settings > advanced> anti-aliasing use CMAA, then go back one menu, and set resolution scaling to .5 or .75.

[See here for more details on how this patch works](https://www.kylemohr.com/Trials-Rising-EasyAntiCheat-Bypass-Analysis)

All credit for finding this method goes to the user ['Cade-H'](https://pcgamingwiki.com/w/index.php?title=Trials_Rising&diff=prev&oldid=1519149) for posting this method on the [Trials Rising PCGamingWiki Entry](https://www.pcgamingwiki.com/wiki/Trials_Rising#Disable_Easy_Anti-Cheat)
