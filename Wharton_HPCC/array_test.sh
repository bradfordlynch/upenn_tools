#!/usr/bin/env bash
# Enable Python 3
source /opt/rh/rh-python36/enable

# Activate virtual environment that has been setup previously
# with the packages needed, e.g., Pandas
source ~/env/bin/activate

# Run our script
python array_test.py