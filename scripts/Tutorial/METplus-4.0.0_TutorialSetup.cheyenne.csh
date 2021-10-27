# METplus v4.0.0 Tutorial Setup Script on Cheyenne (NCAR) using csh

module use /glade/p/ral/jntp/MET/METplus/modulefiles
module load metplus/4.0.0
ncar_pylib

# Directory to store tutorial files - configurations, output, notes, etc.
set tmpvar =($_)
set rootdir = `dirname $tmpvar[2]`
#setenv METPLUS_TUTORIAL_DIR `cd $rootdir && pwd`
cd $rootdir
setenv METPLUS_TUTORIAL_DIR `pwd`

# Path to the METplus installation location
setenv METPLUS_BUILD_BASE /glade/p/ral/jntp/MET/METplus/METplus-4.0.0

# Path to the MET installation location
setenv MET_BUILD_BASE /glade/p/ral/jntp/MET/MET_releases/10.0.0

# Path to input data required for running use cases
setenv METPLUS_DATA /glade/p/ral/jntp/MET/METplus/METplus-4.0_sample_data
