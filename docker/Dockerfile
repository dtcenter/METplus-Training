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
#WORKDIR /metplus

RUN echo DOCKER_WORK_DIR is ${DOCKER_WORK_DIR}

ENV DOCKER_WORK_DIR /root

RUN echo DOCKER_WORK_DIR is ${DOCKER_WORK_DIR}

#
# Setup the environment for interactive bash/csh container shells.
#
RUN mkdir -p ${DOCKER_WORK_DIR}/METplus_Tutorial \
 && echo export METPLUS_TUTORIAL_DIR=${DOCKER_WORK_DIR}/METplus_Tutorial >> /etc/bashrc \
 && echo setenv METPLUS_TUTORIAL_DIR ${DOCKER_WORK_DIR}/METplus_Tutorial >> /etc/csh.cshrc \
 && echo export METPLUS_BUILD_BASE=${DOCKER_WORK_DIR}/METplus >> /etc/bashrc \
 && echo setenv METPLUS_BUILD_BASE ${DOCKER_WORK_DIR}/METplus >> /etc/csh.cshrc \
 && echo export MET_BUILD_BASE=/usr/local >> /etc/bashrc \
 && echo setenv MET_BUILD_BASE /usr/local >> /etc/csh.cshrc \
 && echo export METPLUS_DATA=/data/input/METplus_Data >> /etc/bashrc \
 && echo setenv METPLUS_DATA /data/input/METplus_Data >> /etc/csh.cshrc

#
# Install additional tools for METplus Training modules
#
# RUN yum -y update \
# && yum -y install nco.x86_64

