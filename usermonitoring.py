
from pickle import TRUE
import pwd
import subprocess


def diskusagehome(id):
    # Execute the cmd command and returning the values for the disk usage with PID
    # getpwuid returns the directorýs URL in the system
    # With the command split(\t) if just saving the disk usage from the stdout (includes the URL too)
    try:
        dir = pwd.getpwuid(id).pw_dir
        process_4 = subprocess.run(
            "sudo du -s -b -m " + str(dir), shell=True, stdout=subprocess.PIPE, text=True)
        return process_4.stdout.split("\t")
    except KeyError:
        return None
