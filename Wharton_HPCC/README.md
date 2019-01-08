# Working With Wharton's HPCC
## Setting up Python
Wharton Research IT's official docs are [here](https://research-it.wharton.upenn.edu/tools/python/)

Setup happens on an actual compute node, so open an interactive session:

```bash
qlogin
```

The HPCC's default environment uses Python 2.7. You can enable Python 3 with:

```bash
source /opt/rh/rh-python36/enable
```

Once you create a virtual environment it will be available to worker nodes as well.

## Running an Array Job

The fun stuff...

An array job is launched with:

```bash
qsub -t n[-m[:s]]
```

The scheduler will set specific environment variables for array jobs:

* SGE_TASK_ID - The id of the task being run, id=1,...n
* SGE_TASK_FIRST
* SGE_TASK_LAST - If m is specified in command
* SGE_TASK_STEPSIZE - Default is 1

The files array_test.py and array_test.sh demonstrate loading a file and doing something with it based on the task id. To run the example:

```bash
qsub -t 1-5 array_test.sh
```

This will generate a bunch of output files *array_test.sh.o{submission_number}* and error log files *array_test.sh.e{submission_number}*. Tail the output to watch the results stream in:

```bash
tail -f array_test.sh.o*
```
