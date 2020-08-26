.. _metplus_common_config_vars:

Common Configuration Variables
==============================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/KCISG0phmbw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 3.1**.

(*Introduction*)

(*show https://dtcenter.github.io/METplus/Users_Guide/systemconfiguration.html#common-config-variables*)

This video will cover METplus wrapper configuration variables that are used in most use cases. They control things like time looping and information about input fields and file paths. The configurations covered in this video are described in detail in `Chapter 3 section 3 <https://dtcenter.github.io/METplus/Users_Guide/systemconfiguration.html#common-config-variables>`_ of the METplus User's Guide.

Time Looping
------------

The METplus wrappers allow you to set a range of run times to process. For each run time, the wrappers will build commands to run the MET tools. The LOOP_BY variable determines if the run times should loop over initialization (INIT) times or valid (VALID) times. If LOOP_BY is set to INIT (or RETRO), then your configuration file must contain INIT_TIME_FMT, INIT_BEG, INIT_END, and INIT_INCREMENT. If LOOP_BY is set to VALID (or REALTIME), then your configuration file must contain VALID _TIME_FMT, VALID _BEG, VALID _END, and VALID _INCREMENT. Let’s focus on looping by valid time for now.

Looping by Valid Time
^^^^^^^^^^^^^^^^^^^^^

VALID_TIME_FMT defines the format of VALID_BEG and VALID_END. It uses Python’s strftime notation and accepts any strftime directives. A list of all possible directives can be found at strftime.org.

(*show https://strftime.org*)

The example configuration shown here will loop by valid time from February 1st, 2020 until February 3rd, 2020. The valid time format is set to contain year, month, and day, so the valid begin and end values match that format::

  LOOP_BY = VALID

  VALID_TIME_FMT = %Y%m%d

  VALID_BEG = 20200201
  VALID_END = 20200203

This next example contains the hour in the valid time format and the valid begin and end values. Execution will start at 12Z on February 1st, 2020 and will end at 18Z on February 1st, 2020::

  LOOP_BY = VALID

  VALID_TIME_FMT = %Y%m%d%H

  VALID_BEG = 2020020112
  VALID_END = 2020020318

The VALID_INCREMENT variable determines the interval between run times. The valid begin time will be processed, then the valid increment will be added to that time to determine the next run time. If the new run time is greater than the valid end time, then execution will stop. The value must be at least one minute::

  VALID_INCREMENT = 3600

The default units for valid increment are seconds if no unit identifier is present. Year, month, day, hour, minute, and second can be defined by adding the letter of the corresponding Python strftime directive to the end of the value. For example, a capital letter M corresponds to minute and a lowercase letter m corresponds to month::

  VALID_INCREMENT = 1M

Looping by Initialization Time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your use case needs to loop over initialization times instead of valid times, set the LOOP_BY variable to INIT and set the appropriate variables to define the initialization time format, begin time, end time, and increment.

The configuration shown here will loop by initialization time from March 31, 2020 until April 1st, 2020 in 6 hour increments::

  LOOP_BY = INIT

  INIT_TIME_FMT = %Y%m%d

  INIT_BEG = 20200331
  INIT_END = 20200401

  INIT_INCREMENT = 6H

Looping over Forecast Leads
^^^^^^^^^^^^^^^^^^^^^^^^^^^

For each run time defined by the INIT or VALID variables, you can iterate over a list of forecast leads. The LEAD_SEQ variable is used to define a comma-separated list of forecast leads to process relative to the current initialization or valid time::

  LEAD_SEQ = 3, 6, 9

The default unit for the lead sequence is hour, so this configuration will process the 3 hour, 6 hour, and 9 hour forecast leads. You can define other units, such as minutes, by adding the appropriate Python strftime directive letter::

  LEAD_SEQ = 15M, 30M

This will process the 15 minute and 30 minute forecast leads.

If LOOP_BY is set to INIT, then each forecast lead will be added to the current initialization run time. If LOOP_BY is set to VALID, then each forecast lead will be subtracted from the current valid run time.

Skipping Times
^^^^^^^^^^^^^^

(*show examples from https://dtcenter.github.io/METplus/Users_Guide/systemconfiguration.html#skipping-times*)

A new feature added to the METplus wrappers in version 3.1 is the ability to skip certain times. The variable SKIP_TIMES in the [config] section controls this functionality. The times to skip are defined with Python string formatting directives followed by a colon, then a list of values that match the format, separated by a comma. Each rule must be surrounded by double quotation marks.

There are a few examples listed in the METplus User’s Guide:

[ example 1 ]

This will skip the month of March, the 3rd month.

[ example 2 ]

This will skip every 30th and 31st day of each month.

You can specify multiple string formatting directives in a single time format definition.

[ example 5 ]

This configuration will skip the specific year, month, day of December 31, 1999 and October 31, 2014.

You can define multiple time skipping rules. Each runtime will be compared to all of the rules and will be skipped if it matches any of them. Separate out each rule with a comma. Again, be sure that each rule is surrounded by double quotation marks.

[ example 3 ]

This will skip every 30th and 31st day and every 3rd month.

You can also use begin/end/increment syntax to create a list of values without typing out each value.
[ example 4 ] 
If you only want to skip certain times for a single wrapper, you can use a wrapper-specific variable. Using a wrapper-specific variable will ignore the generic SKIP_TIMES values.
[ example 6 ] 
This will skip the months March through November for GridStat wrapper only. All other wrappers in the PROCESS_LIST will skip the 31st day of each month. Note that the SKIP_TIMES values are not applied to GridStat in this case.

Loop Order
----------

The LOOP_ORDER variable determines the order to run processes. Acceptable values for this variables are ‘processes’ and ‘times’ which define which to loop over first. The configuration shown here runs two processes, PCPCombine and GridStat, and two valid times: February 1st, 2020 at 12Z and February 1, 2020 at 13Z:: 

  PROCESS_LIST = PCPCombine, GridStat

  LOOP_BY = VALID

  VALID_TIME_FMT = %Y%m%d%H

  VALID_BEG = 2020020112

  VALID_END = 2020020113

  VALID_INCREMENT = 1H

If LOOP_ORDER = processes, then the PROCESS_LIST will be looped over first. For each item in the process list, that process will run for every run time specified before moving on to the next process in the list. The order of execution will be as shown:

* PCPCombine at February 1st, 2020 @12Z
* PCPCombine at February 1st, 2020 @13Z
* GridStat at February 1st, 2020 @12Z
* GridStat at February 1st, 2020 @13Z

If LOOP_ORDER = times, then the run times will be looped over first. For each run time, all of the processes in the process list will run before moving on to the next run time. The order of execution will be as shown:

* PCPCombine at February 1st, 2020 @12Z
* GridStat at February 1st, 2020 @12Z
* PCPCombine at February 1st, 2020 @13Z
* GridStat at February 1st, 2020 @13Z

Please note that some of the MET tools must be run with LOOP_ORDER = processes. For example, if running an analysis tool that processes data over a range of times, such as StatAnalysis or SeriesAnalysis, any tools run earlier in the process list will need to be called for all run times so that all of the data is available for the analysis tools to use.

(*Advanced topics: INIT_SEQ, Realtime Looping (now/today, shift, truncate), Custom Looping- should these go in another video?*)

There are a few additional sections in the User’s Guide that cover advanced topics that are not covered in this video. These include functionality for configuring real time looping, looping over custom strings like ensemble names, and defining a list of available initialization times of your forecast data to dynamically generate a list of forecast leads for each valid run time.

(*begin_end_incr syntax - used in multiple places (lead sequence, custom loop list, etc.) - should this go in another video? Useful tricks?*)

Field Info
----------

Many MET tools utilize configuration files to define the fields to process::

  //
  // Forecast and observation fields to be verified
  //
  fcst = {
    field = [
      {
        name       = "APCP";
        level      = [ "A03" ];
        cat_thresh = [ >0.0, >=5.0 ];
      },
      {
        name       = "TMP";
        level      = [ "P250", “P500”, “P750”, “P1000” ];
      },
      {
        name       = "RH";
        level      = [ "P150", “P250” ];
      }
    ];
  }
  obs = fcst;

The configuration files read by the METplus wrapper allow users to define these fields in one place so changes are not needed in every MET configuration file::

  FCST_VAR1_NAME = APCP
  FCST_VAR1_LEVELS = A03, A06
  FCST_VAR1_THRESH = >0.0, >=5.0

  OBS_VAR1_NAME = APCP
  OBS_VAR1_LEVELS = A03, A06
  OBS_VAR1_THRESH = >0.0, >=5.0

  FCST_VAR2_NAME = TMP
  FCST_VAR2_LEVELS = P250, P500, P750, P1000

  OBS_VAR2_NAME = TMP
  OBS_VAR2_LEVELS = P250, P500, P750, P1000

  FCST_VAR3_NAME = RH
  FCST_VAR3_LEVELS = P150, P250
  FCST_VAR3_OPTIONS = GRIB_lvl_typ = 105;

  OBS_VAR3_NAME = RH
  OBS_VAR3_LEVELS = P150, P250

The field name for forecast data is defined with FCST_VAR<n>_NAME, where <n> is any integer. A comma-separated list of levels can be defined for each name::

  FCST_VAR1_NAME = APCP
  FCST_VAR1_LEVELS = A03, A06

If forecast name/level values are set for a given VAR<n>, then a corresponding observation name/level value must be set::

  OBS_VAR1_NAME = APCP
  OBS_VAR1_LEVELS = A03, A06

If the values for both forecast and observation fields are the same, then variables beginning with BOTH\_ may be used instead to describe both datasets::

  BOTH_VAR1_NAME = APCP
  BOTH_VAR1_LEVELS = A03, A06

Thresholds
----------

Threshold values can be defined with [FCST/OBS/BOTH]_VAR<n>_THRESH variables. The value is a comma-separated list of values that must start with a comparison operator and contain at least one digit. The comparison operators can be defined with symbols:

>,>=,==,!=,<,<=

Or their alphabetic equivalent:

gt,ge,eq,ne,lt,le

Complex thresholds can be combined with the “and” operator, notated with two ampersands (&&) or the “or” operator, notated with two vertical bars (||).

Here is an example::

  FCST_VAR1_THRESH = >0.0, >=5.0
  OBS_VAR1_THRESH = gt0.0, ge2.54

Extra options
-------------

(*show https://dtcenter.github.io/METplus/Users_Guide/systemconfiguration.html#fcst-var-n-options-obs-var-n-options*)

There are additional options that can be defined in the MET configuration field dictionary, such as ???. See the MET User’s Guide for more information on what can be added. There are defined with the [FCST/OBS/BOTH]_VAR<n>_OPTIONS variables::

  FCST_VAR3_OPTIONS = GRIB_lvl_typ = 105;

Each option must end with a semi-colon. Multiple options can be defined::

  FCST_VAR3_OPTIONS = GRIB_lvl_typ = 105; set_attr_name = "TEMP";

Wrapper-specific
----------------

(* show https://dtcenter.github.io/METplus/Users_Guide/systemconfiguration.html#wrapper-specific-field-info*)

New to METplus 3.0 is the ability to specify VAR<n> items differently across comparison wrappers. In previous versions, it was assumed that the list of forecast and observation files that were processed would be applied to any MET Stat tool used, such as GridStat, PointStat, EnsembleStat, MODE, or MTD. This prevented the ability to run, for example, EnsembleStat, then pass the output into GridStat.

(*show example 1*)

If the generic FCST_VAR<n>_NAME variables are used, the same values will be applied to all tools that don’t have wrapper specific fields defined. If wrapper specific fields are defined, any generic fields will be ignored.

(*show example 2*)

In this example, GridStat will process HGT at pressure levels 500 and 750 and TMP at pressure levels 500 and 750, while EnsembleStat will only process HGT at pressure level 500. To configure EnsembleStat to also process TMP, the user will have to define it explicitly with FCST_ENSEMBLE_STAT_VAR2_NAME.
This functionality applies to GridStat, EnsembleStat, PointStat, MODE, and MTD wrappers only.
For more information on GRIB_lvl_typ and other file-specific commands, review the MET User’s Guide, Chapter 3.

Directory/Template Info
-----------------------

(*show https://dtcenter.github.io/METplus/Users_Guide/systemconfiguration.html#directory-and-filename-template-info*)

Follow along User’s Guide info?

Sub-topics: Using templates (obs, fcst, data assimilation), time shifting, file windows

