# Dynatrace_file_module


## Usage

*processName* can be set to any process on a host that is monitored
*filePath* is utilizing the python glob module.
   - Getting txt files:  *Setting \<filepath\>/\*.txt
   - Getting all files under one directory: \<filepath\>/\*

## Examples

filePath = /etc/\* (getting all files under /etc/)
filePath = /etc/\*.txt (getting txt files under /etc/)



The module will also count the number of directories in that folder.
