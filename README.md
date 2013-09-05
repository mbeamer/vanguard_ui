vanguard_scripts
================

Scripts to augment interactions with Vanguard MMO

Cloning:

This project is best situated in the Vanguard directory.  Since GIT won't let you clone into an existing folder, this makes getting started a bit tricky.

Follow these instructions (found here https://gist.github.com/davisford/5039064)

cd Vanguard
$ git init
$ git remote add origin git@github.com:yourname/foo.git
$ git fetch
$ git branch master origin/master
$ git checkout master

Dependencies:

The guild_members script requires BeautifulSoup.  I've used 4.3.1, it can be found at http://www.crummy.com/software/BeautifulSoup/.

Usage:

The process is this:
In Vanguard we set ourselves to log, log our inventory, and stop logging (since it doesn't write until you terminate) -

    /log
    /inventory (or /bankdisplay)
    /log

From command line we process into a yuku friendly format -
(Get the latest python and inventory_markup.py (or use bank_markup.py) (save it, don't run it))

    d:\Vanguard> python inventory_markup.py 
    Enter the log name: d:\Vanguard\logs\Chat_log_2013_0825_1854.txt
    Enter the log markup name (d:\Vanguard\logs\Chat_log_2013_0825_1854.txt.yuku)
    Logging to: d:\Vanguard\logs\Chat_log_2013_0825_1854.txt.yuku

You will now have a file which is ready to be posted to the forums. 
