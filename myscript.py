import os
from pip._internal.vcs import git

badhash = git.Repo(search_parent_directories=True).head.object.hexsha
goodhash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
bisect_command = f"python manage.py test"
os.system(f"git bisect start {badhash} {goodhash}")
os.system(f"git bisect run {bisect_command}")
