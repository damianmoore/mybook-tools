# WD MyBook Live Tools

A clean version of Debian can be installed on the Western Digital MyBook Live. This is my collection of utilities to bring back some features that were in the original distribution and add some too.

The steps I followed to install Debian are here: https://www.schwabenlan.de/en/blog/2015/04/06/clean-debian-install-on-mybook-live-nas

## Scripts
 - **monitorio.py** - Sets the LED to the default green colour causing it to flash when drive being accessed. Spins down the drive into low power mode after a period of inactivity and sets the LED to blue. When the drive is accessed again the drive spins up and the LED goes green. This should be run in the background via system init.
