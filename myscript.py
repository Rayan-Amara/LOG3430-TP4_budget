import os
import sys
badhash = sys.argv[1]
goodhash = sys.argv[2]
bisect_command = f"python manage.py test"
os.system(f"git bisect start {badhash} {goodhash}")
os.system(f"git bisect run {bisect_command}")
