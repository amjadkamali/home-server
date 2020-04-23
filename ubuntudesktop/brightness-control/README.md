# brightness.py

Having been using laptops primarily for the majority of my life, I'm used to being able to compusilvly change my screen brightness without menu diving on monitors- and with a dual screen setup it's just weird. Although my initial goal was to get the built in gnome slider to work with my external monitors, this is a pretty cool compromise.

This is a python script that gets called by argos, a gnome extension that lets you add status icons and menus to gnome using bash or python! Very cool. 

To get it up and running:

1. Install argos from [here](https://extensions.gnome.org/extension/1176/argos/) or the Ubuntu Software Center 

2. Install ddcutil
`apt install ddcutil`

3. You'll want to play around with i2c permissions to get your user to issue these commands without requiring sudo. Read into that [here](https://www.ddcutil.com/i2c_permissions/)

4. Copy `brightness.py` to `~/.config/argos/`

5. Get one of your screen's serial numbers by running `ddcutil detect` and set "monitorSN" in the script. This is used to read the current brightness and since both monitors have the same setting, we only need to read one.

That should be it!

