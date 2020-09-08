.. _met_installation:

Compiling MET
=============

.. raw:: html

  <iframe width="560" height="315" src="https://www.youtube.com/embed/KCISG0phmbw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Developed for **MET Version 9.1**.

**Follow Along!** with these exercises.

(*Introduction*)

In this video, we will step through the process of installing the Model Evaluation Tools (MET) verification package using a compilation script that is accessible on our `website <https://dtcenter.org/community-code/model-evaluation-tools-met>`_.  

This is the website for MET. The information we need is on the "`Download <https://dtcenter.org/community-code/model-evaluation-tools-met/download>`_" page, so we will go to that page now by clicking on the "Download" link on the right side of this page.  Detailed information about the Software Installation can be found in `Chapter 2 <https://dtcenter.github.io/MET/Users_Guide/installation.html>`_ of the MET Users Guide, but for this session, we are going to be using the information on this "Download" page.

The MET package has several external libraries that are required for compiling and building MET.  Under the section "External Libraries Needed To Build MET", you can see that the BUFRLIB, NetCDF4, HDF5, zlib, and GSL libraries are required, and the GRIB2C, HDF4, HDF-EOS, Cairo and FreeType libraries are optional.

These dependent libraries are contained in the tar_files.tgz package on this Download page under "Sample Script For Compiling External Libraries And MET". 

Now, we will step through the process of installing the MET package and its dependent libraries.  You will need to decide on a location where you want to install MET.   Then, create a directory using the name of the version of MET that you are installing.  In this case, we will create a directory called 9.1, and we'll go into that directory.

.. code-block::

      mkdir 9.1
      cd 9.1
      
Now, we want go to the Download page, right click on "compile_MET_all.sh" and select "Copy Link Address".  Going back to the terminal window, let's type "wget", space, and then paste in the link that we copied and hit enter.

.. code-block::

   wget https://dtcenter.org/sites/default/files/community-code/met/compile_scripts/compile_MET_all.sh.tgz

Now, we will go back to the Download page again and will right click on "tar_files.tgz" and select "Copy Link Address".  Going back to the terminal window, we will type "wget", space, and then paste in the link that we copied and hit enter.

.. code-block::

   wget https://dtcenter.org/sites/default/files/community-code/met/compile_scripts/tar_files.tgz

Now we will unpack the files we downloaded.  We will run the command to unpack the tar_files directory containing the MET library dependencies:

.. code-block::

  tar zxf tar_files.tgz


We will run the command to unpack the compilation script:

.. code-block::

  tar zxf compile_MET_all.sh.tgz 


Now that we have unpacked the files, we can go ahead and remove the tarred gzipped files. So, we'll execute the following command to remove those files:

.. code-block::

  rm tar_files.tgz compile_MET_all.sh.tgz


While the tar_files directory contains MET's library dependencies, it does not contain the MET package.  So, you'll need to get the MET package for the version of MET that you'd like to install. We recommend getting the latest stable release of MET.  In this case, that version is 9.1.

Once again, we will go to the Download page, find the version under "Recommended", right click on the met-9.1.tar.gz file, and select "Copy Link Address". Going back to the terminal window, we will go into the tar_files directory, type "wget", space, and then paste in the link that we copied and hit enter.

.. code-block::

   cd tar_files
   wget https://github.com/dtcenter/MET/releases/download/met-9.1/met-9.1.20200810.tar.gz

We now have everything we need to install MET on this machine.  The compilation script expects some environment variables to be set in a configuration file to be passed to the script. To save time, we created this file in advance, but will go over each of the need environment variables.  We will get out of the tar_files directory and go up one level.

.. code-block::

   cd ../

The configuration file is named install_met_env.hera.  "Hera" is the name of the machine we will be working on.  Looking in the file, we see the first three lines contain "module use" and "module load" statements.  These are loading the intel compiler and the Python package via anaconda on this machine.  If you are installing on a machine that does not use modules, be sure that the compiler executables, for example gcc, icc, etc., are in your PATH environment variable, and for Python embedding, make sure that the Python version 3.6.3 or higher executable is in your PATH environment variable as well.  The MET tools include the ability to embed Python to a limited degree.  Users may use Python scripts and whatever associated Python packages they wish in order to prepare 2D gridded data fields, point observations, and matched pairs as input to the MET tools.  Our installation will include the Python embedding functionality.

