.. _metplus_example_wrapper:

Common Config Part 2 - Filename Templates and Example METplus Wrapper
=====================================================================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/5m_1KXz9mM8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 3.1**.

(*Setup: Open 2 terminals in Docker, one for running master_metplus.py, one for editing the configuration files*)
(*Setup: Run PS1='${debian_chroot:+($debian_chroot)}\w\$ ' to remove command prompt text*)
(*Setup: Open URL: https://dtcenter.github.io/METplus/Users_Guide/systemconfiguration.html#directory-and-filename-template-info*)
(*Setup: Open URL: strftime.org*)
(*Setup: Open URL: https://dtcenter.github.io/METplus/generated/met_tool_wrapper/Example/Example.html#metplus-configuration*)

(*Introduction*)

If you would like to follow along with the exercises in this video, please select one of the options to set up your own
:ref:`Training Environment <training_environment>`.

(*Show Title*)

This video will demonstrate how to run the Example wrapper use case.

(*Open https://dtcenter.github.io/METplus/generated/met_tool_wrapper/Example/Example.html#metplus-configuration*)

Information about each use case in the METplus repository can be found in the User's Guide under METplus Use
Cases.

(*Click through MET tools, Example, Example.conf, scroll down to METplus Configuration*)

The Example wrapper does not run any of the MET applications, but it is a good starting point to understand how the
other wrappers are used. It loops over each run time, substitutes values into the filename template, and logs
the results. It allows you to adjust the configuration values to build the correct file paths without cluttering
the log output with extra information.

(*Open 2 terminals*)

This video assumes that you have already installed the MET tools and configured the METplus wrappers correctly.
If you are following the online tutorial, you have likely already set up your environment by sourcing the tutorial
setup scripts. If not, and you haven’t already created a user or tutorial configuration file, you will have to do so
before running the example.

This is the user configuration file I am using on Docker to run this example::

(*Run: less METplus_Tutorial/tutorial.conf*)

This file is provided in the tutorial and references environment variables to set the METplus variables.
These are the values of those environment variables:

(*Run: echo METPLUS_TUTORIAL_DIR; echo ${METPLUS_BUILD_BASE}; echo ${MET_BUILD_BASE}; echo ${METPLUS_DATA}*)

Let's take a look at the Example wrapper use case configuration file. It is found in the METplus repository under
parm/use_cases/met_tool_wrapper/Example and is named Example.conf.

(*Type: less ${METPLUS_BUILD_BASE}parm/use_cases/met_tool_wrapper/Example/Example.conf, but don't hit enter*)

(*Unhide Example.conf*)

If you are unfamiliar with the time looping variables, please refer to the Common Config Variables - Part 1 video.
Link: :ref:`Common Configuration Variables <metplus_common_config_part1>` video.

This use case is looping by valid time starting at February 1st, 2017 at 0Z and ending on February 2 at 0Z, incrementing
by 6 hours each time. For each valid time, 4 forecast leads will be processed -- 3 hour, 6 hour, 9 hour, and 12 hour.
The EXAMPLE_CUSTOM_LOOP_LIST is an optional list of strings that can be referenced in filename templates using 'custom'
as the template tag identifier. Each run time defined by the time variables will be called once for each item in this
list. This can be useful in certain use cases, such as processing a set of ensembles. If the custom loop list is left
blank or not set at all, the custom template tag will be replaced with an empty string.

(*NOTE: Consider moving the CUSTOM_LOOP_LIST information into the Timing Control video instead*)

The example input dir variable defines the directory where your imaginary data resides. Remember, filename template tags
will not be handled properly if they are used in the input directory variables.
Finally, we have the example input template, which defines how our input files are named. This example uses init, lead,
and custom filename template tags.

(*Pause*)

Let's run this use case.

(*Hide Example.conf*)

To run this use case, we will run... (*describe what you type*)

(*Type master_metplus.py -c $METPLUS_BUILD_BASE/parm/use_cases/met_tool_wrapper/Example/Example.conf -c $METPLUS_TUTORIAL_DIR/tutorial.conf*)

A lot of text was output to the screen. Let's open the log file to take a closer look and what happened. We recently
added the log file name to bottom of the screen output to make it easier to determine which log file to open. By default
the timestamp is appended to the log file name for each run. I'm going to copy this filepath and open the log file.

(*Copy the log file path and run less <filename>*)

The first line of the log output is the command that was run. Here you can see that METplus was run for this valid time.
These are the values that were set for the input directory and input template. Each forecast lead in the lead sequence
list is processed for each custom string. First the custom string ext and the 3 hour forecast lead were processed, then
the custom string nc and the 3 hour lead are processed. See how the file path for each run has been filled out.
You'll notice that even though we are looping by valid time, the initialization time values were computed appropriately.
Also notice that the forecast lead is always 3 digits. This happened because the lead template tag format was set to
percent three capital H.

(*Scroll with down arrow key*)

After all of the forecast leads and custom strings were processed, the next valid time is processed in the same way.

(*Pause*)

Now let's modify some of these settings. We recommend that you copy the use case configuration files in the METplus
repository into your own directory instead of modifying them directly. I will create a directory called user_config
under the METplus tutorial directory and copy the config file into it.

(*Run: mkdir $METPLUS_TUTORIAL_DIR/user_config; cp $METPLUS_BUILD_BASE/parm/use_cases/met_tool_wrapper/Example/Example.conf $METPLUS_TUTORIAL_DIR/user_config/Example_tutorial.conf*)

I renamed the file Example underscore tutorial dot conf so I remember what it contains.

(*Type but don't hit enter: vi $METPLUS_TUTORIAL_DIR/user_config/Example_tutorial.conf*)
(*Rename the ExampleText source to Example_tutorial.conf and unhide the Example.conf group*)

Now let's edit the new file.

I will change the valid end value to the same value as valid beg so that only one valid time is processed.
(*Do that*)
I'm also going to change the lead sequence to contain 1D and 2D, which stands for 1 day and 2 days
(*Change LEAD_SEQ value to 1D, 2D -- NOTE: this is incorrect, should be lower-case d!*)
I don't want to use the custom loop list anymore, so I am going to remove the values here.
(*Do that*)
Last I am going to change the input template to something different.
(*Set EXAMPLE_INPUT_TEMPLATE to init_{init?fmt=%Y%m%d%H}_lead_{lead?fmt=%3H}_valid_{fmt=%Y%m%d}.nc*)

Now I'll save this file and run it through master_metplus

(*Save file but don't quit*)
(*Hide Example.conf*)

(*Run master_metplus.py with the new config file, step through finding the error, fix it, and rerun*)

(*Show Directory and Filename Template Info section of User's Guide*)

Be sure to read through this section of the User's Guide to learn about more advanced topics using filename
templates to find files to process.
