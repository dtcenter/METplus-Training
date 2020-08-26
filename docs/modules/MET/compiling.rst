.. _met_compiling:

Compiling MET Software
======================

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/KCISG0phmbw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **METplus Version 3.1**.

(*Introduction*)

In this video, we will step through the process of installing the Model Evaluation Tools (MET) verification package using a compilation script that is accessible on our website.  

(*Starting on https://dtcenter.org/community-code/model-evaluation-tools-met*)

This is the website for MET. The information we need is on the “Download” page, so we will go to that page now by clicking on the “Download” link on the right side of this page.  Detailed information about the Software Installation can be found in Chapter 2 of the MET User’s Guide, but for this session, we are going to be using the information on this “Download” page.

The MET package has several external libraries that are required for compiling and building MET.  Under the section “External Libraries Needed To Build MET”, you can see that the BUFRLIB, NetCDF4, HDF5, zlib, and GSL libraries are required, and the GRIB2C, HDF4, and HDF-EOS libraries are optional.

These dependent libraries are contained in the tar_files.tgz package on this Download page under “Sample Script For Compiling External Libraries And MET”. 

Now, we will step through the process of installing the MET package and its dependent libraries.  You will need to decide on a location where you want to install MET.   Then, we will create a directory using the name of the version of MET that we are installing.  In this case, we will create a directory called ….., and will go into that directory.  Now, we will go back to the Download page, right click on “compile_MET_all.sh” and select “Copy Link Address”.  Going back to the terminal window, let’s type “wget”, space, and then paste in the link that we copied and hit enter.

Now, we will go back to the Download page again and will right click on “tar_files.tgz” and select “Copy Link Address”.  Going back to the terminal window, we will type “wget”, space, and then paste in the link that we copied and hit enter.

Now we will unpack the files we downloaded.  We will run the command:

.. code-block:

  tar zxf tar_files.tgz

To unpack the tar_files directory containing the MET library dependencies.

We will run the command:

.. code-block:

  tar zxf compile_MET_all.sh.tgz 

To unpack the compile script. 

Now that we have unpacked the files, we can go ahead and remove the tarred gzipped files. So

.. code-block:

  rm tar_files.tgz compile_MET_all.sh.tgz

While the tar_files directory contains MET’s library dependencies, it does not contain the MET package.  So, you’ll need to get the MET package for the version of MET that you’d like to install. We recommend getting the latest stable release of MET.  In this case, that version is ….

So, once again, we will go to the Download page, find the version under “Recommended”, right click on the MET .tar.gz file, and select “Copy Link Address”. Going back to the terminal window, we will go into the tar_files directory, type “wget”, space, and then paste in the link that we copied and hit enter.

We now have everything we need to install MET on this machine.  The script expects some environment variables to be set in a configuration file to be passed to the script. To save time, we created this file in advance, but will go over each of the need environment variables.  We will get out of the tar_files directory and go up one level.

The configuration file is named install_met_env.hera.  “Hera” is the name of the machine we will be working on.  Looking in the file, we see the first three lines contain “module use” and “module load” statements.  These are loading the intel compiler and the Python package via anaconda.  If you are installing on a machine that does not use modules, be sure that the compiler executables, for example gcc, icc, etc., are in your PATH environment variable, and for Python embedding, make sure that the Python version 3.6.3 or higher executable is in your PATH environment variable.  The MET tools include the ability to embed Python to a limited degree.  Users may use Python scripts and whatever associated Python packages they wish in order to prepare 2D gridded data fields, point observations, and matched pairs as input to the MET tools.  Our installation will include the Python embedding functionality.

Next in the configuration file is TEST_BASE, which should be set to the installation directory, which in this case is /contrib/met/<version number>.  

Then, we will set the COMPILER.  The format here is the name of the compiler, followed by an underscore, followed by the version number.  In this case, we are using intel_18.0.5.274  because we’re using version 18.0.5.274 of the intel compiler.  For the GNU family of compilers, use “gnu” for the compiler name.  For the Intel family of compilers, use “intel”, “ics”, “ips” or other depending on your system.  For the PGI family of compilers, use “pgi” for the compiler name.  

The next variable to set is the MET_SUBDIR, which is the location where top level MET subdir, for example met-9.1_beta1...) should be placed. I typcially set this to the ${TEST_BASE} environment variable. 

