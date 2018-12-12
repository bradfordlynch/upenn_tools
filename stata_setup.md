# Stata Setup
## Official Instructions from Stata
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
### Missing Packages
Stata makes use of several packages which are no longer part of the latest Ubuntu LTS releases. Thus these need to be installed manually:

1. (*N.B.* This isn't necessary if the PNG fix below is applied.)libpng012 - Available [here](https://packages.ubuntu.com/xenial/amd64/libpng12-0/download).
2. canberra-gtk-module - Install with apt: `$ apt install libcanberra-gtk*`

### Broken PNG Icon Issue
After you get Stata running the icons are broken. Stata community has developed a fix for this which available [here](https://github.com/kylebarron/stata-png-fix).
