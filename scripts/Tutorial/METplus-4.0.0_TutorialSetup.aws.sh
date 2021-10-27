# METplus v4.0.0 Tutorial variables for AMI

# Directory to store tutorial files - configurations, output, notes, etc.
export METPLUS_TUTORIAL_DIR=/home/admin/METplus-4.0.0_Tutorial

# Path to the METplus installation location
export METPLUS_BUILD_BASE=/opt/METplus

# Path to the MET installation location
export MET_BUILD_BASE=/opt/MET

# Path to input data required for running use cases
export METPLUS_DATA=/d1/projects/METplus/METplus_Data

# Add METplus ush directory and MET bin directory to the path
# This allows you to run METplus without specifying the full path
export PATH=${METPLUS_BUILD_BASE}/ush:${MET_BUILD_BASE}/bin:${PATH}
