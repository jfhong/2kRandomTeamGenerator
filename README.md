# 2kRandomTeamGenerator
Python script to randomize teams since 2k's randomizing is a little iffy. This generator only works for the CURRENT teams in 2K19. This does not cover classic teams or the WNBA.

INSTRUCTIONS ON HOW TO RUN CODE

IF YOU DON'T HAVE PYTON INSTALLED PLEASE FOLLOW STEPS 1 - 7.

IF YOU DO HAVE PYTHON INSTALLED, SKIP TO STEP 8.



All steps 1 - 7 does is install Homebrew to install Python3 on your unix machine.

1. Open Terminal. If you don't know how to do this click 'cmd + spacebar', it should prompt you with a spotlight search. At this point type in 'Terminal'.

2. In terminal copy and paste this and hit enter.

	 /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

3. If you're doing this on a fresh Mac, it'll prompt you by asking to install Apple's 'command line developer tools'. To continue with installation just confirm the dialog box by clicking 'install'.

4. You'll most likely hit 'Enter' to continue the Homebrew installation.

5. Homebrew will ask you to enter your password so it can finalize the installation. Enter the password you use to log into your mac and hit 'Enter'. Depending on your internet connection, it'll take a few minutes to download the required files. Once installed it'll go back to your normal command line prompt window. At this point Homebrew is installed on your system.

6. When it's at your normal command line prompt copy and paste this into your command line and hit 'Enter'. 

	 brew install python3

7. It should've installed python3 on your machine at this point and if you wanted to test it you can type 'pip3' into your command line and hit 'Enter'. You should see python's "Pip" pacakage manager (basically help commands for python, you don't have to worry about this, we just wanted to check if python is installed). If nothing pops up or you get an error just go back to step 6 and try again.

8. Now since you have the files, you're going to need to find the file through command line. 'cd' and 'ls' help to move around and show what files are where. If you need help with this you should google it as I don't know where your files get downloaded.

9. Once you've found the files on your computer, make sure you're in the folder and not the file itself. Copy and paste this into command line and hit 'Enter' and it should execute and give you the team you're playing with. Do this as many times as you so wish.

	 python 2kRandomTeamGenerator.py