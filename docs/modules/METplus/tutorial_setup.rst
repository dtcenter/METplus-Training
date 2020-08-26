.. _metplus_tutorial_setup:

METplus Tutorial Setup
======================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/KCISG0phmbw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 3.1**.

(*Introduction*)

https://dtcenter.org/metplus-practical-session-guide-version-3-0/session-1-metplus-setupgrid-grid

Welcome to the METplus Tutorial.  The Tutorial is organized into 5 chapters, with several videos per chapter that focus on using MET tools and METplus wrappers to perform analysis of meteorological forecast and observation, including plotting, forecast-obs comparisons, statistical analysis, and storm tracking.  The goal of METplus is to make a set of tools that are easily used by scientists for meteorological evaluation.

https://dtcenter.org/metplus-practical-session-guide-version-3-0/session-1-metplus-setupgrid-grid/metplus-setup


This video describes how to set up the METplus Tutorial environment, which assumes METplus is pre-installed on either an NCAR Linux machine (Dakota, eyewall, Kiowa) or on the NOAA Hera server.  METplus can be installed on other machines, but that won’t be covered here; there are links in the chapter on where to go to download the tarballs and install.  METplus consists of the METplus python wrappers, the MET tools (C++ executables), the METviewer GUI, and METplotpy, METcalcpy, and METdb, which are still under development.  Here we’re only looking at METplus python wrappers and the MET tools.

https://dtcenter.org/metplus-practical-session-guide-version-3-0/session-1-metplus-setupgrid-grid/metplus-setup/metplus-initial-setup


The first thing you should do is pick a location for your METplus Tutorial directory.  This is where you will have customized configuration files as well as output, which can be PostScript images, NetCDF files, and ascii (text) files.  It is recommended you use space on a scratch or work disk rather than your home directory so you don’t run out of space.  When you identify a place for your METplus_Tutorial directory, use either the bash or cshrc command to set the environment variable ${METPLUS_TUTORIAL_DIR} to /path/to/METplus_Tutorial, where /path/to is the absolute path (eg /scratch1/BMC/dtc/Joe.User/METplus_Tutorial on hera).
Following that, you can use the mkdir command to create the directory if you haven’t done so already.

Next there are two files that need to be copied into your METplus_Tutorial directory, TutorialSetup.[hera/bash/cshrc].sh and tutorial.conf.  TutorialSetup.[bash/cshrc/hera].sh is a shell script that sets up the rest of the METplus environment.  You will need to edit /path/to to point to your METplus_Tutorial directory.  Close the file and do

source TutorialSetup.[hera/linux-bash/linux-cshrc].sh

using bash or cshrc for whichever shell you prefer, unless you are on hera, which has its own unique setup.  Following this, type “env” to see that the MET and METplus environment variables have been set, and “which master_metplus.py” to see that there is a path to master_metplus.py.  Typing “echo ${METPLUS_BUILD_BASE}”, “echo ${MET_BUILD_BASE}”, and echo “${MET_DATA}” to confirm that these environment variables are set to point to the proper directories.

Next, “cd ${METPLUS_TUTORIAL_DIR} to get into the METplus_Tutorial directory, and “mkdir user_config” and “mkdir output”.  These directories will be used for custom METplus configure scripts and output data, respectively.

https://dtcenter.org/metplus-practical-session-guide-version-3-0/session-1-metplus-setupgrid-grid/metplus-setup/metplus-directories-configuration-files-overview

Typing “ls ${METPLUS_BUILD_BASE} will show the contents of that directory, which is where the METplus scripts and other files live.  Looking in the parm subdirectory, there is the metplus_config directory, which contains 4 files: metplus_system.conf, metplus_data.conf, metplus_runtime.conf, and metplus_logging.conf.  These 4 files set most of the METplus variables (which can be modified by other configuration files) and are called first by default.

Also under the parm directory is use_cases, which is divided into metplus_tool_wrapper (metplus configure files designed to call MET tools) and model_applications, which are organized by model type.  In the default cases, you will call these configuration files depending on what task you are trying to do.  In other cases, you will copy these files to your user_config directory and modify them there, leaving the unmodified files in place.

https://dtcenter.org/metplus-practical-session-guide-version-3-0/session-1-metplus-setupgrid-grid/metplus-setup/metplus-user-configuration-settings

Lastly, run the use_case calling Example.conf to see that OUTPUT_BASE is not defined and the command errors out.  Open up the tutorial.conf file (in your METplus_Tutorial directory) to see that OUTPUT_BASE is defined there.  When you call master_metplus.py, the first config file should be tutorial.conf; values can be modified by subsequent calls to config files.

An example of this is adding another configuration file that changes the output directory in a new file, change_output_base.conf, which you create in your user_config directory.  Add in the text as instructed and go to the next page.  Running master_metplus.py with tutorial.conf and Example.conf places the output under the output directory, including a file called master_metplus.conf which contains all of the final configurations set by all of the configuration files.  Values set by the first 4 config files and tutorial.conf can be overridden by subsequent calls to other config files.  This can be seen by running master_metplus.py with user_config/change_output_base.conf called last; the data should now be in output_changed.

This concludes the METplus Setup video.  You are now ready to proceed with Chapter 1: MET Tool: PCP Combine

