Session 1 Video 2b: Set Up User Workstation Environment
-------------------------------------------------------

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/9EP59dp8Xp0" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 4.0**.

Preparation
^^^^^^^^^^^

* Slides: metplus_online_tutorial_session_1_setup.pptx (note formatting
  of PowerPoint presentation differs between PowerPoint and Google Drive!
  Please use PowerPoint if available or copy file and adjust formatting)
* Open a web browser
* Open a terminal on your own machine and set
  the PS1 environment variable to something that hides the user and machine
  names, i.e. export PS1="$~"

Description (add to YouTube video)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

METplus 4.0 Online Tutorial
Session 1 : Setup
Video 2b: Set Up User Workstation Environment

The content in this video corresponds to this online tutorial section: https://dtcenter.org/metplus-practical-session-guide-version-4-0/session-1-metplus-setupgrid-grid/metplus-setup/metplus-initial-setup

Next Video:
***ADD URL FOR Session 1 Video 3***

Other Relevant Videos:
Compiling MET - https://www.youtube.com/watch?v=tqyYVFh6vlc
Installing METplus - https://www.youtube.com/watch?v=ap9-Fdlb7Fo

Questions? Visit the METplus GitHub Discussions Form:
https://github.com/dtcenter/METplus/discussions

METplus DTC Webpage:
https://dtcenter.org/community-code/metplus

METplus User’s Guide:
https://metplus.readthedocs.io/en/latest/Users_Guide

Script
^^^^^^

(show slide 7 - title)

Welcome to the “Set Up User Workstation Environment” video, part of the “Session 1: Setup” portion of the METplus 4.0 Online Tutorial.

(show slide 8 - Topics Covered in This Video)

***add link to “Set Up Pre-Configured Environment” video***

This video covers how to set up the tutorial if you are running on your own computer. If you are running in a pre-configured environment such as Hera or Cheyenne, then please watch the “Set Up Pre-Configured Environment” video instead.

(open a web browser and navigate to https://dtcenter.org/metplus-practical-session-guide-version-4-0/session-1-metplus-setupgrid-grid/metplus-setup/metplus-initial-setup)

The content in this video corresponds to the online tutorial section titled “Initial Setup” which is found in the “METplus Setup” portion of “Session 1: METplus Setup / Grid-to-Grid.”

(navigate to Pre-Configured Environments / User Configured Environments headers)

I will go through the instructions for setting up the tutorial using bash. The instructions for using c-shell are very similar. We recommend using bash if you do not have a shell preference.

(click on the link to navigate to bash instructions: https://dtcenter.org/metplus-practical-session-guide-version-4-0/session-1-metplus-setupgrid-grid/metplus-setup/metplus-initial-setup/setting-tutorial-environment-bash)

(open a shell, set the PS1 environment variable to something that hides the user and machine names, i.e. export PS1="$~")

Open a shell and follow the instructions. Be sure to read each instruction carefully. For example, this important info block tells you to change the value of slash path slash to before running the command.

(run through the instructions to create a directory and cd in the directory)

Navigate to a directory where you have write permissions. Next create a directory called METplus dash 4.0.0 underscore tutorial. This directory will contain all of your tutorial work including configuration files, output data, and any other notes you’d like to keep. Change directory into this directory. You can run the “pwd” command to see which directory you are currently in if it is not displayed in the shell.  Next create the user_config and output directories.
The tutorial setup files are downloaded from the DTC webpage using wget commands.

(copy wget commands and paste into terminal)

Notice that the file is renamed in the wget command to METplus-4.0.0_TutorialSetup.sh. This is done so that no matter which set of instructions are followed, the subsequent tutorial commands will be identical.

The user configured environment instructions require an additional step of modifying the tutorial setup script after it has been obtained to set values that correspond to the local environment.

(open the tutorial setup script in an editor)

Any variable that references “slash path slash to” must be modified to include the correct path.

(change values for METPLUS_BUILD_BASE, MET_BUILD_BASE, and METPLUS_DATA to the correct locations on your machine)

If you are unsure what values to set for these variables, the next page in the tutorial entitled “Verify Environment is Set Correctly” provides examples of what should be found inside these directories.

(open or print contents of tutorial.conf file)

The environment variables in the setup script are referenced in the tutorial.conf METplus configuration file.

The tutorial setup script runs any module commands, if applicable, and sets environment variables that are referenced throughout the tutorial. Simply source this file each time you return to the tutorial instructions and you will be ready to run.

(navigate back to the bash instructions in the web browser and scroll to bottom of the page)

At the end of each environment specific page is a link to the page titled “Verify Environment is Set Correctly.”

(show slide 6 - links)

***add clickable links for next video and useful links in description***

The next video in this tutorial is titled “Verify Environment is Set Correctly.” This is an important next step to ensure that all of the instructions in this video were completed correctly.

If you have any questions, please visit the METplus GitHub Discussions Forum. On this page you can check if your question has already been asked by another user or create a new discussion topic.

Other useful resources, such as User’s Guide and Contributor’s Guide, can be found on the Developmental Testbed Center webpage.

All of the links can also be found in the description of this video.

Thank you for watching!
