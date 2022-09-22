from distutils.dir_util import copy_tree
import os
import shutil

src = "glm"
dst = "include/glm"
uselessFolders = [
	"cmake",
	"doc",
	"test",
	"util"
]

if not os.path.isdir(dst):
	os.makedirs(dst)

copy_tree(src, dst)

for folder in uselessFolders:
	shutil.rmtree(folder, ignore_errors=True)