Next in the configuration file is TEST_BASE, which should be set to the installation directory - the full path, including the 9.1 directory you recently created.  

Then, we will set the COMPILER.  The format here is the name of the compiler, followed by an underscore, followed by the version number.  In this case, we are using intel_18.0.5.274  because we're using version 18.0.5.274 of the intel compiler.  For the GNU family of compilers, use "gnu" for the compiler name.  For the Intel family of compilers, use "intel", "ics", "ips" or another name, depending on your system.  For the PGI family of compilers, use "pgi" for the compiler name.  

The next variable to set is the MET_SUBDIR, which is the location where the top level MET subdir, for example met-9.1, should be placed. I typcially set this to the value of the TEST_BASE environment variable. 

Next, we need to tell the script the name of the MET_TARBALL. In this case, the value is met-9.1.20200810.tar.gz.

For this tutorial, we are compiling MET and its dependent libraries on a machine that uses modulefiles, so we will set USE_MODULES to TRUE.  If you're compiling on a machine that does not use modulefiles, please set USE_MODULES to FALSE.

The next environment variable is PYTHON_MODULE.  If you are on a machine that does not use modulefiles, simply exclude this variable entirely from your file.  If you are on a machine that does use modulefiles, you will need to set this variable. The format is the name of the Python module to load followed by an underscore and then the version number.  In this case, the value is anaconda_latest, but it could also look something like python_3.6.3. 

If you wish to have the Python embedding functionality, you'll want to set the next three environment variables - MET_PYTHON, MET_PYTHON_CC, and MET_PYTHON_LD. MET_PYTHON should be set to the location containing the bin, include, lib and share subdirectories for Python.  In this case, we're using an anaconda location, but often it is in a location in /usr/local/python3.  MET_PYTHON_CC should be set to dash upper case I, "-I", followed by the directory containing the Python include files.  In this case, the value is ${MET_PYTHON}/include/python3.7m. You may be able to get this information by running "python3-config --cflags", however, in some cases, like on this machine the running the python3-config command provides additional information that is not necessary to include.

.. code-block::
   
   python3-config --cflags

MET_PYTHON_LD should be set to dash upper case L, "-L", followed by the directory containing the Python library files, then a space and dash lower case l, "-l", followed by the necessary Python libraries to link to. In this case, we actually set two different directories to link with, which was determined by running "python3-config --ldflags".

.. code-block::

   python3-config --ldflags

Please note that the backslashes are necessary in the example shown. 

Finally, the variable SET_D64BIT should be set to FALSE if your version of the GRIB2C library was not compiled with the -D__64BIT__ option, but set to TRUE if your version of the GRIB2C library was compiled with the -D__64BIT__ option. The -D__64BIT__ option should either be used for compiling both the GRIB2C library and MET, or for neither.  By default, compile_MET_all.sh will install the GRIB2C library without the -D__64BIT__ option.

Now we are ready to run the installation script to install MET and its library dependencies.  To do this, we will make sure we are in our top level TEST_BASE directory and will run:

.. code-block::

  ./compile_MET_all.sh install_met_env.hera

As the script runs, you'll see screen output telling you the libraries that are being installed, and then you'll see the MET package being installed.  Once the MET installation is finished you will see the text "Finished compiling at" followed by the date and time.

Because the installation can take a while, I ran through it previously in this same area and saved off the screen output and the installation in a 9.1_preinstall directory, which I'll take you to now so we can take a look at that screen output.  Looking at the screen output we can see some of the settings from our environment followed by the compilation of each libary and then the installation of MET.  We can also see the output of the MET variables being set in the script.  At the bottom, we see the message that MET finished compiling.


It is always a good idea to check for errors in the make_test.log file, so we'll run:

.. code-block::
  
  grep -i error  met-9.1/make_test.log

And, fortunately, we don't see any errors. If you received any errors in your make_test.log file or your installation did not go smoothly in some other aspect, please email met_help@ucar.edu with a description of the problem you experienced, and we will provide assistance.  This information is located on the MET website under `"User Support" <https://dtcenter.org/community-code/model-evaluation-tools-met/user-support>`_.  Otherwise, congratulations on your successful installation of the MET package.  

Thank you for watching!

