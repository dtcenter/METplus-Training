# METplus v4.0.0 Tutorial Setup Script on Seneca (NCAR) using bash

# Directory to store tutorial files - configurations, output, notes, etc.
export METPLUS_TUTORIAL_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Path to the METplus installation location
export METPLUS_BUILD_BASE=/usr/local/METplus-4.0.0

# Path to the MET installation location
export MET_BUILD_BASE=/usr/local/met-10.0.0

# Path to input data required for running use cases
export METPLUS_DATA=/d1/projects/METplus/METplus_Data

# Add METplus ush directory and MET bin directory to the path
# This allows you to run METplus without specifying the full path
export PATH=${METPLUS_BUILD_BASE}/ush:${MET_BUILD_BASE}/bin:${PATH}
