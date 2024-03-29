import os
import subprocess

badhash = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()
goodhash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
bisect_command = f"python manage.py test"
os.system(f"git bisect start {badhash} {goodhash}")
os.system(f"git bisect run {bisect_command}")
