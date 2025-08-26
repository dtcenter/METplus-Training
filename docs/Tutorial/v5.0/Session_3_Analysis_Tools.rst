Session 3: Analysis Tools
=========================

**METplus Practical Session 3**

During this practical session, you will run the tools indicated below:
You may navigate through this tutorial by following the links at the bottom of each page or by using the menu navigation.
Since you already set up your runtime enviroment in Session 1, you should be ready to go! To be sure, run through the following instructions to check that your environment is set correctly.

**Prerequisites: Verify Environment is Set Correctly**

Before running the tutorial instructions, you will need to ensure that you have a few environment variables set up correctly. If they are not set correctly, the tutorial instructions will not work properly.

.. note::

  **1:** Navigate to your tutorial directory and run the tutorial setup script.

.. important::

  &lt;strong&gt;In the following instructions, change "/path/to" to the directory you chose.&lt;p&gt;&lt;/p&gt;
  &lt;/strong&gt;&lt;p&gt;**EDIT AFTER COPYING and BEFORE HITTING RETURN!**&lt;/p&gt;

.. code-block::

  cd /path/to/METplus-5.0.0_Tutorial&lt;br/&gt;
  source METplus-5.0.0_TutorialSetup.sh

.. note::

  **2:** Check that you have environment variables set correctly. If any of these variables are not set, navigate back to the METplus Setup section of the tutorial.

.. code-block::

  echo ${METPLUS_TUTORIAL_DIR}&lt;br/&gt;
  echo ${METPLUS_BUILD_BASE}&lt;br/&gt;
  echo ${MET_BUILD_BASE}&lt;br/&gt;
  echo ${METPLUS_DATA}&lt;br/&gt;
  ls ${METPLUS_TUTORIAL_DIR}&lt;br/&gt;
  ls ${METPLUS_BUILD_BASE}&lt;br/&gt;
  ls ${MET_BUILD_BASE}&lt;br/&gt;
  ls ${METPLUS_DATA}

.. important::

  **METPLUS_TUTORIAL_DIR** is the location of all of your tutorial work, including configuration files, output data, and any other notes you'd like to keep.&lt;br/&gt;
  **METPLUS_BUILD_BASE** is the full path to the METplus installation (/path/to/METplus-X.Y)&lt;br/&gt;
  **MET_BUILD_BASE** is the full path to the MET installation (/path/to/met-X.Y)&lt;br/&gt;
  **METPLUS_DATA** is the location of the sample test data directory

.. note::

  **3:** Check that the MET applications are in the path:

.. code-block::

  which point_stat

.. important::

  You should see the usage statement for Point-Stat. The version number listed should correspond to the version listed in **MET_BUILD_BASE**. If it does not, you will need to either reload the met module, or add **${MET_BUILD_BASE}/bin** to your PATH.

.. note::

  **4:** Check that the correct version of **run_metplus.py** is in your **PATH**:

.. code-block::

  which run_metplus.py

.. important::

  If you don't see the full path to script from the shared installation, please set it. It should look the same as the output from this command:

.. code-block::

  echo ${METPLUS_BUILD_BASE}/ush/run_metplus.py&lt;br/&gt;
  ls ${METPLUS_BUILD_BASE}/ush/run_metplus.py

See the instructions in Session 1 for more information.
You are now ready to move on to the next section.

.. important::

  If you discover any typos, error in the run commands, incorrect output listed, or any other issues while completing the tutorial, you are encouraged to submit your findings to the METplus team in a `GitHub Discussion <https://github.com/dtcenter/METplus/discussions>`_. Be sure to provide what session and specific page you encountered the issue on.


MET Tool: Stat-Analysis
-----------------------

**STAT-ANALYSIS FUNCTIONALITY**

The Stat-Analysis tool reads the ASCII output files from the Point-Stat, Grid-Stat, Wavelet-Stat, and Ensemble-Stat tools. It provides a way to filter their STAT data and summarize the statistical information they contain. If you pass it the name of a directory, Stat-Analysis searches that directory recursively and reads any .stat files it finds. Alternatively, if you pass it an explicit file name, it'll read the contents of the file regardless of the suffix, enabling it to the optional _LINE_TYPE.txt files. Stat-Analysis runs one or more analysis jobs on the input data. It can be run by specifying a single analysis job on the command line or multiple analysis jobs using a configuration file. The analysis job types are summarized below:

The filter job simply filters out lines from one or more STAT files that meet the filtering options specified.
The summary job operates on one column of data from a single STAT line type. It produces summary information for that column of data: mean, standard deviation, min, max, and the 10th, 25th, 50th, 75th, and 90th percentiles.
The aggregate job aggregates STAT data across multiple time steps or masking regions. For example, it can be used to sum contingency table data or partial sums across multiple lines of data. The -line_type argument specifies the line type to be summed.
The aggregate_stat job also aggregates STAT data, like the aggregate job above, but then derives statistics from that aggregated STAT data. For example, it can be used to sum contingency table data and then write out a line of the corresponding contingency table statistics. The -line_type and -out_line_type arguments are used to specify the conversion type.
The ss_index job computes a skill-score index, of which the GO Index (go_index) is a special case. The GO Index is a performance metric used primarily by the United States Air Force.
The ramp job processes a time series of data and identifies rapid changes in the forecast and observation values. These forecast and observed ramp events are used populate a 2x2 contingency table from which categorical statistics are derived.

**STAT-ANALYSIS USAGE**

View the usage statement for Stat-Analysis by simply typing the following:

.. code-block::

  stat_analysis

Usage: stat_analysis

-lookin path
Space-separated list of input paths where each is a _TYPE.txt file, STAT file, or directory which should be searched recursively for STAT files. Allows the use of wildcards (required).

[-out filename]
Output path or specific filename to which output should be written rather than the screen (optional).

[-tmp_dir path]
Override the default temporary directory to be used (optional).

[-log file]
Outputs log messages to the specified file

[-v level]
Level of logging

[-config config_file] | [JOB COMMAND LINE] (Note: "|" means "or")

[-config config_file]
STATAnalysis config file containing Stat-Analysis jobs to be run.

[JOB COMMAND LINE]
All the arguments necessary to perform a single Stat-Analysis job. See the MET Users Guide for complete description of options.

At a minimum, you must specify at least one directory or file in which to find STAT data (using the -lookin path command line option) and either a configuration file (using the -config config_file command line option) or a job command on the command line.


Configure
^^^^^^^^^

.. note::

  Start by making an output directory for Stat-Analysis and changing directories:

.. code-block::

  mkdir -p ${METPLUS_TUTORIAL_DIR}/output/met_output/stat_analysis&lt;br/&gt;
  cd ${METPLUS_TUTORIAL_DIR}/output/met_output/stat_analysis



The behavior of Stat-Analysis is controlled by the contents of the configuration file or the job command passed to it on the command line. The default Stat-Analysis configuration may be found in the data/config/StatAnalysisConfig_default file.

.. note::

  Copy the default configuration file into your working directory and rename it:



.. code-block::

  cp ${MET_BUILD_BASE}/share/met/config/STATAnalysisConfig_default STATAnalysisConfig_tutorial



