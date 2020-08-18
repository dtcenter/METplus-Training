ARG METPLUS_VERSION

FROM dtcenter/metplus:${METPLUS_VERSION:-develop}
MAINTAINER John Halley Gotway <johnhg@ucar.edu>

# 
# This Dockerfile extends the METplus image for training
#

ARG SOURCE_BRANCH

RUN if [ -z ${SOURCE_BRANCH+x} ]; then \
      echo "ERROR: SOURCE_BRANCH undefined! Rebuild with \"--build-arg SOURCE_BRANCH={branch name}\""; \
      exit 1; \
    else \
      echo "Build Argument SOURCE_BRANCH=${SOURCE_BRANCH}"; \
    fi

ARG METPLUS_VERSION

RUN if [ -z ${METPLUS_VERSION+x} ]; then \
      echo "ERROR: METPLUS_VERSION undefined! Using default (develop) or rebuild with \"--build-arg METPLUS_VERSION={branch or tag name}\""; \
      exit 1; \
    else \
      echo "Build Argument METPLUS_VERSION=${METPLUS_VERSION}"; \
    fi

#
# Set working directory
#
WORKDIR /metplus

#
# Install additional tools for METplus Training modules
#
# RUN yum -y update \
# && yum -y install nco.x86_64

