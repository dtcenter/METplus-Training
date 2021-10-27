# METplus v4.0.0 Tutorial Setup Script on Cheyenne (NCAR) using bash

module use /glade/p/ral/jntp/MET/METplus/modulefiles
module load metplus/4.0.0
ncar_pylib

# Directory to store tutorial files - configurations, output, notes, etc.
export METPLUS_TUTORIAL_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Path to the METplus installation location
export METPLUS_BUILD_BASE=/glade/p/ral/jntp/MET/METplus/METplus-4.0.0

# Path to the MET installation location
export MET_BUILD_BASE=/glade/p/ral/jntp/MET/MET_releases/10.0.0

# Path to input data required for running use cases
export METPLUS_DATA=/glade/p/ral/jntp/MET/METplus/METplus-4.0_sample_data
