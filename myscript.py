import os
import sys
badhash = "6256a66dfaf03a14874d79d34c30d03d29fb4eb0"
goodhash = "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c"
bisect_command = f"python manage.py test"
os.system(f"git bisect start {badhash} {goodhash}")
os.system(f"git bisect run {bisect_command}")
