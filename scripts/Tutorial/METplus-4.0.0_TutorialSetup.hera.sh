# METplus v4.0.0 Tutorial Setup Script for Hera (NOAA)

module use /contrib/METplus/modulefiles
module load metplus/4.0.0

export METPLUS_TUTORIAL_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
export METPLUS_BUILD_BASE=/contrib/METplus/METplus-4.0.0
export MET_BUILD_BASE=/contrib/met/10.0.0
export METPLUS_DATA=/scratch1/BMC/dtc/METplus/METplus-4.0_sample_data
