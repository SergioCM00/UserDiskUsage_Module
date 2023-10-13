
import usermonitoring
import os

try:
    # For the following IDs (0,my userID and an invented one), print disk Usage
    for uid in [0, os.getuid(), 7777]:
        mb = usermonitoring.diskusagehome(uid)
        print("Disk Usage of user with UID " +
              str(uid) + " : " + str(mb[0]) + " mb")
except TypeError:
    # If there is an error (non-existing user usage) print this
    print("Disk Usage of user with UID " + str(uid) +
          " : Could not determine disk usage")
