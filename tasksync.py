import TheHitList
from subprocess import *
import gtasks
import sys

thl = TheHitList.Application()

passwd = sys.argv[2]
user = sys.argv[1]
if len(sys.argv) < 3:
    print """"Run this script with your Google email and password. \n
    Ex: python tasksync.py name@gmail.com hunter2
    """
    sys.exit()
if len(sys.argv) > 3:
    tag = " " + sys.argv[3]
else:
    tag = " /gtasks"
#kludge to get the tasks...

# TODO: when I hack the gtasks script to be importable this will go away
#tasks_raw = Popen(['python', 'gtasks.py', '-e', user, '-p', passwd], stdout=PIPE).communicate()[0]

#gtasks = tasks_raw.splitlines()
gtasks = gtasks.gtasks(user, passwd, '* ')

for gtask in gtasks:
    task = gtask + tag
    print task
    thl.new_task(task)