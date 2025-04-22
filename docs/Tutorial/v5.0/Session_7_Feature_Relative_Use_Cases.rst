Session 7: Feature Relative Use Cases
=====================================

Session 7: Feature Relative Use Cases

METplus Practical Session 7
---------------------------

This session will cover two METplus feature relative use cases.

Prerequisites: Verify Environment is Set Correctly
--------------------------------------------------

Before running the tutorial instructions, you will need to ensure that you have a few environment variables set up correctly. If they are not set correctly, the tutorial instructions will not work properly.

.. note::

   1: Navigate to your tutorial directory and run the tutorial setup script.

.. important::

   In the following instructions, change "/path/to" to the directory you chose.
   EDIT AFTER COPYING and BEFORE HITTING RETURN!

.. code-block::

   cd /path/to/METplus-5.0.0_Tutorial
   source METplus-5.0.0_TutorialSetup.sh

 

.. note::

   2: Check that you have environment variables set correctly. If any of these variables are not set, navigate back to the METplus Setup section of the tutorial.

.. code-block::

   echo ${METPLUS_TUTORIAL_DIR}
   echo ${METPLUS_BUILD_BASE}
   echo ${MET_BUILD_BASE}
   echo ${METPLUS_DATA}
   ls ${METPLUS_TUTORIAL_DIR}
   ls ${METPLUS_BUILD_BASE}
   ls ${MET_BUILD_BASE}
   ls ${METPLUS_DATA}

.. important::

   METPLUS_TUTORIAL_DIR is the location of all of your tutorial work, including configuration files, output data, and any other notes you'd like to keep.
   METPLUS_BUILD_BASE is the full path to the METplus installation (/path/to/METplus-X.Y)
   MET_BUILD_BASE is the full path to the MET installation (/path/to/met-X.Y)
   METPLUS_DATA is the location of the sample test data directory

 

.. note::

   3: Check that the MET applications are in the path:

.. code-block::

   which point_stat

.. important::

   You should see the usage statement for Point-Stat. The version number listed should correspond to the version listed in MET_BUILD_BASE. If it does not, you will need to either reload the met module, or add ${MET_BUILD_BASE}/bin to your PATH.

 

.. note::

   4: Check that the correct version of run_metplus.py is in your PATH:

.. code-block::

   which run_metplus.py

.. important::

   If you don't see the full path to script from the shared installation, please set it. It should look the same as the output from this command:

.. code-block::

   echo ${METPLUS_BUILD_BASE}/ush/run_metplus.py
   ls ${METPLUS_BUILD_BASE}/ush/run_metplus.py

 

If more information is needed see the instructions in Session 1 for more information.

You are now ready to move on to the next section.

Click on a use case below to get started.

.. important::

   If you discover any typos, error in the run commands, incorrect output listed, or any other issues while completing the tutorial, you are encouraged to submit your findings to the METplus team in a GitHub Discussions. Be sure to provide what session and specific page you encountered the issue on.


METplus Use Case: Feature Relative (Series-Analysis by Initialization Time)
===========================================================================

METplus Use Case: Feature Relative (Series-Analysis by Initialization Time)

METplus Use Case: Feature Relative (Series-Analysis by init)
------------------------------------------------------------

Setup
^^^^^

In this exercise, you will perform a series analysis based on the init time of your sample data. This use case focuses on using the latitude and longitude pairs for a "feature", such as a tropical cyclone or extra-tropical cyclone, to identify a user-specified tile around the feature.  The tiles are then used to compute statistics using Series_Analysis.  Therefore, this use-case utilizes the MET Tc-Pairs, Tc-Stat, and Series-Analysis tools, and the METplus wrappers: TcPairs, ExtractTiles, TcStat, and SeriesAnalysis. Please refer to the `**MET Users Guide** `_ for a description of the MET tools and the `**METplus Users Guide**  `_for more details about the wrappers.

Review Use Case Configuration File: feature_relative.conf
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

View the file and study the configuration variables that are defined.

.. code-block::

   less ${METPLUS_BUILD_BASE}/parm/use_cases/model_applications/medium_range/TCStat_SeriesAnalysis_fcstGFS_obsGFS_FeatureRelative_SeriesByInit.conf

