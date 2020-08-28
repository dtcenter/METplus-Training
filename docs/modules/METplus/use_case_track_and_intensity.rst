.. _metplus_use_case_track_and_intensity:

Track and Intensity Use Case
============================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/KCISG0phmbw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 3.1**.

(*Introduction*)

If you would like to follow along with the exercises in this video, please select one of the options to set up your own :ref:`Training Environment <training_environment>`.

This video describes the track and intensity use case that involves the TCMPR (tropical cyclone matched pair) plotter ( **WEB BROWSER** *Begin with view of this section of the tutorial in the web browser* ). 

Before you proceed, make sure you have run the tutorial from `Session 5: TC-Pairs Tool <https://dtcenter.org/metplus-practical-session-guide-version-3-0/session-5-trkintfeature-relative>`_ and have saved all corresponding output.( **WEB BROWSER** *Show web page of tutorial pointing to this* )

The TCMPR plotter wraps the plot_tcmpr.R, the R plotting script that is part of your MET installation.( **WEB BROWSER** *highlight github MET repo*) 

If you want to familiarize yourself with plot_tcmpr.R, refer to the TC-Stat tool example in the MET User’s Guide. ( **WEB BROWSER** *Show web page of MET user's guide to TC-Stat tool* ) 

If you haven’t already done so, you can also follow Session 5 of the tutorial: Trk&Int/Feature Relative >MET Tool: TC-STAT. ( **WEB BROWSER** *Show web page of tutorial for TC-Stat section*).   

This use case uses output from the MET tc-pairs tool.  You can refer to section 20.2.3 of the MET Users Guide for a description of the tc-pairs output format. ( **WEB BROWSER** *Go to web browser with MET User's guide web page* ).

The TCMPR plotter wrapper makes use of three configuration files (in addition to the other default METplus configuration files described in Session 1: METplus Setup/Directories and Configurations files- Overview).  

These configuration files are: TCMPRPlotterConfig_Customize, TCMPRPlotter.conf, and track_and_intensity.output.conf. track_and_intensity_output.conf is a custom configuration file that you will create, that is why it doesn't appear in this directory (XTERM *highlight these files in your directory*). 

The TCMPRPlotterConfig_Customize file is used by MET’s R script that generates the plot, and is used to set attributes of the plot.  

The TCMPRPlotter.conf file is a default configuration file that encapsulates common settings.  

It is located in the parm/use_cases/met_tool_wrapper/TCMPRPlotter directory of your METPlus directory.  

You can override the following values (WEB BROWSER *point to/mouse third blue box*) that are defined in the TCMPRPlotter.conf file by defining these in the custom config file, track_and_intensity.output.conf. 

The settings in the TCMPRPlotter.conf file and track_and_intensity.output.conf file are used by the METplus wrapper to run MET’s R plotting script.  

Before we proceed, let’s look at the  TCMPRPlotterConfig_Customize.conf file, which is used by the R script to set plot attributes.  (**XTERM** *open the TCMPRPlotterConfig_Customize.conf file*)

When you open the file, you can see that it has only one key-value setting, img_res = 72. This value dictates the image size of the plot that is created.  If this value is left unset (that is, set to nothing), the R script plot_tcmpr.R will use the default value of 300. This value results in an extremely large plot in your display.  The default value is also used if this configuration file is omitted/non-existent.

(**WEB BROWSER**)
Let’s begin by setting up the use case.  For the next steps, make sure you are working out of the METplus Tutorial directory.  Create a unique output directory where you want to save the use case output files.  

Open the custom configuration file called track_and_intensity.output.conf and set the OUTPUT_BASE value with the path to the output directory you just created. (**WEB BROWSER** *point to/mouse to the first blue box with the example*) 

Now set the INPUT_BASE to the full path corresponding to the output directory from the TC-Pairs Tool tutorial (this is the directory that contains your tc_pairs.tcst file). Close the file. 

(**XTERM**)
Unassigned settings under the [config] section corresponding to the plot_tcmpr.R options will use default values that are established in the plot_tcmpr.R script.

You can take a moment to look at what is defined in the parm/use_cases/met_tool_wrapper/TCMPRPlotter/TCMPRPlotter.conf, under the [config] section. 
( **XTERM** *open this file* ) 

Sections are indicated with the section name, surrounded by square brackets.( **XTERM** *highlight the [config] header*) 

The plotting settings of interest will begin with ‘TCMPR_PLOTTER’, followed by a descriptive name (**XTERM** *scroll down to TCMPR_PLOTTER section*)

For example TCMPR_PLOTTER_TITLE sets the title of the plot (**XTERM** *highlight TCMPR_PLOTTER_TITLE*).  

The settings from the default and configuration files will allow you to generate a boxplot and plots of the mean and median for the A- and B-track MSLP, the A- and B-track maximum wind, and the track errors(**XTERM** *scroll down to TCMPR_PLOTTER_DEP_VARS and highlight the MSLP, MAX_WIND, TK_ERR*) .

(**WEB BROWSER** *go to Example 1*)
Now you are ready to run the track and intensity use case. We will read in the .tcst files as input to the plot_tcmpr.R script, and create static image files with a ‘.png’ extension.

From the command line, run the master_metplus.py command in the dark grey box:

(**WEB BROWSER** *mouse over/point to the command line command in the dark grey box under Example 1*)  

You should observe the following output in the output directory you created:

(**WEB BROWSER** *mouse over/point to the output in the blue box below the dark grey box*)

The plot filenames are comprised of the dependent variable name from the TCMPR_PLOTTER_DEP_VARS setting and the plot type from the TCMPR_PLOTTER_PLOT_TYPES setting (**XTERM** *open TCMPRPlotter.conf and highlight TCMPR_PLOTTER_DEP_VARS and TCMPR_PLOTTER_PLOT_TYPES*)

You can use the ‘display’ command to view these .png files. Here is an example of how to use the ‘display’ command.
(**WEB BROWSER** *scroll down to bottom of page and mouse over/point to dark grey box*)

(**WEB BROWSER** *scroll back up to section the section ‘Example 2’*)

In the previous example, we generated boxplots, mean and median plots. Now let’s just create boxplots of the variables of interest. 

Open your track_and_intensity.output.conf file and set TCMPR_PLOTTER_PLOT_TYPES=BOXPLOT (**WEB BROWSER** *highlight the blue box under Example 2*)

Close the file and rerun the master_metplus.py command from the command line:
(**WEB BROWSER** *mouse over/point to the dark grey box with the command line command*)

Now look at your output files in your output directory.  Now you should see that only boxplot plots were generated.

(**WEB BROWSER** *mouse over/point to light blue box with list of png boxplot files*)

Again, use the ‘display’ command to view the plots.

(**WEB BROWSER** *scroll to bottom of the page and mouse over/point to the dark grey box with examples of using ‘display’*)

This concludes the Track and Intensity TCMPR Plotter use case.  Now it’s your turn to do more experimentation with the configuration files.  Thank you for your time and attention.
