import TheHitList
from subprocess import *
import sys

thl = TheHitList.Application()

passwd = sys.argv[2]
user = sys.argv[1]

if len(sys.argv) > 3:
    tag = sys.argv[3]
else:
    tag = "/gtasks"
#kludge to get the tasks...

# TODO: when I hack the gtasks script to be importable this will go away
tasks_raw = Popen(['python', 'gtasks.py', '-e', user, '-p', passwd], stdout=PIPE).communicate()[0]

gtasks = tasks_raw.splitlines()

for gtask in gtasks:
    task = gtask[4:] + tag
    print task
    thl.new_task(task)