.. _met_tool_gen_vx_mask:

Gen-Vx-Mask Tool
================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/KCISG0phmbw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **MET Version 9.1**.

(*Introduction*)

If you would like to follow along with the exercises in this video, please select one of the options to set up your own :ref:`Training Environment <training_environment>`.

Outline
-------

* What this video will cover
* For more information
* GenVxMask MET tool
* Functionality
* Usage
* How to run it
* Additional examples
* Example 1?
* Example 2?
* METplus integration
* Wrapper options
* SWPC GenVxMask use case

[Screenshot of a GenVxMask mask]
The GenVxMask tool supports a wide array of masking options which are really useful for subsetting your verification domain to a certain region of interest. Many users may do this because they just want to limit their verification results to a particular subregion. Another reason to do this is to cut down on the computational cost and storage when undertaking large verifications with global model datasets. Using GenVxMask to create a subdomain for your region of interest can dramatically speed-up the run times of other MET tools. In this video, I’ll describe what the tool can do, explain the various options that it takes, and illustrate how to run it on the command line. Then we’ll look at some specific examples and show how it can be wrapped by METplus. [If there is time.]

For more information

Before we get started, let me give you a resource where you get more information about GenVxMask. 

(*Screenshot of Chapter 6.1 of the MET User’s Guide*)

https://dtcenter.github.io/MET/Users_Guide/masking.html
You can find technical information about GenVxMask and all of its options in `Chapter 6.1 <https://dtcenter.github.io/MET/Users_Guide/masking.html#gen-vx-mask-tool>`_ of the MET User’s Guide. A link to this is provided in the description for this video.
GenVxMask MET tool
Okay, let’s get started. 

(*Show online tutorial web page for GenVxMask*)

If you’d like to follow along, please open up the online MET tutorial page, which is linked in the description to this video:
https://dtcenter.org/metplus-practical-session-guide-version-3-0/session-1-metplus-setupgrid-grid/met-tool-gen-vx-mask

(*Open up a terminal window*)

Also, please open up a terminal window where you have MET installed. If you still need to get MET installed and running on your system, please refer to video [...] in this series. A link is in the description of this video.
Functionality
The Gen-Vx-Mask tool defines a bitmap masking region for your domain. Unlike many other MET tools, this tool doesn’t use a configuration file. All of its options are specified as command line arguments. GenVxMask requires three required arguments: 
The first required input is a gridded data file which defines your domain. 
The second required argument defines the area of interest (e.g., your mask). Depending on what type of mask you want to make, this can either be a gridded data file or one of a number of options. 
The third required argument specifies the name of the output file which will be generated. Gen-Vx-Mask writes out a NetCDF file containing the bitmap for that masking region. 

The Gen-Vx-Mask tool also also accepts a number of other options.  

.. code-block::

  Example code

Note that it is possible to run Gen-Vx-Mask iteratively, passing its output back in as input, to define more complex masking regions. 