.. note::

  Open up the **STATAnalysisConfig_tutorial** file for editing with your preferred text editor.



.. code-block::

  vi STATAnalysisConfig_tutorial



You will see that most options are left blank, so the tool will use whatever it finds or whatever is specified in the command or job line.  If you go down to the jobs[] section you will see a list of the jobs run for the test scripts.
.. note::

Remove those existing jobs and add the following 2 analysis jobs:



.. admonition:: Sample Output

  jobs = [&lt;br/&gt;
  "-job aggregate -line_type CTC -fcst_thresh &amp;gt;273.0 -vx_mask FULL -interp_mthd NEAREST",&lt;br/&gt;
  "-job aggregate_stat -line_type CTC -out_line_type CTS -fcst_thresh &amp;gt;273.0 -vx_mask FULL -interp_mthd NEAREST"&lt;br/&gt;
  ];



The first job listed above will select out only the contingency table count lines (CTC) where the threshold applied is &gt;273.0 over the FULL masking region. This should result in 2 lines, one for pressure levels P850-500 and one for pressure P1050-850. So this job will be aggregating contingency table counts across vertical levels.
The second job listed above will perform the same aggregation as the first. However, it'll dump out the corresponding contingency table statistics derived from the aggregated counts.

  .. note::

  Close the file and run it on the next page.

Run on Point-Stat Output
^^^^^^^^^^^^^^^^^^^^^^^^

.. note::

  Now, run Stat-Analysis on the command line using the following command:



.. code-block::

  stat_analysis \&lt;br/&gt;
  -config STATAnalysisConfig_tutorial \&lt;br/&gt;
  -lookin ../point_stat \&lt;br/&gt;
  -v 2





The output for these two jobs are printed to the screen.

.. note::

  Try redirecting their output to a file by adding the **-out** command line argument:

.. code-block::

  stat_analysis \&lt;br/&gt;
  -config STATAnalysisConfig_tutorial \&lt;br/&gt;
  -lookin ../point_stat \&lt;br/&gt;
  -v 2 \&lt;br/&gt;
  -out aggr_ctc_lines.out

The output was written to aggr_ctc_lines.out. We'll look at this file in the next section.

.. note::

  Next, try running the first job again, but entirely on the command line without a configuration file:



.. code-block::

  stat_analysis \&lt;br/&gt;
  -lookin ../point_stat \&lt;br/&gt;
  -v 2 \&lt;br/&gt;
  -job aggregate \&lt;br/&gt;
  -line_type CTC \&lt;br/&gt;
  -fcst_thresh "&amp;gt;273.0" \&lt;br/&gt;
  -vx_mask FULL \&lt;br/&gt;
  -interp_mthd NEAREST