Note the configuration settings for this complex use-case. The **PROCESS_LIST** contains 5 items, 2 of which are the same wrapper, TCStat. Since METplus version 4.0.0 was released, users have had the ability to run multiple instances of a given tool using an instance name. The METplus User's Guide describes in detail how to use `Instance Names in the Process List `_ to configure two or more instances of the same tool with different settings.

For this example, the **[for_series_analysis]** instance of TCStat, which runs after the initial TCStat instance and an ExtractTiles instance, will inherit all of the settings from the initial TCStat instance. Then, it will override those settings with any of the settings found in the **[for_series_analysis]** section. Looking at the configuration file, we see the following:

.. admonition:: Sample Output

   TC_STAT_JOB_ARGS = -job filter -init_beg {INIT_BEG} -init_end {INIT_END} -dump_row {TC_STAT_OUTPUT_DIR}/{TC_STAT_DUMP_ROW_TEMPLATE}
   TC_STAT_OUTPUT_DIR = {SERIES_ANALYSIS_OUTPUT_DIR}
   TC_STAT_LOOKIN_DIR = {EXTRACT_TILES_OUTPUT_DIR}

This indicates that the **TC_STAT_JOB_ARGS, TC_STAT_OUTPUT_DIR,** and **TC_STAT_LOOKIN_DIR** will be overridden with the provided values.

.. important::

   Instance names are a powerful option for METplus users who need to run tools multiple times with different settings for some or all of the variables between each run. Combined with options such as CUSTOM_LOOP_LIST, intricate verification tasks can be completed in a single configuration file.

The **SERIES_ANALYSIS_STAT_LIST** is set to four statistics, but can be set to many more.  The size of the tiles are configurable using the **EXTRACT_TILES** settings.  Also, note that variables in **feature_relative.conf** reference other variables you defined in other configuration files. For example: 

.. admonition:: Sample Output

   TC_STAT_INPUT_DIR = {OUTPUT_BASE}/tc_pairs

This references **OUTPUT_BASE** which you set in the METplus defaults configuration file (**${METPLUS_BUILD_BASE}/parm/metplus_config/defaults.conf**). METplus config variables can reference other config variables, even if they are defined in a config file that is read afterwards.

Run METplus
^^^^^^^^^^^

Change to the METplus Tutorial Directory:

.. code-block::

   cd ${METPLUS_TUTORIAL_DIR}

Run the following command. Use config.OUTPUT_BASE to change the output directory from the command line:

.. code-block::

   run_metplus.py \
   ${METPLUS_BUILD_BASE}/parm/use_cases/model_applications/medium_range/TCStat_SeriesAnalysis_fcstGFS_obsGFS_FeatureRelative_SeriesByInit.conf \
   ${METPLUS_TUTORIAL_DIR}/tutorial.conf \
   config.OUTPUT_BASE=${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_init

You will see output streaming to your screen. This may take up to 4 minutes to complete. METplus is finished running when control returns to your terminal console and you see the following text:

.. admonition:: Sample Output

   INFO: METplus has successfully finished running.

Review the Output Files
^^^^^^^^^^^^^^^^^^^^^^^

You should have output files in the following directories from the intermediate wrappers TcPairs, ExtractTiles, and TcStat, respectively:

.. code-block::

   ls ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_init

.. admonition:: Sample Output

   tc_pairs
   extract_tiles
   track_data_atcf

and the output of interest, from the SeriesAnalysis wrapper:

.. admonition:: Sample Output

   series_analysis_init

which has a directory corresponding to the date(s) of data in the data window.  This area also includes the logs and a tmp directory:

.. code-block::

   ls ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_init/series_analysis_init

.. admonition:: Sample Output

   20141214_00

and under that directory are subdirectories named by the storm. They begin with ML. Below are a few examples:

.. code-block::

   ls ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_init/series_analysis_init/20141214_00

.. admonition:: Sample Output

   ML1201032014
   ML1201042014, etc.

and under each of those directories lies the files of interest:

.. code-block::

   ls ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_init/series_analysis_init/20141214_00/ML1201042014

.. admonition:: Sample Output

   series_analysis_files_fcst_ML1201042014_init_20141214000000_valid_ALL_lead_ALL.txt
   series_analysis_files_obs_ML1201042014_init_20141214000000_valid_ALL_lead_ALL.txt
   series_TMP_Z2_FBAR.png
   series_TMP_Z2_FBAR.ps
   series_TMP_Z2_ME.png
   series_TMP_Z2_ME.ps
   series_TMP_Z2.nc
   series_TMP_Z2_OBAR.png
   series_TMP_Z2_OBAR.ps
   series_TMP_Z2_TOTAL.png
   series_TMP_Z2_TOTAL.ps

The series_analysis_files_obs_ML########## (where ########## is the storm) is a text file that contains a list of the observation data included in the series analysis.

The series_analysis_files_fcst_ML########## (where ########## is the storm) is a text file that contains a list of forecast data included in the series analysis.

The .nc files are the series analysis output generated from the MET series_analysis tool.

The .png and .ps files are graphics files that can be viewed using display or ghostview, respectively:

.. code-block::

   display ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_init/series_analysis_init/20141214_00/ML1201042014/series_TMP_Z2_FBAR.png &amp;

or

.. code-block::

   gv ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_init/series_analysis_init/20141214_00/ML1201042014/series_TMP_Z2_FBAR.ps &amp;

.. note::

   Note: the &amp; is used to run this command in the background

Review the Log File
^^^^^^^^^^^^^^^^^^^

A log file is generated in your logging directory: **${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_init/logs**. The filename contains the timestamp corresponding to the current day. To view the log file:

.. code-block::

   ls ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_init/logs/metplus.log.*

Review the Final Configuration File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The final configuration file is** metplus_final.conf**. This contains all of the configuration variables used in the run.

.. code-block::

   less ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_init/metplus_final.conf


METplus Use Case: Feature Relative (Series-Analysis by Lead Time with Forecast Hour Grouping)
=============================================================================================

METplus Use Case: Feature Relative (Series-Analysis by Lead Time with Forecast Hour Grouping)

METplus Use Case: Feature Relative (Series-Analysis by lead, by forecast hour grouping)
---------------------------------------------------------------------------------------

Setup
^^^^^

In this exercise, you will perform a series analysis based on the lead time (forecast hour) of your sample data and organize your results by forecast hour groupings. This use case utilizes the MET Tc-Pairs, Tc-Stat, and Series-Analysis tools, and the METplus wrappers: TcPairs, ExtractTiles, TcStat, and SeriesAnalysis. Please refer to the `MET User's Guide `_ for a description of the MET tools and the `METplus Users Guide `_ for more details about the wrappers. Please note that the METplus User's Guide is a work-in-progress and may have missing content.

Change to the METplus Tutorial Directory:

.. code-block::

   cd ${METPLUS_TUTORIAL_DIR}

Review Use Case Configuration File: series_by_lead_by_fhr_grouping.conf
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

View the file and study the configuration variables that are defined.

.. code-block::

   less ${METPLUS_BUILD_BASE}/parm/use_cases/model_applications/medium_range/TCStat_SeriesAnalysis_fcstGFS_obsGFS_FeatureRelative_SeriesByLead.conf

Note that the Lead time groupings are specified by the **LEAD_SEQ** config options. 

.. admonition:: Sample Output

   # forecast lead sequence 1 list (0, 6, 12, 18)
   LEAD_SEQ_1 = begin_end_incr(0,18,6)
   LEAD_SEQ_1_LABEL = Day1
    
   # forecast lead sequence 2 list (24, 30, 36, 42)
   LEAD_SEQ_2 = begin_end_incr(24,42,6)
   LEAD_SEQ_2_LABEL = Day2

This references **OUTPUT_BASE **which you set in the METplus default configuration file (**metplus_config/defaults.conf**). METplus config variables can reference other config variables, even if they are defined in a config file that is read afterwards.

Run METplus
^^^^^^^^^^^

Run the following command:

.. code-block::

   run_metplus.py \
   ${METPLUS_TUTORIAL_DIR}/tutorial.conf \
   ${METPLUS_BUILD_BASE}/parm/use_cases/model_applications/medium_range/TCStat_SeriesAnalysis_fcstGFS_obsGFS_FeatureRelative_SeriesByLead.conf \
    dir.OUTPUT_BASE=${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_lead_fhr_groupings

You will see output streaming to your screen. This may take up to 3 minutes to complete. When it is complete, your prompt returns.

Review the Output Files
^^^^^^^^^^^^^^^^^^^^^^^

You should have output directories including the following that result from running the wrappers TcPairs, ExtractTiles, and TcStat, respectively:

.. code-block::

   ls ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_lead_fhr_groupings

.. admonition:: Sample Output

   track_data_atcf
   extract_tiles
   tc_pairs

and the output directory of interest, from the SeriesByLead wrapper:

.. admonition:: Sample Output

   series_analysis_lead

That directory contains the following directories:

.. code-block::

   ls ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_lead_fhr_groupings/series_analysis_lead

.. admonition:: Sample Output

   Day1
   Day2
   series_animate

Day1 contain the following files:

.. code-block::

   ls ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_lead_fhr_groupings/series_analysis_lead/Day1

.. admonition:: Sample Output

   series_analysis_files_fcst_init_ALL_valid_ALL_lead_ALL.txt
   series_analysis_files_obs_init_ALL_valid_ALL_lead_ALL.txt
   series_F000_to_F018_TMP_Z2_FBAR.png
   series_F000_to_F018_TMP_Z2_FBAR.ps
   series_F000_to_F018_TMP_Z2_ME.png
   series_F000_to_F018_TMP_Z2_ME.ps
   series_F000_to_F018_TMP_Z2.nc
   series_F000_to_F018_TMP_Z2_OBAR.png
   series_F000_to_F018_TMP_Z2_OBAR.ps
   series_F000_to_F018_TMP_Z2_TOTAL.png
   series_F000_to_F018_TMP_Z2_TOTAL.ps

The series_analysis_files_obs_init_ALL_valid_ALL_lead_ALL.txt is a text file that contains a list of the data that is included in the series analysis.
Day2 contains equivalent files for forecast leads 24 to 42.

The .nc files are the series analysis output generated from the MET Series-Analysis tool.

The .png and .ps files are graphics files that can be viewed using **display**:

.. code-block::

   display ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_lead_fhr_groupings/series_analysis_lead/Day1/series_F000_to_F018_TMP_Z2_FBAR.png &amp;

**or **

.. code-block::

   display ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_lead_fhr_groupings/series_analysis_lead/Day1/series_F000_to_F018_TMP_Z2_FBAR.ps &amp;

.. note::

   Note: the &amp; is used to run this command in the background

The series_animate directory contains the gif images of the animations:

.. code-block::

   ls ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_lead_fhr_groupings/series_analysis_lead/series_animate

.. admonition:: Sample Output

   series_animate_TMP_Z2_FBAR.gif
   series_animate_TMP_Z2_ME.gif
   series_animate_TMP_Z2_OBAR.gif
   series_animate_TMP_Z2_TOTAL.gif

To watch the animations, go to **${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_lead_fhr_groupings/series_analysis_lead/series_animate**, enter the following (if *firefox* doesn't work you can use *animate* instead):

.. code-block::

   cd ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_lead_fhr_groupings/series_analysis_lead/series_animate

.. code-block::

   firefox ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_lead_fhr_groupings/series_analysis_lead/series_animate/series_animate_TMP_Z2_FBAR.gif

.. code-block::

   firefox ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_lead_fhr_groupings/series_analysis_lead/series_animate/series_animate_TMP_Z2_ME.gif

.. code-block::

   firefox ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_lead_fhr_groupings/series_analysis_lead/series_animate/series_animate_TMP_Z2_OBAR.gif

Review the Log File
^^^^^^^^^^^^^^^^^^^

A log file is generated in your logging directory: **${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_lead_fhr_groupings/logs**. The filename contains the timestamp corresponding to the current day. To view the log file:

.. code-block::

   ls ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_lead_fhr_groupings/logs/metplus.log.*

Review the Final Configuration File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The final configuration file is **metplus_final.confYYYYMMDDHHMMSS**. (where YYYYMMDDHHMMSS refers to year, month, day, hour, minute, second that the file was created.)This contains all of the configuration variables used in the run.

.. code-block::

   less $(ls -t ${METPLUS_TUTORIAL_DIR}/output/feature_relative_by_lead_fhr_groupings/metplus_final.conf* | head -1)


End of Session 7
================

End of Session 7

End of Session 7
----------------

Congratulations! You have completed Session 7!


