vanguard_scripts
================

UI Modifications for Vanguard: Saga of Heroes

Cloning:

This project is best situated in the Vanguard directory.  Since GIT won't let you clone into an existing folder, this makes getting started a bit tricky.

Follow these instructions (found here https://gist.github.com/davisford/5039064)

cd Vanguard
$ git init
$ git remote add origin git@github.com:yourname/foo.git
$ git fetch
$ git branch master origin/master
$ git checkout master

Usage:

The contents of this repository constitute custom UI elements for Vanguard.  To use these elements, you must update your bin\VGClient.ini:

[UI]
ShellName=MOD