Note that we had to put double quotes (") around the forecast theshold string for this to work.

.. note::

  Next, run the same command but add the **-dump_row** command line option. This will redirect all of the STAT lines used by the job to a file. Also, add the **&lt;em&gt;-out_stat&lt;/em&gt;** command line option. This will write a full STAT output file, including the 22 header columns:



.. code-block::

  stat_analysis \&lt;br/&gt;
  -lookin ../point_stat \&lt;br/&gt;
  -v 2 \&lt;br/&gt;
  -job aggregate \&lt;br/&gt;
  -line_type CTC \&lt;br/&gt;
  -fcst_thresh "&amp;gt;273.0" \&lt;br/&gt;
  -vx_mask FULL \&lt;br/&gt;
  -interp_mthd NEAREST \&lt;br/&gt;
  -dump_row aggr_ctc_job.stat \&lt;br/&gt;
  -out_stat aggr_ctc_job_out.stat


.. note::

  Open up the file **aggr_ctc_job.stat** to see the 2 STAT lines used by this job.



.. code-block::

  vi aggr_ctc_job.stat

.. note::

  Open up the file **aggr_ctc_job_out.stat** to see the 1 output STAT line. Notice that the **FCST_LEV** and **OBS_LEV** columns contain the input strings concatenated together.

.. code-block::

  vi aggr_ctc_job_out.stat

.. note::

  Try re-running this job using **-set_hdr FCST_LEV P1050-500** and **-set_hdr OBS_LEV P1050-500**. How does that affect the output?

.. important::

  The use of the **-dump_row** option is **highly recommended** to ensure that your analysis jobs run on the exact set of data that you intended. It's easy to make mistakes here!

Output
^^^^^^

On the previous page, we generated the output file aggr_ctc_lines.out by using the -out command line argument.
.. note::

Open that file using the text editor of your choice, and be sure to turn word-wrapping off.



This file contains the output for the two jobs we ran through the configuration file. The output for each job consists of 3 lines as follows:

The JOB_LIST line contains the job filtering parameters applied for this job.
The COL_NAME line contains the column names for the data to follow in the next line.
The third line consists of the line type generated (CTC and CTS in this case) followed by the values computed for that line type.

.. note::

  Next, try running the Stat-Analysis tool on the output file **../point_stat/point_stat_run2_360000L_20070331_120000V.stat**. Start by running the following job:

.. code-block::

  stat_analysis \&lt;br/&gt;
  -lookin ../point_stat/point_stat_run2_360000L_20070331_120000V.stat \&lt;br/&gt;
  -v 2 \&lt;br/&gt;
  -job aggregate \&lt;br/&gt;
  -fcst_var TMP \&lt;br/&gt;
  -fcst_lev Z2 \&lt;br/&gt;
  -vx_mask EAST -vx_mask WEST \&lt;br/&gt;
  -interp_pnts 1 \&lt;br/&gt;
  -line_type CTC \&lt;br/&gt;
  -fcst_thresh "&amp;gt;278.0"

This job should aggregate 2 CTC lines for 2-meter temperature across the EAST and WEST regions.

.. note::

Next, try creating your own Stat-Analysis command line jobs to do the following:

.. note::

  Do the same aggregation as above but for the 5x5 interpolation output (i.e. 25 points instead of 1 point).

.. note::

  Do the aggregation listed in (1) but compute the corresponding contingency table statistics (CTS) line. Hint: you will need to change the job type to **aggregate_stat** and specify the desired **-out_line_type**.
How do the scores change when you increase the number of interpolation points? Did you expect this?

.. note::

  Aggregate the scalar partial sums lines (SL1L2) for 2-meter temperature across the EAST and WEST masking regions. How does aggregating the East and West domains affect the output?

.. note::

  Do the aggregation listed in (3) but compute the corresponding continuous statistics (CNT) line. Hint: use the **aggregate_stat** job type.

.. note::

  Run an **aggregate_stat** job directly on the matched pair data (MPR lines), and use the **-out_line_type** command line argument to select the type of output to be generated. You'll likely have to supply additional command line arguments depending on what computation you request.

.. note::

  Now answer this question about this Stat-Analysis output:

How do the scores compare to the original (separated by level) scores? What information is gained by aggregating the statistics?

.. important::

  When doing the exercises above, don't forget to use the **-dump_row** command line option to verify that you're running the job over the STAT lines you intended.

.. important::

  If you get stuck on any of these exercises, you may refer to the exercise answers on the next page. We will return to the Stat-Analysis tool in the future practical sessions.

Exercise Answers
^^^^^^^^^^^^^^^^

Job Number 1:

.. code-block::

  stat_analysis \&lt;br/&gt;
  -lookin ../point_stat/point_stat_run2_360000L_20070331_120000V.stat -v 2 \&lt;br/&gt;
  -job aggregate -fcst_var TMP -fcst_lev Z2 -vx_mask EAST -vx_mask WEST -interp_pnts 25 -fcst_thresh "&amp;gt;278.0" \&lt;br/&gt;
  -line_type CTC \&lt;br/&gt;
  -dump_row job1_ps.stat

Job Number 2:

.. code-block::

  stat_analysis \&lt;br/&gt;
  -lookin ../point_stat/point_stat_run2_360000L_20070331_120000V.stat -v 2 \&lt;br/&gt;
  -job aggregate_stat -fcst_var TMP -fcst_lev Z2 -vx_mask EAST -vx_mask WEST -interp_pnts 25 -fcst_thresh "&amp;gt;278.0" \&lt;br/&gt;
  -line_type CTC -out_line_type CTS \&lt;br/&gt;
  -dump_row job2_ps.stat

Job Number 3:

.. code-block::

  stat_analysis \&lt;br/&gt;
  -lookin ../point_stat/point_stat_run2_360000L_20070331_120000V.stat -v 2 \&lt;br/&gt;
  -job aggregate -fcst_var TMP -fcst_lev Z2 -vx_mask EAST -vx_mask WEST -interp_pnts 25 \&lt;br/&gt;
  -line_type SL1L2 \&lt;br/&gt;
  -dump_row job3_ps.stat

Job Number 4:

.. code-block::

  stat_analysis \&lt;br/&gt;
  -lookin ../point_stat/point_stat_run2_360000L_20070331_120000V.stat -v 2 \&lt;br/&gt;
  -job aggregate_stat -fcst_var TMP -fcst_lev Z2 -vx_mask EAST -vx_mask WEST -interp_pnts 25 \&lt;br/&gt;
  -line_type SL1L2 -out_line_type CNT \&lt;br/&gt;
  -dump_row job4_ps.stat

This MPR job recomputes contingency table statistics for 2-meter temperature over G212 using a new threshold of "&gt;=285":

.. code-block::

  stat_analysis \&lt;br/&gt;
  -lookin ../point_stat/point_stat_run2_360000L_20070331_120000V.stat -v 2 \&lt;br/&gt;
  -job aggregate_stat -fcst_var TMP -fcst_lev Z2 -vx_mask G212 -interp_pnts 25 \&lt;br/&gt;
  -line_type MPR -out_line_type CTS \&lt;br/&gt;
  -out_fcst_thresh ge285 -out_obs_thresh ge285 \&lt;br/&gt;
  -dump_row job5_ps.stat

METplus Use Case: StatAnalysis
------------------------------

.. important::

IMPORTANT NOTE: If you are returning to the tutorial, you must source the tutorial setup script before running the following instructions. If you are unsure if you have done this step, please navigate to the :ref:`Verify Environment is Set Correctly <verif_env_set_correct>` page.

The StatAnalysis use case utilizes the MET Stat-Analysis tool.

Optional: Refer to the `MET Users Guide <https://metplus.readthedocs.io/en/main_v5.1/Users_Guide/index.html>`_ for a description of the MET tools used in this use case.

Optional: Refer to the `METplus Config Glossary <https://metplus.readthedocs.io/en/main_v5.1/Users_Guide/glossary.html>`_ section of the METplus Users Guide for a reference to METplus variables used in this use case.

.. note::

  Change to the ${METPLUS_TUTORIAL_DIR}

.. code-block::

  cd ${METPLUS_TUTORIAL_DIR}

Review the use case configuration file: StatAnalysis.conf

In this use-case, Stat-Analysis is performing a simple filtering job and writing the data out to a .stat file using dump_row.

.. code-block::

  less ${METPLUS_BUILD_BASE}/parm/use_cases/met_tool_wrapper/StatAnalysis/StatAnalysis.conf

.. admonition:: Sample Output

  STAT_ANALYSIS_JOB1 = -job filter -dump_row [dump_row_file]

Note: Several of the optional variables may be set to further stratify of the results. LOOP_LIST_ITEMS needs to have at least 1 entry for the use-case to run.

.. admonition:: Sample Output

  MODEL_LIST = {MODEL1}&lt;br/&gt;
  DESC_LIST =&lt;br/&gt;
  FCST_LEAD_LIST =&lt;br/&gt;
  OBS_LEAD_LIST =&lt;br/&gt;
  FCST_VALID_HOUR_LIST = 12&lt;br/&gt;
  FCST_INIT_HOUR_LIST = 00, 12&lt;br/&gt;
  ...&lt;br/&gt;
  FCST_VAR_LIST = TMP&lt;br/&gt;
  ...&lt;br/&gt;
  GROUP_LIST_ITEMS = FCST_INIT_HOUR_LIST&lt;br/&gt;
  LOOP_LIST_ITEMS = FCST_VALID_HOUR_LIST, MODEL_LIST

Also note: This example uses test output from the grid_stat tool

.. admonition:: Sample Output

  MODEL1_STAT_ANALYSIS_LOOKIN_DIR = {INPUT_BASE}/met_test/out/grid_stat

Run the use case:

  .. code-block::

  run_metplus.py \&lt;br/&gt;
  ${METPLUS_BUILD_BASE}/parm/use_cases/met_tool_wrapper/StatAnalysis/StatAnalysis.conf \&lt;br/&gt;
  ${METPLUS_TUTORIAL_DIR}/tutorial.conf \&lt;br/&gt;
  config.OUTPUT_BASE=${METPLUS_TUTORIAL_DIR}/output/StatAnalysis

Review the output files: 


The following output file should been generated:

.. code-block::

  vi ${METPLUS_TUTORIAL_DIR}/output/StatAnalysis/stat_analysis/12Z/WRF/WRF_2005080712.stat

You will see there are many line types, verification masks, interpolation methods, and thresholds in the filtered file. NOTE: use ":" then "set nowrap" to be able to easily see the full line
If you look at the log file in ${METPLUS_TUTORIAL_DIR}/output/StatAnalysis/logs, you will see the how the Stat-Analysis command is built and what jobs it is processing. If you want to re-run, you can copy the call to stat_analysis and the path to the -lookin file after the "COMMAND:" (excluding the -config argument) and then everything after -job after "DEBUG 2: Processing Job 1:"

.. admonition:: Sample Output

  COMMAND: /usr/local/met-10.0.0/bin/stat_analysis -lookin /d1/projects/METplus/METplus_Data/met_test/out/grid_stat -config /usr/local/METplus-4.0.0/parm/met_config/STATAnalysisConfig_wrapped&lt;br/&gt;
  OUTPUT: DEBUG 1: Default Config File: /usr/local/met-10.0.0/share/met/config/STATAnalysisConfig_default&lt;br/&gt;
  DEBUG 1: User Config File: /usr/local/METplus-4.0.0/parm/met_config/STATAnalysisConfig_wrapped&lt;br/&gt;
  DEBUG 2: Processing 4 STAT files.&lt;br/&gt;
  DEBUG 2: STAT Lines read = 858&lt;br/&gt;
  DEBUG 2: STAT Lines retained = 136&lt;br/&gt;
  DEBUG 2:&lt;br/&gt;
  DEBUG 2: Processing Job 1: -job filter -model WRF -fcst_valid_beg 20050807_120000 -fcst_valid_end 20050807_120000 -fcst_valid_hour 120000 -fcst_init_hour 000000 -fcst_init_hour 120000 -fcst_var TMP -obtype ANALYS -dump_row /d1/personal/jensen/tutorial/METplus-4.0.0_Tutorial/output/StatAnalysis/stat_analysis/12Z/WRF/WRF_2005080712.stat




Copy METplus config file to aggregate statistics, and re-run

.. code-block::

  cp ${METPLUS_BUILD_BASE}/parm/use_cases/met_tool_wrapper/StatAnalysis/StatAnalysis.conf \&lt;br/&gt;
  ${METPLUS_TUTORIAL_DIR}/user_config/StatAnalysis_run2.conf

.. code-block::

  vi ${METPLUS_TUTORIAL_DIR}/user_config/StatAnalysis_run2.conf

.. note::

  Change **STAT_ANALYSIS_JOB1**, **VX_MASK_LIST**, and **OBS_THRESH_LIST** to compute (aggregate) statistics over two masking regions for two thresholds

.. admonition:: Sample Output

  STAT_ANALYSIS_JOB1 = -job aggregate_stat -line_type CTC -out_line_type CTS&lt;br/&gt;
  VX_MASK_LIST = DTC165, DTC166&lt;br/&gt;
  OBS_THRESH_LIST = &amp;gt;=300,&amp;lt;300&lt;br/&gt;
  LOOP_LIST_ITEMS = FCST_VALID_HOUR_LIST, MODEL_LIST, OBS_THRESH_LIS

.. note::

  Also comment out the **STAT_ANALYSIS_OUTPUT_TEMPLATE** value to prevent the -out argument from being added to the command.

.. note::

  #STAT_ANALYSIS_OUTPUT_TEMPLATE = job.out

.. code-block::

  run_metplus.py \&lt;br/&gt;
  ${METPLUS_TUTORIAL_DIR}/user_config/StatAnalysis_run2.conf \&lt;br/&gt;
  ${METPLUS_TUTORIAL_DIR}/tutorial.conf \&lt;br/&gt;
  config.OUTPUT_BASE=${METPLUS_TUTORIAL_DIR}/output/StatAnalysis_run2

Review Directory and Log File

.. note::

  Let's review the output in the directory

.. code-block::

  ls ${METPLUS_TUTORIAL_DIR}/output/StatAnalysis_run2

Which returns something that looks like the following:

.. admonition:: Sample Output

  logs     metplus_final.conf.YYYYMMDDHHMMSS     tmp

Why is there no stat_analysis directory? Because we removed the -dump_row flag from the STAT_ANALYSIS_JOB_ARGS line and removed the STAT_ANALYSIS_OUTPUT_TEMPLATE value. So did anything happen? The answer is yes. There is a command line option called "-out" controlled by STAT_ANALYSIS_OUTPUT_TEMPLATE which allows a user to define the name of an output filename to capture the aggregation in a file. If the "-out" option is not set, the output is written to the screen as standard output. Let's check the log file in ${METPLUS_TUTORIAL_DIR}/output/StatAnalysis_run2/logs to see if the output is captured there.

.. note::

  Search on "Computing" and it will take you to this:

.. admonition:: Sample Output

  JOB_LIST: -job aggregate_stat -model WRF -fcst_valid_beg 20050807_120000 -fcst_valid_end&lt;br/&gt;
  20050807_120000 -fcst_valid_hour 120000 -fcst_init_hour 000000 -fcst_init_hour 120000 -fcst_var TMP -obtype ANALYS&lt;br/&gt;
  -vx_mask DTC165 -vx_mask DTC166 -obs_thresh &amp;gt;=300 -line_type CTC -out_line_type CTS -out_alpha 0.05000&lt;br/&gt;
  DEBUG 2: Computing output for 1 case(s).&lt;br/&gt;
  DEBUG 2: For case "", found 2 unique VX_MASK values: DTC165,DTC166&lt;br/&gt;
  COL_NAME: TOTAL BASER BASER_NCL BASER_NCU BASER_BCL BASER_BCU FMEAN FMEAN_NCL FMEAN_NCU FMEAN_BCL FMEAN_BCU ACC ACC_NCL ACC_NCU ACC_BCL ACC_BCU FBIAS FBIAS_BCL FBIAS_BCU PODY PODY_NCL PODY_NCU PODY_BCL PODY_BCU PODN PODN_NCL PODN_NCU PODN_BCL PODN_BCU POFD POFD_NCL POFD_NCU POFD_BCL POFD_BCU FAR FAR_NCL FAR_NCU FAR_BCL FAR_BCU CSI CSI_NCL CSI_NCU CSI_BCL CSI_BCU GSS GSS_BCL GSS_BCU HK HK_NCL HK_NCU HK_BCL HK_BCU HSS HSS_BCL HSS_BCU ODDS ODDS_NCL ODDS_NCU ODDS_BCL ODDS_BCU LODDS LODDS_NCL LODDS_NCU LODDS_BCL LODDS_BCU ORSS ORSS_NCL ORSS_NCU ORSS_BCL ORSS_BCU EDS EDS_NCL EDS_NCU EDS_BCL EDS_BCU SEDS SEDS_NCL SEDS_NCU SEDS_BCL SEDS_BCU EDI EDI_NCL EDI_NCU EDI_BCL EDI_BCU SEDI SEDI_NCL SEDI_NCU SEDI_BCL SEDI_BCU BAGSS BAGSS_BCL BAGSS_BCU CTS: 12420 0.11715 0.11161 0.12292 NA NA 0.14509 0.139 0.15139 NA NA 0.96063 0.95706 0.96391 NA NA 1.23849 NA NA 0.9512 0.94727 0.95485 NA NA 0.96188 0.95837 0.96511 NA NA 0.038121 0.034894 0.041634 NA NA 0.23196 0.22462 0.23947 NA NA 0.73892 0.73112 0.74657 NA NA 0.70576 NA NA 0.91308 0.90125 0.92491 NA NA 0.8275 NA NA 491.84743 380.09404 636.458 NA NA 6.19817 5.94042 6.45592 NA NA 0.99594 0.9949 0.99699 NA NA 0.9544 0.94404 0.96477 NA NA 0.85693 0.84708 0.86678 NA NA 0.96984 0.96086 0.97881 NA NA 0.97212 0.96147 0.9782 NA NA 0.67864 NA NA

These is the aggregate statistics computed from the summed CTC lines for the DTC165 and DTC166 masking regions for the threshold &gt;=300. If you scroll down further, you will see the same info but for the threshold &lt;300.

Have output written to .stat file

.. note::

  Edit the conf file and add an additional job called -out_stat, set the out_stat_template to the same as dump_row_template, and rerun

.. code-block::

  vi ${METPLUS_TUTORIAL_DIR}/user_config/StatAnalysis_run2.conf

.. note::

  Add the following line:

.. admonition:: Sample Output

  MODEL1_STAT_ANALYSIS_OUT_STAT_TEMPLATE = {fcst_valid_hour?fmt=%H}Z/{MODEL1}/{MODEL1}_{valid?fmt=%Y%m%d%H}.stat

.. note::

  and modify the following line:

.. admonition:: Sample Output

  STAT_ANALYSIS_JOB1 = -job aggregate_stat -line_type CTC -out_line_type CTS -out_stat [out_stat_file]

.. note::

  Now rerun the use case, writing to a new output directory StatAnalysis_run3:

.. code-block::

  run_metplus.py \&lt;br/&gt;
  ${METPLUS_TUTORIAL_DIR}/user_config/StatAnalysis_run2.conf \&lt;br/&gt;
  ${METPLUS_TUTORIAL_DIR}/tutorial.conf \&lt;br/&gt;
  config.OUTPUT_BASE=${METPLUS_TUTORIAL_DIR}/output/StatAnalysis_run3

.. note::

  Review the output:

.. code-block::

  ls ${METPLUS_TUTORIAL_DIR}/output/StatAnalysis_run3/stat_analysis/12Z/WRF

You should see the .stat file now in the stat_analysis/12Z/WRF directory

MET Tool: Series-Analysis
-------------------------

**SERIES-ANALYSIS FUNCTIONALITY**

The Series-Analysis Tool accumulates statistics separately for each horizontal grid location over a series. Usually, the series is defined as a time series, however any type of series is possible, including a series of vertical levels. This differs from the Grid-Stat tool in that Grid-Stat computes statistics aggregated over a spatial masking region at a single point in time. The Series-Analysis Tool computes statistics for each individual grid point and can be used to quantify how the model performance varies over the domain.

**SERIES-ANALYSIS USAGE**

View the usage statement for Series-Analysis by simply typing the following:

.. code-block::

  series_analysis

Usage: series_analysis

  -fcst file_1 ... file_n
  Gridded forecast files or ASCII file containing a list of file names.



  -obs file_1 ... file_n
  Gridded observation files or ASCII file containing a list of file names.



  [-both file_1 ... file_n]
  Sets the -fcst and -obs options to the same list of files
  (e.g. the NetCDF matched pairs files from Grid-Stat).



[-paired]
Indicates that the -fcst and -obs file lists are already matched up
(i.e. the n-th forecast file matches the n-th observation file).



  -out file
  NetCDF output file name for the computed statistics.



  -config file
  SeriesAnalysisConfig file containing the desired configuration settings.



  [-log file]
  Outputs log messages to the specified file



  [-v level]
  Level of logging (optional).



  [-compress level]
  NetCDF compression level (optional).



At a minimum, the -fcst, -obs (or -both), -out, and -config settings must be passed in on the command line. All forecast and observation fields must be interpolated to a common grid prior to running Series-Analysis.





Configure
^^^^^^^^^

.. note::

  Start by making an output directory for Series-Analysis and changing directories:



.. code-block::

  mkdir -p ${METPLUS_TUTORIAL_DIR}/output/met_output/series_analysis&lt;br/&gt;
  cd ${METPLUS_TUTORIAL_DIR}/output/met_output/series_analysis



The behavior of Series-Analysis is controlled by the contents of the configuration file passed to it on the command line. The default Series-Analysis configuration file may be found in the data/config/SeriesAnalysisConfig_default file.

.. note::

  Prior to modifying the configuration file, users are advised to make a copy of the default:



.. code-block::

  cp ${MET_BUILD_BASE}/share/met/config/SeriesAnalysisConfig_default SeriesAnalysisConfig_tutorial

The configurable items for Series-Analysis are used to specify how the verification is to be performed. The configurable items include specifications for the following:

The forecast fields to be verified at the specified vertical level or accumulation interval.
The threshold values to be applied.
The area over which to limit the computation of statistics - as predefined grids or configurable lat/lon polylines.
The confidence interval methods to be used.
The smoothing methods to be applied.
The types of statistics to be computed.

You may find a complete description of the configurable items in the series_analysis configuration file section of the MET User's Guide. Please take some time to review them.

.. note::

For this tutorial, we'll run Series-Analysis to verify a time series of 3-hour accumulated precipitation. We'll use GRIB1 for the forecast files and NetCDF for the observation files. Since the forecast and observations are different file formats, we'll specify the **name** and **level** information for them slightly differently.

.. note::

  Open up the **SeriesAnalysisConfig_tutorial** file for editing with your preferred text editor and edit it as follows:



.. code-block::

  vi SeriesAnalysisConfig_tutorial

.. note::

  Set the **fcst** dictionary to

.. admonition:: Sample Output

  fcst = {&lt;br/&gt;
  field = [&lt;br/&gt;
  {&lt;br/&gt;
  name  = "APCP";&lt;br/&gt;
  level = [ "A3" ];&lt;br/&gt;
  }&lt;br/&gt;
  ];&lt;br/&gt;
  }



To request the GRIB abbreviation for precipitation (APCP) accumulated over 3 hours (A3).

.. note::

  Delete **obs = fcst;** and insert



.. admonition:: Sample Output

  obs = {&lt;br/&gt;
  field = [&lt;br/&gt;
  {&lt;br/&gt;
  name  = "APCP_03";&lt;br/&gt;
  level = [ "(*,*)" ];&lt;br/&gt;
  }&lt;br/&gt;
  ];&lt;br/&gt;
  }

To request the NetCDF variable named APCP_03 where its two dimensions are the gridded dimensions (*,*).

.. note::

  Look up a few lines above the **fcst** dictionary and set

.. admonition:: Sample Output

  cat_thresh = [ &amp;gt;0.0, &amp;gt;=5.0 ];

To define the categorical thresholds of interest. By defining this at the top level of config file context, these thresholds will be applied to both the fcst and obs settings.

.. note::

  In the **mask** dictionary, set

.. admonition:: Sample Output

  grid = "G212";

To limit the computation of statistics to only those grid points falling inside the NCEP Grid 212 domain.

.. note::

  Set

.. admonition:: Sample Output

  block_size = 10000;

To process 10,000 grid points in each pass through the data. Setting block_size larger should make the tool run faster but use more memory.

.. note::

  In the **output_stats** dictionary, set

.. admonition:: Sample Output

  **   **fho    = [ "F_RATE", "O_RATE" ];&lt;br/&gt;
  ctc    = [ "FY_OY", "FN_ON" ];&lt;br/&gt;
  cts    = [ "CSI", "GSS" ];&lt;br/&gt;
  mctc   = [];&lt;br/&gt;
  mcts   = [];&lt;br/&gt;
  cnt    = [ "TOTAL", "RMSE" ];&lt;br/&gt;
  sl1l2  = [];&lt;br/&gt;
  pct    = [];&lt;br/&gt;
  pstd   = [];&lt;br/&gt;
  pjc    = [];&lt;br/&gt;
  prc    = [];

For each line type, you can select statistics to be computed at each grid point over the series. These are the column names from those line types. Here, we select the forecast rate (FHO: F_RATE), observation rate (FHO: O_RATE), number of forecast yes and observation yes (CTC: FY_OY), number of forecast no and observation no (CTC: FN_ON), critical success index (CTS: CSI), and the Gilbert Skill Score (CTS: GSS) for each threshold, along with the root mean squared error (CNT: RMSE).

.. note::

  Save and close this file.

Run
^^^

.. note::

  First, we need to prepare our observations by putting 1-hourly StageII precipitation forecasts into 3-hourly buckets. Create an output directory:

.. code-block::

  mkdir -p sample_obs/ST2ml_3h

.. note::

  Run the following PCP-Combine commands to prepare the observations:

.. code-block::

  pcp_combine -sum 00000000_000000 01 20050807_030000 03 \&lt;br/&gt;
  sample_obs/ST2ml_3h/sample_obs_2005080703V_03A.nc \&lt;br/&gt;
  -pcpdir ${METPLUS_DATA}/met_test/data/sample_obs/ST2ml

.. code-block::

  pcp_combine -sum 00000000_000000 01 20050807_060000 03 \&lt;br/&gt;
  sample_obs/ST2ml_3h/sample_obs_2005080706V_03A.nc \&lt;br/&gt;
  -pcpdir ${METPLUS_DATA}/met_test/data/sample_obs/ST2ml

.. code-block::

  pcp_combine -sum 00000000_000000 01 20050807_090000 03 \&lt;br/&gt;
  sample_obs/ST2ml_3h/sample_obs_2005080709V_03A.nc \&lt;br/&gt;
  -pcpdir ${METPLUS_DATA}/met_test/data/sample_obs/ST2ml

.. code-block::

  pcp_combine -sum 00000000_000000 01 20050807_120000 03 \&lt;br/&gt;
  sample_obs/ST2ml_3h/sample_obs_2005080712V_03A.nc \&lt;br/&gt;
  -pcpdir ${METPLUS_DATA}/met_test/data/sample_obs/ST2ml

.. code-block::

  pcp_combine -sum 00000000_000000 01 20050807_150000 03 \&lt;br/&gt;
  sample_obs/ST2ml_3h/sample_obs_2005080715V_03A.nc \&lt;br/&gt;
  -pcpdir ${METPLUS_DATA}/met_test/data/sample_obs/ST2ml

.. code-block::

  pcp_combine -sum 00000000_000000 01 20050807_180000 03 \&lt;br/&gt;
  sample_obs/ST2ml_3h/sample_obs_2005080718V_03A.nc \&lt;br/&gt;
  -pcpdir ${METPLUS_DATA}/met_test/data/sample_obs/ST2ml

.. code-block::

  pcp_combine -sum 00000000_000000 01 20050807_210000 03 \&lt;br/&gt;
  sample_obs/ST2ml_3h/sample_obs_2005080721V_03A.nc \&lt;br/&gt;
  -pcpdir ${METPLUS_DATA}/met_test/data/sample_obs/ST2ml

.. code-block::

  pcp_combine -sum 00000000_000000 01 20050808_000000 03 \&lt;br/&gt;
  sample_obs/ST2ml_3h/sample_obs_2005080800V_03A.nc \&lt;br/&gt;
  -pcpdir ${METPLUS_DATA}/met_test/data/sample_obs/ST2ml

Note that the previous set of PCP-Combine commands could easily be run by looping through times in METplus Wrappers! The MET tools are often run using METplus Wrappers rather than typing individual commands by hand. You'll learn more about automation using the METplus Wrappers throughout the tutorial.

.. note::

Next, we'll run Series-Analysis using the following command:

.. code-block::

  series_analysis \&lt;br/&gt;
  -fcst ${METPLUS_DATA}/met_test/data/sample_fcst/2005080700/wrfprs_ruc13_03.tm00_G212 \&lt;br/&gt;
  ${METPLUS_DATA}/met_test/data/sample_fcst/2005080700/wrfprs_ruc13_06.tm00_G212 \&lt;br/&gt;
  ${METPLUS_DATA}/met_test/data/sample_fcst/2005080700/wrfprs_ruc13_09.tm00_G212 \&lt;br/&gt;
  ${METPLUS_DATA}/met_test/data/sample_fcst/2005080700/wrfprs_ruc13_12.tm00_G212 \&lt;br/&gt;
  ${METPLUS_DATA}/met_test/data/sample_fcst/2005080700/wrfprs_ruc13_15.tm00_G212 \&lt;br/&gt;
  ${METPLUS_DATA}/met_test/data/sample_fcst/2005080700/wrfprs_ruc13_18.tm00_G212 \&lt;br/&gt;
  ${METPLUS_DATA}/met_test/data/sample_fcst/2005080700/wrfprs_ruc13_21.tm00_G212 \&lt;br/&gt;
  ${METPLUS_DATA}/met_test/data/sample_fcst/2005080700/wrfprs_ruc13_24.tm00_G212 \&lt;br/&gt;
  -obs sample_obs/ST2ml_3h/sample_obs_2005080703V_03A.nc \&lt;br/&gt;
  sample_obs/ST2ml_3h/sample_obs_2005080706V_03A.nc \&lt;br/&gt;
  sample_obs/ST2ml_3h/sample_obs_2005080709V_03A.nc \&lt;br/&gt;
  sample_obs/ST2ml_3h/sample_obs_2005080712V_03A.nc \&lt;br/&gt;
  sample_obs/ST2ml_3h/sample_obs_2005080715V_03A.nc \&lt;br/&gt;
  sample_obs/ST2ml_3h/sample_obs_2005080718V_03A.nc \&lt;br/&gt;
  sample_obs/ST2ml_3h/sample_obs_2005080721V_03A.nc \&lt;br/&gt;
  sample_obs/ST2ml_3h/sample_obs_2005080800V_03A.nc \&lt;br/&gt;
  -out series_analysis_2005080700_2005080800_3A.nc \&lt;br/&gt;
  -config SeriesAnalysisConfig_tutorial \&lt;br/&gt;
  -v 2

The statistics we requested in the configuration file will be computed separately for each grid location and accumulated over a time series of eight three-hour accumulations over a 24-hour period. Each grid point will have up to 8 matched pair values.
Note how long this command line is. Imagine how long it would be for a series of 100 files! Instead of listing all of the input files on the command line, you can list them in an ASCII file and pass that to Series-Analysis using the -fcst and -obs options.

Output
^^^^^^

The output of Series-Analysis is one NetCDF file containing the requested output statistics for each grid location on the same grid as the input files.
You may view the output NetCDF file that Series-Analysis wrote using the ncdump utility. Run the following command to view the header of the NetCDF output file:

.. code-block::

  ncdump -h series_analysis_2005080700_2005080800_3A.nc

In the NetCDF header, we see that the file contains many arrays of data. For each threshold (&gt;0.0 and &gt;=5.0), there are values for the requested statistics: F_RATE, O_RATE, FY_OY, FN_ON, CSI, and GSS. The file also contains the requested RMSE and TOTAL number of matched pairs for each grid location over the 24-hour period.

Next, run the ncview utility to display the contents of the NetCDF output file:

.. code-block::

  ncview series_analysis_2005080700_2005080800_3A.nc &amp;amp;

Click through the different variables to see how the performance varies over the domain. Looking at the series_cnt_RMSEvariable, are the errors larger in the south eastern or north western regions of the United States?
Why does the extent of missing data increase for CSI for the higher threshold? Compare series_cts_CSI_gt0.0 to series_cts_CSI_ge5.0. (Hint: Find the definition of Critical Success index (CSI) in the MET User's Guide and look closely at the denominator.)
Try running Plot-Data-Plane to visualize the observation rate variable for non-zero precipitation (i.e. series_fho_O_RATE_gt0.0). Since the valid range of values for this data is 0 to 1, use that to set the -plot_range option.
Setting block_size to 10000 still required 3 passes through our 185x129 grid (= 23865 grid points). What happens when you increase block_size to 24000 and re-run? Does it run slower or faster?

METplus Use Case: SeriesAnalysis
--------------------------------

.. important::

  **&lt;span&gt; &lt;/span&gt;IMPORTANT NOTE: If you are returning to the tutorial, you must source the tutorial setup script before running the following instructions. If you are unsure if you have done this step, please navigate to the &lt;a :ref:`Verify Environment is Set Correctly <verif_env_set_correct>` page.**

The SeriesAnalysis use case utilizes the MET Series-Analysis tool.

Optional: Refer to the MET Users Guide for a description of the MET tools used in this use case.

Optional: Refer to the METplus Config Glossary section of the METplus Users Guide for a reference to METplus variables used in this use case.

.. note::

  Change to the ${METPLUS_TUTORIAL_DIR}

.. code-block::

  cd ${METPLUS_TUTORIAL_DIR}

.. note::

  **Review the use case configuration file: SeriesAnalysis.conf**

.. note::

  Open the file and look at all of the configuration variables that are defined.

This use-case shows a simple example of running Series-Analysis across precipitation forecast fields at 3 different lead times. Forecast data is from WRF output, while observational data is Stage II quantitative precipitation estimates.

.. code-block::

  less ${METPLUS_BUILD_BASE}/parm/use_cases/met_tool_wrapper/SeriesAnalysis/SeriesAnalysis.conf

Note: Forecast and observation variables are referred to individually including reference to both the NAMES and LEVELS, which relate to .

.. admonition:: Sample Output

  FCST_VAR1_NAME = APCP&lt;br/&gt;
  FCST_VAR1_LEVELS = A03
  &lt;p&gt;OBS_VAR1_NAME = APCP_03&lt;br/&gt;
  OBS_VAR1_LEVELS = "(*,*)"&lt;/p&gt;

Which relates to the following fields in the MET configuration file

.. admonition:: Sample Output

  fcst = {&lt;br/&gt;
  field = [&lt;br/&gt;
  {&lt;br/&gt;
  name = "APCP";&lt;br/&gt;
  level = [ "A03" ];&lt;br/&gt;
  }&lt;br/&gt;
  ];&lt;br/&gt;
  }&lt;br/&gt;
  obs = {&lt;br/&gt;
  field = [&lt;br/&gt;
  {&lt;br/&gt;
  name = "APCP_03";&lt;br/&gt;
  level = [ "(*,*)" ];&lt;br/&gt;
  }&lt;br/&gt;
  ];&lt;br/&gt;
  }

Also note: Paths in SeriesAnalysis.conf may reference other config options defined in a different configuration files. For example:

.. admonition:: Sample Output

  FCST_SERIES_ANALYSIS_INPUT_DIR = {INPUT_BASE}/met_test/data/sample_fcst

where INPUT_BASE which is set in the tutorial.conf configuration file. METplus config variables can reference other config variables even if they are defined in a config file that is read afterwards.



.. note::

  **Run the use case:**

.. code-block::

  run_metplus.py \&lt;br/&gt;
  ${METPLUS_BUILD_BASE}/parm/use_cases/met_tool_wrapper/SeriesAnalysis/SeriesAnalysis.conf \&lt;br/&gt;
  ${METPLUS_TUTORIAL_DIR}/tutorial.conf \&lt;br/&gt;
  config.OUTPUT_BASE=${METPLUS_TUTORIAL_DIR}/output/SeriesAnalysis

METplus is finished running when control returns to your terminal console and you see the following text:
.. admonition:: Sample Output

INFO: METplus has successfully finished running.

.. note::

  **Review the output files: **

You should have output file in the following directories:

.. code-block::

  ls ${METPLUS_TUTORIAL_DIR}/output/SeriesAnalysis/met_tool_wrapper/SeriesAnalysis

.. admonition:: Sample Output

  &lt;p&gt;2005080700_sa.nc&lt;/p&gt;

.. note::

  Take a look at the contents of the netCDF to see what was generated inside the file.

.. code-block::

  ncdump -h 2005080700_sa.nc

.. admonition:: Sample Output

  &lt;p&gt;netcdf \2005080700_sa {&lt;br/&gt;
  dimensions:&lt;br/&gt;
  lat = 129 ;&lt;br/&gt;
  lon = 185 ;&lt;/p&gt;
  &lt;p&gt;variables:&lt;br/&gt;
  float lat(lat, lon) ;&lt;br/&gt;
  lat:long_name = "latitude" ;&lt;br/&gt;
  lat:units = "degrees_north" ;&lt;br/&gt;
  lat:standard_name = "latitude" ;&lt;/p&gt;
  &lt;p&gt;float lon(lat, lon) ;&lt;br/&gt;
  lon:long_name = "longitude" ;&lt;br/&gt;
  lon:units = "degrees_east" ;&lt;br/&gt;
  lon:standard_name = "longitude" ;&lt;/p&gt;
  &lt;p&gt;int n_series ;&lt;br/&gt;
  n_series:long_name = "length of series" ;&lt;/p&gt;
  &lt;p&gt;float series_cnt_TOTAL(lat, lon) ;&lt;br/&gt;
  series_cnt_TOTAL:_FillValue = -9999.f ;&lt;br/&gt;
  series_cnt_TOTAL:name = "TOTAL" ;&lt;br/&gt;
  series_cnt_TOTAL:long_name = "Total number of matched pairs" ;&lt;br/&gt;
  series_cnt_TOTAL:fcst_thresh = "NA" ;&lt;br/&gt;
  series_cnt_TOTAL:obs_thresh = "NA" ;&lt;/p&gt;
  &lt;p&gt;float series_cnt_RMSE(lat, lon) ;&lt;br/&gt;
  series_cnt_RMSE:_FillValue = -9999.f ;&lt;br/&gt;
  series_cnt_RMSE:name = "RMSE" ;&lt;br/&gt;
  series_cnt_RMSE:long_name = "Root mean squared error" ;&lt;br/&gt;
  series_cnt_RMSE:fcst_thresh = "NA" ;&lt;br/&gt;
  series_cnt_RMSE:obs_thresh = "NA" ;&lt;/p&gt;
  &lt;p&gt;float series_cnt_FBAR(lat, lon) ;&lt;br/&gt;
  series_cnt_FBAR:_FillValue = -9999.f ;&lt;br/&gt;
  series_cnt_FBAR:name = "FBAR" ;&lt;br/&gt;
  series_cnt_FBAR:long_name = "Forecast mean" ;&lt;br/&gt;
  series_cnt_FBAR:fcst_thresh = "NA" ;&lt;br/&gt;
  series_cnt_FBAR:obs_thresh = "NA" ;&lt;/p&gt;
  &lt;p&gt;float series_cnt_OBAR(lat, lon) ;&lt;br/&gt;
  series_cnt_OBAR:_FillValue = -9999.f ;&lt;br/&gt;
  series_cnt_OBAR:name = "OBAR" ;&lt;br/&gt;
  series_cnt_OBAR:long_name = "Observation mean" ;&lt;br/&gt;
  series_cnt_OBAR:fcst_thresh = "NA" ;&lt;br/&gt;
  series_cnt_OBAR:obs_thresh = "NA" ;&lt;/p&gt;

From this output, we can see CNT line type statistics: TOTAL, RMSE, FBAR, and OBAR. These correspond to what we requested from the configuration file for output:

.. admonition:: Sample Output

  SERIES_ANALYSIS_OUTPUT_STATS_CNT = TOTAL, RMSE, FBAR, OBAR

.. note::

  Let's take a look at one of these variables up close using ncview:

.. code-block::

  ncview 2005080700_sa.nc

From the GUI that pops up, select the series_cnt_RMSE variable to view it. The image that displays is the RMSE value calculated at each grid point across the three lead times selected in the METplus configuration file.

There are two more files located in the output directory that while not statistically useful, do contain information on how METplus ran the SeriesAnalysis configuration file.
FCST_FILES contains all of the files that were found fitting the input templates for the forecast files. These are controlled by FCST_SERIES_ANALYSIS_INPUT_DIR and FCST_SERIES_ANALYSIS_INPUT_TEMPLATE. In our configuration file, these are set to

.. admonition:: Sample Output

  &lt;span class="nv"&gt;FCST_SERIES_ANALYSIS_INPUT_DIR&lt;/span&gt; &lt;span class="o"&gt;=&lt;/span&gt; &lt;span class="o"&gt;{&lt;/span&gt;INPUT_BASE&lt;span     class="o"&gt;}&lt;/span&gt;/met_test/data/sample_fcst&lt;br/&gt;
  &lt;span class="nv"&gt;FCST_SERIES_ANALYSIS_INPUT_TEMPLATE&lt;/span&gt; &lt;span class="o"&gt;=&lt;/span&gt; &lt;span class="o"&gt;{&lt;/span&gt;init?fmt&lt;span class="o"&gt;=&lt;/span&gt;%Y%m%d%H&lt;span class="o"&gt;}&lt;/span&gt;/wrfprs_ruc13_&lt;span class="o"&gt;{&lt;/span&gt;lead?fmt&lt;span class="o"&gt;=&lt;/span&gt;%2H&lt;span class="o"&gt;}&lt;/span&gt;.tm00_G212

Because {INPUT_BASE} is not changing for this run and the use case uses one initialization time, the lead sequences, set with the LEAD_SEQ variable and substituted in for {lead?fmt=%2H} in FCST_SERIES_ANALYSIS_INPUT_TEMPLATE, are what causes multiple files to be found. Specifically, FCST_FILES has three listed files, matching the LEAD_SEQ list from the configuration file.

.. code-block::

  less FCST_FILES

Likewise, OBS_FILES contains all of the files that were found fitting the input templates for the observation files. These were controlled by OBS_SERIES_ANALYSIS_INPUT_DIR and OBS_SERIES_ANALYSIS_INPUT_TEMPLATE found in the configuration file.

.. note::

  **Review the log output:**

Log files for this run are found in ${METPLUS_TUTORIAL_DIR}/output/SeriesAnalysis/logs. The filename contains a timestamp of the current day.

.. code-block::

  ls -1 ${METPLUS_TUTORIAL_DIR}/output/SeriesAnalysis/logs/metplus.log.*

Inside the log file all of the configuration options are listed, as well as the command that was used to call Series-Analysis:

.. admonition:: Sample Output

  /usr/local/met-11.0.0/bin/series_analysis -fcst /d1/personal/user/output/SeriesAnalysis/met_tool_wrapper/SeriesAnalysis/FCST_FILES -obs /d1/personal/user/output/SeriesAnalysis/met_tool_wrapper/SeriesAnalysis/OBS_FILES -out /d1/personal/user/output/SeriesAnalysis/met_tool_wrapper/SeriesAnalysis/2005080700_sa.nc -config /usr/local/METplus-4.0.0/parm/met_config/SeriesAnalysisConfig_wrapped -v 2

Note that FCST_FILES and OBS_FILES were passed at runtime, rather than individual files.
There's also room for improvement noted in the low level verbosity comments of the log file:

.. admonition:: Sample Output

  DEBUG 2: Computing statistics using a block size of 1024, requiring 24 pass(es) through the 185 x 129 grid.&lt;br/&gt;
  WARNING:&lt;br/&gt;
  WARNING: A block size of 1024 for a 185 x 129 grid requires 24 passes through the data which will be slow.&lt;br/&gt;
  WARNING: Consider increasing "block_size" in the configuration file based on available memory.&lt;br/&gt;
  WARNING:

This is a result of not setting the SERIES_ANALYSIS_BLOCK_SIZE in the METplus configuration file, which then defaults to the MET_INSTALL_DIR/share/met/config/SeriesAnalysisConfig_default value of 1024.   

.. note::

  **Create imagery for a variable in the netCDF output**

While ncview was used to review the statistical imagery created by SeriesAnalysis, there is always the option to create an image using the Plot-Data-Plane tool. These images can be easily shared with others and used to demonstrate output in a presentation.
Use the following command to generate an image of the RMSE:

.. code-block::

  plot_data_plane \&lt;br/&gt;
  ${METPLUS_TUTORIAL_DIR}/output/SeriesAnalysis/met_tool_wrapper/SeriesAnalysis/2005080700_sa.nc \&lt;br/&gt;
  ${METPLUS_TUTORIAL_DIR}/output/SeriesAnalysis/met_tool_wrapper/SeriesAnalysis/2005080700_RMSE.ps \&lt;br/&gt;
  'name="series_cnt_RMSE"; level="(*,*)";'

The successful run of that command should produce an image. view it with the following command:

.. code-block::

  display ${METPLUS_TUTORIAL_DIR}/output/SeriesAnalysis/met_tool_wrapper/SeriesAnalysis/2005080700_RMSE.ps

End of Session 3
----------------

Congratulations! You have completed Session 3!
