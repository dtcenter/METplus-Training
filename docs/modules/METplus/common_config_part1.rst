.. _metplus_common_config_part1:

Common Configuration Variables
==============================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/watch?v=0ZMEf10lUYc" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 3.1**.

(*Setup: Pull up webpage: https://dtcenter.github.io/METplus/Users_Guide/systemconfiguration.html#common-config-variables*)
(*Setup: Pull up webpage: https://strftime.org*)

(*Introduction*)

(*Show Title Slide*)

Common Configuration Variables Part 1: Timing Control
-------------------------------------------------------------

This video will describe the METplus wrapper configuration variables that are used to control time.

(*show https://dtcenter.github.io/METplus/Users_Guide/systemconfiguration.html#common-config-variables*)

The material covered in this video is described in detail in the Common Config Variables
section in the System Configuration Chapter of the METplus User's Guide, shown here.

`Common Config Variables <https://dtcenter.github.io/METplus/Users_Guide/systemconfiguration.html#common-config-variables>`_

The METplus wrappers allow you to set a range of run times to process. For each run time, the wrappers will build
commands to run the MET tools.

(*Show Next Slide*)

The LOOP_BY variable in the [config] section determines if the run times that are processed should be based on
initialization times or valid times.
If LOOP_BY is set to VALID, then your configuration file must contain the valid time format, valid beg,
valid end and valid increment variables.

(*Show Next Slide*)

Loop by can also be set to REALTIME to loop over valid times if you prefer that terminology.
You will still need to set the appropriate VALID time variables.

(*Show Next Slide*)

If LOOP_BY is set to INIT, then your configuration file must contain
the init time format, init beg, init end and init increment variables.

(*Show Next Slide*)

RETRO can also be used for the value of loop by, but you will still need to set the appropriate INIT time variables.

Let’s focus on looping by valid time for now.

Looping by Valid Time
^^^^^^^^^^^^^^^^^^^^^

(*Show Next Slide*)

VALID_TIME_FMT defines the format of the valid begin and end times.
It uses Python’s string format notation and accepts any of those directives.

(*show https://strftime.org*)

A list of all possible directives can be found at this website.

(*Switch back to Slide*)

The example configuration shown here will loop by valid time from March 1st, 2020 until March 3rd, 2020.

(*Show Next Slide*)

The valid time format is set to contain year, month, and day, so the valid begin and end values must match that format::

(*Pause*)

(*Show Next Slide*)

This next example adds the hour in the valid time format, so the valid begin and end values must include the hour as well.
Execution will start at 12Z on March 1st and will end at 18Z on March 3rd.

(*Show Next Slide*)

The VALID_INCREMENT variable determines the interval between run times. The valid begin time will be processed, then the
valid increment will be added to that time to determine the next run time. If the new run time is later than the valid
end time, then execution will stop. The value must be at least 1 minute or 60 seconds.
The default units for valid increment are seconds if no unit identifier is present.

(*Show https://dtcenter.github.io/METplus/Users_Guide/systemconfiguration.html#time-interval-units*)

Time interval units can be explicitly defined by adding a letter that represents year, month, day, hour, minute, or second.
The supported time interval units are listed in the User's Guide.

(*Show Next Slide*)

For example, a capital letter H represents hours.

(*Show Next Slide*)

In this example, the run times are processed every 12 hours --
valid at 12Z on March. 1, 0Z on March 2, 12Z on March 2, 0Z on March 3, and 12Z on March 3.
Note that the valid end time is 18Z, but that time was not processed.

Looping by Initialization Time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(*Show Next Slide*)

If your use case should loop over initialization times instead of valid times, set the LOOP_BY variable to INIT and
set the corresponding variables. They are configured in the same way as the valid time variables.

Looping over Forecast Leads
^^^^^^^^^^^^^^^^^^^^^^^^^^^

(*Show Next Slide*)

For each run time defined by the INIT or VALID variables, you can iterate over a list of forecast leads. The LEAD_SEQ
variable is used to define a comma-separated list of forecast leads to process relative to the current initialization
or valid time. The default units for the lead sequence is hours, so this example will process the 3 hour and 6 hour
forecast leads for each run time. You can define other units, such as minutes, by adding the appropriate letter.

(*Show Next Slide*)

This example will process the 15 minute and 30 minute forecast leads.

(*Show Next Slide*)

If LOOP_BY is set to VALID, then each forecast lead will be subtracted from the current valid run time to compute the
initialization time.

(*Show Next Slide*)

Here we process the first valid time, March 1 @ 12Z for the 3 hour forecast lead, initialized at 9Z, then the
6 hours forecast lead, initialized at 6Z. Then we increment the valid time by 12 hours and process 0Z on Mar. 2
for the 3 hour lead, initialized at 21Z of the previous day, then the 6 hour lead, initialized at 18Z on the previous day.

(*Show Next Slide*)

If LOOP_BY is set to INIT, then each forecast lead will be added to the current initialization run time to compute the
valid time.

(*Show Next Slide*)

Here we are using the same run times but based around the initialization time instead of the valid time.
We process the first init time, Mar. 1, 2020 @ 12Z first for the 3 hour forecast lead, valid at 15Z, then the
6 hours forecast lead, valid at 18Z. Next we increment the init time by 12 hours and process 0Z on Mar. 2, 2020, first
for the 3 hour lead, valid at 3Z, then finally the 6 hour lead, valid at 6Z.

Again, more information on these topics is found in the METplus User's Guide webpage, including more advanced timing
control topics.

(*END PART 1*)


Skipping Times
^^^^^^^^^^^^^^

(*show examples from https://dtcenter.github.io/METplus/Users_Guide/systemconfiguration.html#skipping-times*)

A new feature added to the METplus wrappers in version 3.1 is the ability to skip certain times. The variable SKIP_TIMES
in the [config] section controls this functionality. The times to skip are defined with Python string formatting
directives followed by a colon, then a list of values that match the format, separated by a comma. Each rule must be
surrounded by double quotation marks.

There are a few examples listed in the METplus User’s Guide:

[ example 1 ]

This will skip the month of March, the 3rd month.

[ example 2 ]

This will skip every 30th and 31st day of each month.

You can specify multiple string formatting directives in a single time format definition.

[ example 5 ]

This configuration will skip the specific year, month, day of December 31, 1999 and October 31, 2014.

You can define multiple time skipping rules. Each runtime will be compared to all of the rules and will be skipped if
it matches any of them. Separate out each rule with a comma. Again, be sure that each rule is surrounded by double
quotation marks.

[ example 3 ]

This will skip every 30th and 31st day and every 3rd month.

You can also use begin/end/increment syntax to create a list of values without typing out each value.
[ example 4 ] 
If you only want to skip certain times for a single wrapper, you can use a wrapper-specific variable. Using a
wrapper-specific variable will ignore the generic SKIP_TIMES values.
[ example 6 ] 
This will skip the months March through November for GridStat wrapper only. All other wrappers in the PROCESS_LIST will
skip the 31st day of each month. Note that the SKIP_TIMES values are not applied to GridStat in this case.

Loop Order
----------

The LOOP_ORDER variable determines the order to run processes. Acceptable values for this variables are ‘processes’ and
‘times’ which define which to loop over first. The configuration shown here runs two processes, PCPCombine and GridStat,
and two valid times: March 1st, 2020 at 12Z and March 1, 2020 at 13Z::

  PROCESS_LIST = PCPCombine, GridStat

  LOOP_BY = VALID

  VALID_TIME_FMT = %Y%m%d%H

  VALID_BEG = 2020020112

  VALID_END = 2020020113

  VALID_INCREMENT = 1H

If LOOP_ORDER = processes, then the PROCESS_LIST will be looped over first. For each item in the process list, that
process will run for every run time specified before moving on to the next process in the list. The order of execution
will be as shown:

* PCPCombine at March 1st, 2020 @12Z
* PCPCombine at March 1st, 2020 @13Z
* GridStat at March 1st, 2020 @12Z
* GridStat at March 1st, 2020 @13Z

If LOOP_ORDER = times, then the run times will be looped over first. For each run time, all of the processes in the
process list will run before moving on to the next run time. The order of execution will be as shown:

* PCPCombine at March 1st, 2020 @12Z
* GridStat at March 1st, 2020 @12Z
* PCPCombine at March 1st, 2020 @13Z
* GridStat at March 1st, 2020 @13Z

Please note that some of the MET tools must be run with LOOP_ORDER = processes. For example, if running an analysis tool
that processes data over a range of times, such as StatAnalysis or SeriesAnalysis, any tools run earlier in the process
list will need to be called for all run times so that all of the data is available for the analysis tools to use.

(*Advanced topics: INIT_SEQ, Realtime Looping (now/today, shift, truncate), Custom Looping- should these go in another video?*)

There are a few additional sections in the User’s Guide that cover advanced topics that are not covered in this video.
These include functionality for configuring real time looping, looping over custom strings like ensemble names, and
defining a list of available initialization times of your forecast data to dynamically generate a list of forecast leads
for each valid run time.

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

The configuration files read by the METplus wrapper allow users to define these fields in one place so changes are not
needed in every MET configuration file::

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

The field name for forecast data is defined with FCST_VAR<n>_NAME, where <n> is any integer. A comma-separated list of
levels can be defined for each name::

  FCST_VAR1_NAME = APCP
  FCST_VAR1_LEVELS = A03, A06

If forecast name/level values are set for a given VAR<n>, then a corresponding observation name/level value must be set::

  OBS_VAR1_NAME = APCP
  OBS_VAR1_LEVELS = A03, A06

If the values for both forecast and observation fields are the same, then variables beginning with BOTH\_ may be used
instead to describe both datasets::

  BOTH_VAR1_NAME = APCP
  BOTH_VAR1_LEVELS = A03, A06

Thresholds
----------

Threshold values can be defined with [FCST/OBS/BOTH]_VAR<n>_THRESH variables. The value is a comma-separated list of
values that must start with a comparison operator and contain at least one digit. The comparison operators can be
defined with symbols:

>,>=,==,!=,<,<=

Or their alphabetic equivalent:

gt,ge,eq,ne,lt,le

Complex thresholds can be combined with the “and” operator, notated with two ampersands (&&) or the “or” operator,
notated with two vertical bars (||).

Here is an example::

  FCST_VAR1_THRESH = >0.0, >=5.0
  OBS_VAR1_THRESH = gt0.0, ge2.54

Extra options
-------------

(*show https://dtcenter.github.io/METplus/Users_Guide/systemconfiguration.html#fcst-var-n-options-obs-var-n-options*)

There are additional options that can be defined in the MET configuration field dictionary, such as ???. See the MET
User’s Guide for more information on what can be added. There are defined with the [FCST/OBS/BOTH]_VAR<n>_OPTIONS
variables::

  FCST_VAR3_OPTIONS = GRIB_lvl_typ = 105;

Each option must end with a semi-colon. Multiple options can be defined::

  FCST_VAR3_OPTIONS = GRIB_lvl_typ = 105; set_attr_name = "TEMP";

Wrapper-specific
----------------

(* show https://dtcenter.github.io/METplus/Users_Guide/systemconfiguration.html#wrapper-specific-field-info*)

New to METplus 3.0 is the ability to specify VAR<n> items differently across comparison wrappers. In previous versions,
it was assumed that the list of forecast and observation files that were processed would be applied to any MET Stat tool
used, such as GridStat, PointStat, EnsembleStat, MODE, or MTD. This prevented the ability to run, for example,
EnsembleStat, then pass the output into GridStat.

(*show example 1*)

If the generic FCST_VAR<n>_NAME variables are used, the same values will be applied to all tools that don’t have wrapper
specific fields defined. If wrapper specific fields are defined, any generic fields will be ignored.

(*show example 2*)

In this example, GridStat will process HGT at pressure levels 500 and 750 and TMP at pressure levels 500 and 750, while
EnsembleStat will only process HGT at pressure level 500. To configure EnsembleStat to also process TMP, the user will
have to define it explicitly with FCST_ENSEMBLE_STAT_VAR2_NAME.
This functionality applies to GridStat, EnsembleStat, PointStat, MODE, and MTD wrappers only.
For more information on GRIB_lvl_typ and other file-specific commands, review the MET User’s Guide, Chapter 3.

Directory/Template Info
-----------------------

(*show https://dtcenter.github.io/METplus/Users_Guide/systemconfiguration.html#directory-and-filename-template-info*)

Follow along User’s Guide info?

Sub-topics: Using templates (obs, fcst, data assimilation), time shifting, file windows

