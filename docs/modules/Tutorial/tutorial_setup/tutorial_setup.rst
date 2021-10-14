.. _metplus_tutorial_setup:

METplus Tutorial Setup
======================

Session 1 Video 1: Find and Navigate the Tutorial
-------------------------------------------------

UPDATE URL WHEN VIDEO HAS BEEN UPLOADED!

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/KCISG0phmbw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 4.0**.

Preparation:
^^^^^^^^^^^^

* Slides: metplus_online_tutorial_session_1_setup.pptx (note formatting of
  PowerPoint presentation differs between PowerPoint and Google Drive!
  Please use PowerPoint if available or copy file and adjust formatting)
* Open a web browser

Description (add to YouTube video)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

METplus 4.0 Online Tutorial
Session 1 : Setup
Video 1: Find and Navigate the Tutorial

The content in this video corresponds to this online tutorial section: https://dtcenter.org/metplus-practical-session-guide-version-4-0/session-1-metplus-setupgrid-grid/metplus-setup

Next Video:
If using a pre-configured environment such as Hera or Cheyenne: ***ADD URL FOR Session 1 Video 2a***
OR
If using your own workstation: ***ADD URL FOR Session 1 Video 2b***

Questions? Visit the METplus GitHub Discussions Form:
https://github.com/dtcenter/METplus/discussions

METplus DTC Webpage:
https://dtcenter.org/community-code/metplus

METplus User’s Guide:
https://metplus.readthedocs.io/en/latest/Users_Guide

Script
^^^^^^

(show slide 1 - title)

Welcome to the “Find and Navigate the Tutorial” video, part of the “Session 1: Setup” portion of the METplus 4.0 Online Tutorial.

(show slide 2 - Topics Covered in This Video)

This video covers how to get started with the METplus 4.0 online tutorial, including where to find the tutorial pages and how to get started.

