import os
import sys
import pandas as pd

# Get the job id from the environment variable SGE_TASK_ID
# Note that it is a string, convert it to an integer
task_id = int(os.environ['SGE_TASK_ID'])

data_filename = '/wrds/boardex/sasdata/na/na_wrds_individual_networks.sas7bdat'

print(sys.version)
print(task_id)

# Load some data
print("Loading data")
foo = pd.read_sas(data_filename, chunksize=1000).read()
print("Loaded data")

# Note that task_id will start at 1, thus i = task_id - 1
print(foo.iloc[task_id - 1])