Next, we need to tell the script the name of the MET_TARBALL. In this case, the value is met-9.1.20200810.tar.gz… 

Some extra steps are taken if users are on a machine that uses modulefiles.  If you’re on a machine that does not use modulefiles, set USE_MODULES to FALSE.  In this case, we are on a machine that does use modulefiles, so I’ll set USE_MODULES to TRUE.  

The next environment variable is PYTHON_MODULE.  If you are on a machine that does not use modulefiles, simply exclude this variable entirely from your file.  If you are on a machine that does use modulefiles, you will need to set this variable. The format is the name of the Python module to load followed by an underscore and then the version number.  In this case, the value is anaconda_latest, but it could also look something like python_3.6.3. 

If you wish to have the Python embedding functionality, you’ll want to set the next three environment variables - MET_PYTHON, MET_PYTHON_CC, and MET_PYTHON_LD. MET_PYTHON should be set to location containing the bin, include, lib and share directory for Python.  In this case, that location is /contrib/anaconda/anaconda3/latest/, but it is often in a location such as /usr/local/python3.  MET_PYTHON_CC should be set to dash upper case I,  followed by the directory containing the Python include files.  In this case, the value is ${MET_PYTHON}include/python3.7m. You may be able to get this information by running ‘python3-config --cflags’, however, in some cases, like on this machine the running the python3-config command provides additional information that is not necessary to include. (Demonstrate by running python3-config --cflags).  MET_PYTHON_LD should be set to dash upper case L,  followed by the directory containing the Python library files, then a space and -l followed by the necessary Python libraries to link to. In this case, we actually set two different directories to link with, which was determined by running ‘python3-config --ldflags’. (Demonstrate by running python3-config --ldflags). Please note that the backslashes are necessary in the example shown. 

FInally, the SET_D64BIT should be set to FALSE if your version of the GRIB2C library was not compiled with the -D__64BIT__ option and set to TRUE if your version of the GRIB2C library was compiled with the -D__64BIT__ option. The __64BIT__ option should either be used for both or neither.  By default, compile_MET_all.sh will install the GRIB2C library without the -D__64BIT__ option.

Now we are ready to run the installation script to install MET and its library dependencies.  To do this, we will make sure we are in our top level TEST_BASE directory and will run:

.. code-block:

  ./compile_MET_all.sh install_met_env.hera

As the script runs, you’ll see the libraries installed in the following order: GSL, BUFRLIB, ZLIB, LIBPNG, JASPER, G2CLIB, HDF4, HDF-EOS, HDF5, NetCDF-C and NetCDF-CXX packages.  Then, the MET package will be installed.  Once the MET installation is finished you will see the text “Finished compiling at” followed by the date and time.  It is always a good idea to check for errors in the make_test.log file, so we’ll run:

.. code-block:
  
  grep -i error  met-9.1/make_test.log

If you received any errors in your make_test.log file or your installation did not go smoothly is some other aspect, please email met_help@ucar.edu with a description of the problem you experienced, and we will provide assistance.  This information is located on the MET website under “User Support” (click on tab to demonstrate).  Otherwise, congratulations on your successful compilation and installation of the MET package.  

Thank you for watching!













Notes
Example MetPy Monday Conda Installation: https://www.youtube.com/watch?v=-fOfyHYpKck
Used this for reference: https://docs.google.com/document/d/1JEszOfMCmFHrQAZz5W1DBj8TDcPOeCQbQXg7QIbN6fY/edit
which is from Tara in the meeting notes from the 20200716 Meeting for METplus Repo, Wrappers, etc.

https://ral.ucar.edu/staff/jpresto/work/MET_jpresto/Users_Guide/installation.html

Note: Take a look at the tutorial to see how installation is integrated.

