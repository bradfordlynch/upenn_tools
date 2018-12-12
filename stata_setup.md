# Stata Setup
## Official Instructions from Stat
- Download Stata15Linux64.tar.gz.
- Become superuser and extract the gzipped tar file into an empty directory.
- Make the installation directory /usr/local/stata15 and cd into it.
- Type /wherever/extracted/files/are/install and follow the instructions.
- For example, assuming you saved the archive in /home/you/Downloads,
  - sudo -s
  - cd /tmp/
  - mkdir statafiles
  - cd statafiles
  - tar -zxf /home/you/Downloads/Stata15Linux64.tar.gz
  - cd /usr/local
  - mkdir stata15
  - cd stata15
  - /tmp/statafiles/install
  
## Post-installation Issues
Stata makes use of several packages which are no longer part of the latest Ubuntu LTS releases. Thus these need to be installed manually:

1. libpng012 - Available [here](https://packages.ubuntu.com/xenial/amd64/libpng12-0/download)
2. canberra-gtk-module - Install with apt: `$ apt install libcanberra-gtk*`