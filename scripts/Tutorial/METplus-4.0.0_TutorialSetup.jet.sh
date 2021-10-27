# METplus v4.0.0 Tutorial Setup Script for Jet (NOAA)

module load intel
module load intelpython/3.6.5
module load netcdf/4.6.1
module load hdf5/1.10.4
module load nco/4.9.1
module load wgrib/1.8.1.0b
module load wgrib2/2.0.8
module load R/4.0.2
module use /contrib/met/modulefiles
module load met/10.0.0
module use /contrib/met/METplus/modulefiles
module load metplus/4.0.0

export METPLUS_TUTORIAL_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

export METPLUS_BUILD_BASE=/contrib/met/METplus/METplus-4.0.0
export MET_BUILD_BASE=/contrib/met/10.0.0
export METPLUS_DATA=/lfs1/HFIP/dtc-hurr/METplus/METplus-4.0_sample_data
