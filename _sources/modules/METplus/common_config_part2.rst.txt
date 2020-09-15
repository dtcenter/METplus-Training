.. _metplus_common_config_part2:

Common Config Part 2 - Filename Templates and Example METplus Wrapper
=====================================================================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/_TlPgEmcNis" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 3.1**.

(*Will split this file into 2*)

(*Setup: Open 2 terminals in Docker, one for running master_metplus.py, one for editing the configuration files*)
(*Setup: Run PS1='${debian_chroot:+($debian_chroot)}\w\$ ' to remove command prompt text*)
(*Setup: Open URL: https://dtcenter.github.io/METplus/Users_Guide/systemconfiguration.html#directory-and-filename-template-info*)
(*Setup: Open URL: strftime.org*)
(*Setup: Open URL: https://dtcenter.github.io/METplus/generated/met_tool_wrapper/Example/Example.html#metplus-configuration*)

(*Introduction*)

If you would like to follow along with the exercises in this video, please select one of the options to set up your own
:ref:`Training Environment <training_environment>`.

(*Show Title*)

This video will cover how the METplus wrappers find input files for each run time and how to use the Example wrapper
to explore this functionality.

(*Show https://dtcenter.github.io/METplus/Users_Guide/systemconfiguration.html#directory-and-filename-template-info*)

In the System Configuration Chapter of the METplus Wrappers User's Guide, under the Common Config Variables section
there is a sub-section called Directory and Filename Template Info. This is a great source of information to help
understand how filename templates can be used to find input files and define output filenames.

Input file names are described with two variables: an input directory in the dir section and
a corresponding input template in the filename_templates section. The input directory should be set to
the top-level directory that contains all of the data for a given input to the MET tools. The input template
describes how the input files under the input directory are named using filename template tags. These tags start and end
with curly braces. They contain an identifier to determine what value should be substituted for the tag and options to
provide more information about how the value should be represented. The identifier and all options are separated by a
question mark. The most commonly used template tags contain valid, init, or lead as the identifier,
representing valid time, initialization time, and forecast lead respectively, and a format
option to determine how the time value should be displayed. The format option is represented with f-m-t following by
an equals sign and a set of Python string format directives.

(*Show strftime.org*)

init and valid can use any of the directives from this website.

(*Switch back*)

lead and level can only use hours, minutes, seconds, or any combination of the three. You can specify the number of
digits of these values by adding a number after the percent sign and in front of the letter. The default precision of
hour, minute, and second are 2 digits.

For each run time, the time values are substituted in the template, then the directory value is prepended to determine
the full path to the desired input file. Please note that filename template tags are currently not supported in the directory
variables. Wildcard characters question mark and asterisk are currently supported in the templates.
A question mark will allow any single character and an asterisk will allow more than one character. This is more commonly
used with tools that allow multiple input files, but it can be used to find a single file. However, if more than one
input file is found to match the wildcard expression and the MET tool only allows a single input file, an error will occur.

How these configuration variables work together is best demonstrated by running the Example wrapper.
