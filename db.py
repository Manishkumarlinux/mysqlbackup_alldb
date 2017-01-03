#!/usr/bin/python

import os
import time
import datetime

DBUSER = 'root'
DBPASS = 'Redhat'
BACKUP_PATH = '/opt/dbbackup/'

DATETIME = time.strftime('%d%m%Y-%H%M')

TODAYBACKUPPATH= BACKUP_PATH + DATETIME

if not os.path.exists(TODAYBACKUPPATH):
    os.makedirs(TODAYBACKUPPATH)
    mysql_cmd = "mysqldump -u" + DBUSER + " -p" + DBPASS + " --all-databases" + " > " + TODAYBACKUPPATH + "/" + "alldb.sql"
    os.system(mysql_cmd)
else:
    print "backup"
