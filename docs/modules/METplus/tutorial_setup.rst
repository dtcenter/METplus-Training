.. _metplus_tutorial_setup:

METplus Tutorial Setup
======================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/KCISG0phmbw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 3.1**.

*Preparation:*

* *Have a terminal with the editor opened with TutorialSetup.linux-csh.sh and have it ready.*
* *Have another terminal ready, in the directory inside the METplus tutorial directory.*
* *Have a browser tab with the link to https://ncar.github.io/METplus/Users_Guide/Installation.html*

(*Introduction*)

Welcome.  This video describes how to set up your computer’s environment for running the METplus tutorial. The information covered in this video corresponds to the METplus practical session on METplus setup (*Mouse over the top of the page METPLUS:INITIAL SETUP*).

Before we begin, it is important that you have both MET and METplus already installed on your computer.  The installation of MET is outside the scope of this tutorial.  You can find the code tarball and release notes at this link at the bottom of the page, under the Information: MET And METplus Source Code section at the bottom of this page.
(*scroll down to the bottom of the page, to the Information: MET And METplus Source Code section and click on the ‘here’ hyperlink*)  

The MET source tarball downloads when you click on this green box (*Mouse over the met-<version>.tar.gz box*)  The latest version of MET will always be available at this location. The corresponding latest version of the other METplus components will also be available by clicking on the appropriate green box. (*Mouse over the METplus and METviewer boxes*)

If you haven’t installed METplus on your computer, please view the video on installing and setting up METplus [NOTE: indicate the appropriate section and video*).  Alternatively, you can follow the instructions available in the Github repository, at https://github.com/NCAR/METplus/releases (*Go to the web browser tab you created, highlight the navbar and then show the section*) The latest available version is always located at the top of the page. To get the source code, expand the Assets link and click on the zip or tar’d gzipped version of the source.(*Scroll down to Assets, expand the link and mouse over the zip and tar.gz links*)

or you can click on this link provided in the tutorial (*Go back to the tutorial page, scroll down to the bold text METPLUS_BUILD_BASE and mouse over the link under ‘NOTE’*) and follow the instructions on that page.


We will need to create a directory to store all the METplus tutorial material. 
Begin by changing directories to the location where you wish to store your tutorial files and create a directory named METplus_Tutorial. These two code boxes show the commands you’ll need to accomplish this.  In this first command example, remember to replace /path/to with the appropriate path. (*Mouse over the first and second code box*)  Change directory to the METplus_Tutorial directory you just created and determine the full path by running ‘pwd’ at the command line.  Set the value returned by the ‘pwd’ command to the METPLUS_TUTORIAL_DIR environment variable.  If you are running in a bash shell, enter this command, which uses the export command (*Mouse over the 4th code box*).  If you are running within a c-shell, enter this command, which uses the setenv command(*Mouse over the 5th code box*) 

Now you will need to obtain two useful files, a shell script and a configuration file.  On your command line, enter the following four commands for bash (*Highlight with mouse the “On your machine (bash)” code box*), and for csh, enter these four commands (*Highlight with mouse the “On your machine (csh)” code box*).  If you are installing the tutorial material on your own computer, follow the instructions that have ‘On linux server’ over the code boxes (*Mouse to the ‘On linux server’ code box*).  There are also instructions for the host ‘hera’, of which you would need an account to access. These instructions are indicated by ‘On hera’ above the code box. (*Mouse to the ‘On hera’ code box*)  You will follow the instructions for installing and setting up on your computer.

The first file you downloaded, TutorialSetup.linux-csh.sh, is the shell script which contains the paths to the environment variables METPLUS_TUTORIAL_DIR, METPLUS_BUILD_BASE, MET_BUILD_BASE, and METPLUS_DATA.  In the editor of your choice, open the TutorialSetup.linux-csh.sh script.  In your shell script, make sure you replace any occurrence of ‘path/to’ with the appropriate path, as you see from this reminder at the top of the script. (*Mouse over this reminder at the top of the shell script*)

The **METPLUS_TUTORIAL_DIR** is the environment variable that indicates where all your tutorial files will reside.  
The **MET_BUILD_BASE** is the environment variable that indicates where MET is installed.  
The **METPLUS_BUILD_BASE** is the environment variable that indicates where METplus is installed.  
Finally, the **METPLUS_DATA** environment variable indicates where sample input data for the tutorial is located.

Save, then close your TutorialSetup.linux-csh.sh file when you have finished setting the paths to these environment variables. (*Close the TutorialSetup.linux-csh.sh script but keep the terminal open*)

Source the TutorialSetup.linux.sh file by entering this command at the command line for the bash version of the script (*Under “4. Source the environment…” mouse over the code box under “On linux server (bash)”*), and for the csh version of the TutorialSetup script, use this command (*Mouse over the code box under “On linux server (csh)*)

Verify that you’ve successfully set the environment variables by entering ‘env’ from the command line (*Enter ‘env’ in the terminal you have available*)  You can scroll the output and find the environment variables you set earlier.  Now enter ‘which master_metplus.py’ (*Enter this command in the terminal that is in the METplus tutorial directory*)
You should see that the master_metplus.py script is located in the METplus tutorial directory you set in the TutorialSetup script. 


The other file you downloaded, the tutorial.conf file is used later in the tutorial. It utilizes the environment variables you just set to run the METplus wrappers in the tutorial. (*Go to the terminal and open the tutorial.conf file and highlight the {ENV[]} sections*)
 
Finally,  we need to retrieve the data for this tutorial.  
If you are installing the tutorial on your own computer, you will need to retrieve data tarballs that are found on the GitHub repository, at https://github.com/NCAR/METplus/releases
(*Highlight the nav bar in your browser with the URL to the github repository*)  The most recent version of METplus will be at the top of this page.  Scroll down to the ‘Sample Input Data’ section. (*Scroll down to the Sample Input Data section*)  There are tarballs under the ‘MET Tool Wrapper’ and ‘Model Applications’ with file extensions .tgz.  You will download all the tarballs under these two sections.

Click on each link to download the data and save it to the directory you specified in the METPLUS_DATA environment variable in the TutorialSetup.linux-csh.sh shell script. It will be easier on you if you configure your browser to always ask you where to save downloaded files. (*Click on one of these and save it to your METplus_Tutorial directory*).  Uncompress and untar each of these tarballs by using this comman (*At terminal, enter tar -xvfz <tarball-name.tgz>  for one of the tarballs you’ve saved*)

Now you are ready to go through the remainder of the online METplus tutorial.

