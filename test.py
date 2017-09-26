import os
import glob
# onlyfiles = next(os.walk("/etc/"))[2] #dir is your directory path as string
# print(len(onlyfiles))
#path = "/etc/*"
path = "/etc/" if "/etc/" is not None else "/etc/*"

file_count = len([f for f in glob.glob(path) if os.path.isfile(os.path.join(path, f))])
dirs_count = len([f for f in glob.glob(path) if os.path.isdir(os.path.join(path, f))])

print("files %s",file_count)
print("dir %s",dirs_count)