(open a web browser and navigate to https://dtcenter.org/metplus-practical-session-guide-version-4-0/session-1-metplus-setupgrid-grid/metplus-setup)

The content in this video corresponds to the online tutorial section titled “METplus Setup” which is found in “Session 1: METplus Setup / Grid-to-Grid.”

To find the METplus online tutorial, navigate to dtcenter.org

(navigate to https://dtcenter.org)

then select “METplus” under the “Community Code” drop down menu.

(mouse over “Community Code” and click on “METplus”)

Next click on “User Support.”

(mouse over the “User Support” button on the menu on the right side of the window,
Reduce the width of the window so that the menu bar disappears from the right side)

You may not see the menu bar on the right-hand side of the window. This occurs when the width of the window is not large enough to display it. If this is the case, navigate to the bottom of the page to find this menu.

(navigate to bottom of page and mouse over the “User Support” menu button)

You can also adjust the width or zoom of your browser window until it appears on the right-hand side.

(demonstrate that increasing the window width and reducing the zoom percentage causes the menu to appear on the right side)

Next click on the “Tutorial - Online” button.

(Click on “Tutorial - Online”)

Finally, click on the link for the “METplus v4.0” tutorial. Previous versions of the online tutorial can also be found here in PDF format.

(navigate to https://dtcenter.org/metplus-practical-session-guide-version-4-0/session-1-metplus-setupgrid-grid)

The first page of the online tutorial describes the format of the instructions.

(scroll to the “Tutorial Format” section of the page)

Text blocks inside dark gray boxes with bold, white text can be copied from the browser and pasted into the command line terminal.
Text blocks inside yellow boxes contain important information or hints.
Text blocks inside light blue boxes contain instructions for the user to perform.
Text blocks inside light gray boxes contain sample output from a command or contents of a file.

(scroll to the “Tutorial Tips” section of the page)
Please note that some of the commands listed in the tutorial instructions use specific applications like vi to open and edit files and okular to view PDF, postscript, and image files. Users are encouraged to use their preferred tools instead of these suggested tools if they are more comfortable with them.

Also please note that if you are running the tutorial instructions inside a Docker container, then the visualization tools used in the tutorial may not be available inside the container. To run these commands, you will have to mount the output directory inside Docker to your local file system and run those tools from there.

(navigate to the bottom of the page and mouse over the line that states “Click the ‘METplus Setup >’ link below to get started!”)

And here is the first instruction of the tutorial telling us to click this link that will take us to the next page of the tutorial.

(click link)

This next page contains a brief overview of the METplus wrappers and a list of links to useful resources such as the user’s guide and the GitHub pages for the various METplus components.

(navigate to next page -- METplus: Initial setup)

This page describes the prerequisites for running the tutorial instructions. It is assumed that you have already installed METplus, including the MET executables and the METplus wrapper scripts, and that you have obtained the sample input data needed to run the exercises.

If you are going through the tutorial on a machine that has been pre-configured to run the tutorial, such as Hera or Cheyenne, then these steps have already been completed for you. If you are going through the tutorial on your own workstation, then you will need to perform the installation steps yourself. If you have not already done so, you can refer to installation videos or the user’s guide.

***provide link to relevant tutorial videos and user’s guide pages
METplus Training: Compiling MET - https://www.youtube.com/watch?v=tqyYVFh6vlc
METplus Training: Installing METplus - https://www.youtube.com/watch?v=ap9-Fdlb7Fo ***

(scroll down to the Pre-Configured Environments and User Configued Environments sections)

Click on the appropriate link to navigate to the instructions that are specific to the environment you are using.

For all environments, the instructions include steps to determine a working area for the tutorial, create a directory that will contain your configuration and output files, and copy a few files into the directory.

If running on your own workstation, we provide instructions for using bash and c-shell. We recommend using bash if you do not have a preference.

(show slide 3 - links)

***add clickable links for next video and useful URLs from description***

The next video in this tutorial depends on the environment you are using. If you are running the tutorial on a pre-configured environment such as Hera or Cheyenne, watch the Setup Pre-Configured Environment video next. If you are running the tutorial on your own computer, watch the Setup User Workstation Environment video next.

If you have any questions, please visit the METplus GitHub Discussions Forum. On this page you can check if your question has already been asked by another user or create a new discussion topic.

Other useful resources, such as User’s Guide and Contributor’s Guide, can be found on the Developmental Testbed Center webpage.

All of the links can also be found in the description of this video.

Thank you for watching!

Session 1 Video 2: Set Up Pre-Configured Environment
----------------------------------------------------

UPDATE URL WHEN VIDEO HAS BEEN UPLOADED!

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/KCISG0phmbw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 4.0**.

Preparation:
^^^^^^^^^^^^

* Slides: metplus_online_tutorial_session_1_setup.pptx (note formatting
  of PowerPoint presentation differs between PowerPoint and Google Drive!
  Please use PowerPoint if available or copy file and adjust formatting)
* Open a web browser
* Open a terminal on a pre-configured machine such as Hera or Cheyenne and set
  the PS1 environment variable to something that hides the user and machine
  names, i.e. export PS1="$~"

Description (add to YouTube video)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

METplus 4.0 Online Tutorial
Session 1 : Setup
Video 2a: Set Up Pre-Configured Environment

The content in this video corresponds to this online tutorial section: https://dtcenter.org/metplus-practical-session-guide-version-4-0/session-1-metplus-setupgrid-grid/metplus-setup/metplus-initial-setup

Next Video:
***ADD URL FOR Session 1 Video 3***

Questions? Visit the METplus GitHub Discussions Form:
https://github.com/dtcenter/METplus/discussions

METplus DTC Webpage:
https://dtcenter.org/community-code/metplus

METplus User’s Guide:
https://metplus.readthedocs.io/en/latest/Users_Guide

Script
^^^^^^

(show slide 4 - title)

Welcome to the “Set Up Pre-Configured Environment” video, part of the “Session 1: Setup” portion of the METplus 4.0 Online Tutorial.

(show slide 5 - Topics Covered in This Video)

***Add clickable link to “Set Up User Workstation Environment” video***

This video covers how to set up the tutorial if you are running in a pre-configured environment such as Hera or Cheyenne. If you are running on your own computer, then please watch the “Set Up User Workstation Environment” video instead.

(open a web browser and navigate to https://dtcenter.org/metplus-practical-session-guide-version-4-0/session-1-metplus-setupgrid-grid/metplus-setup/metplus-initial-setup)

The content in this video corresponds to the online tutorial section titled “METplus: Initial Setup” which is found in the “METplus Setup” portion of “Session 1: METplus Setup / Grid-to-Grid.”

(navigate to Pre-Configured Environments / User Configured Environments headers)

I will go through the instructions for setting up the tutorial on Hera. The instructions for the other pre-configured environments are very similar.

(navigate to Hera instructions: https://dtcenter.org/metplus-practical-session-guide-version-4-0/session-1-metplus-setupgrid-grid/metplus-setup/metplus-initial-setup/setting-tutorial-environment-hera)

(open terminal on Hera on left side of screen, shift the browser window to the right side of the screen)

Open a shell and follow the instructions. Be sure to read each instruction carefully.

(run through the instructions to create a directory and cd in the directory)

Navigate to a directory where you have write permissions. Next create a directory called METplus dash 4.0.0 underscore tutorial. This directory will contain all of your tutorial work including configuration files, output data, and any other notes you’d like to keep. Change directory into this directory. You can run the “pwd” command to see which directory you are currently in if it is not displayed in the shell.  Next create the user_config and output directories.

Tutorial files are copied from a local directory. This command also renames the files so that the subsequent tutorial instructions will be identical regardless of the environment used.

The tutorial setup script runs any module commands, if applicable, and sets environment variables that are referenced throughout the tutorial. Simply source this file each time you return to the tutorial instructions and you will be ready to run.

At the end of each environment specific page is a link to the page titled “Verify Environment is Set Correctly.”

(show slide 6 - links)

***add clickable links for next video and useful links in description***

The next video in this tutorial is titled “Verify Environment is Set Correctly.” This is an important next step to ensure that all of the instructions in this video were completed correctly.

If you have any questions, please visit the METplus GitHub Discussions Forum. On this page you can check if your question has already been asked by another user or create a new discussion topic.

Other useful resources, such as the User’s Guide and Contributor’s Guide, can be found on the Developmental Testbed Center webpage.

All of the links can also be found in the description of this video.

Thank you for watching!


Session 1 Video 2b: Set Up User Workstation Environment
-------------------------------------------------------

UPDATE URL WHEN VIDEO HAS BEEN UPLOADED!

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/KCISG0phmbw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 4.0**.

Preparation:
^^^^^^^^^^^^

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


Session 1 Video 3: Verify Environment is Set Correctly
------------------------------------------------------

UPDATE URL WHEN VIDEO HAS BEEN UPLOADED!

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/KCISG0phmbw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 4.0**.

Preparation:
^^^^^^^^^^^^

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
Video 3: Verify Environment is Set Correctly

The content in this video corresponds to this online tutorial section:
https://dtcenter.org/metplus-practical-session-guide-version-4-0/session-1-metplus-setupgrid-grid/metplus-setup/verify-environment-set-correctly

Next Video:
***ADD URL FOR ?***

Questions? Visit the METplus GitHub Discussions Form:
https://github.com/dtcenter/METplus/discussions

METplus DTC Webpage:
https://dtcenter.org/community-code/metplus

METplus User’s Guide:
https://metplus.readthedocs.io/en/latest/Users_Guide

Script
^^^^^^

(show slide 10 - title)

Welcome to the “Verify Environment is Set Correctly” video, part of the “Session 1: Setup” portion of the METplus 4.0 Online Tutorial.

(show slide 11 - Topics Covered in This Video)

***Add clickable links to “Set Up Pre-Configured Environment” and
“Set up User Workstation Environment” videos***

This video covers how to check that the tutorial environment has been set up correctly.
This video assumes you have already completed the steps covered in the “Set Up Pre-Configured Environment” video OR the “Set up User Workstation Environment” video. If you have not yet completed this step, please navigate to the appropriate video before proceeding with this video.

(navigate to https://dtcenter.org/metplus-practical-session-guide-version-4-0/session-1-metplus-setupgrid-grid/metplus-setup/verify-environment-set-correctly)

To verify that the tutorial environment was set up correctly, this page instructs you to source the setup script and run commands to ensure that everything was done correctly.

The results from these commands may vary slightly based on your environment, but should be similar.

For pre-configured environments, as long as your copy of the setup scripts are found in your personal working directory, you should get the correct results.

If you configured your own workstation to run the tutorial and the output looks very different, you may need to update the tutorial setup script with the correct values.

Start by navigating to your METplus-4.0.0_Tutorial directory and source the setup script.

(run cd and source commands)

We will first check that the paths are set correctly.

(run copy/pastable instructions and describe what you are seeing)

If everything looks as expected, then you are ready to continue to the next page of the METplus online tutorial!
