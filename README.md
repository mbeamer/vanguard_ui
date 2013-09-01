vanguard_scripts
================

Scripts to augment interactions with Vanguard MMO

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
