# Trials-Rising-Steam-Deck-Patch
Disabling Easy Anti-Cheat in trialsrising.exe so that the game works on Linux + Steam Deck

**Updated 2025-07-10**: This patcher now works differently. 
### Easy method:
Download the latest release from the releases tab, and run it on your Steam Deck. It will patch the game for you. If you've previously patched the game, go to the game's properties in Steam > Installed Files > Verify Integrity of Game Files to restore the original file, then run this patcher.

### Run from source:
via the command line on your Steam Deck/Linux machine:
```git clone https://github.com/kylemohr/Trials-Rising-Steam-Deck-Patch.git
cd Trials-Rising-Steam-Deck-Patch
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python patcher.py
```

if this fails at the `pip install` step, you may need to install `python3-pip` via `pacman`. This will likely require you to run `sudo steamos-devmode enable` first, then `sudo pacman -Syu python3-pip`. **You don't need to do this if you're using the easy method above.**

### I highly recommend using GE-Proton-9-1 for this game
You can find instructions for how to do this [here](https://www.rockpapershotgun.com/how-to-install-proton-ge-on-the-steam-deck)

I tried a ton of different flavors and versions of Proton, and lots of them crash, some of them are capped at 30fps, and the controller doesn't work on others. GE-Proton-9-1 had none of these issues.

If you're struggling to reach 60fps consistently, go to the Trials video settings > advanced> anti-aliasing use CMAA, then go back one menu, and set resolution scaling to .5 or .75.

[See here for more details on how this patch works](https://www.kylemohr.com/Trials-Rising-EasyAntiCheat-Bypass-Analysis)

All credit for finding this method goes to the user ['Cade-H'](https://pcgamingwiki.com/w/index.php?title=Trials_Rising&diff=prev&oldid=1519149) for posting this method on the [Trials Rising PCGamingWiki Entry](https://www.pcgamingwiki.com/wiki/Trials_Rising#Disable_Easy_Anti-Cheat)
