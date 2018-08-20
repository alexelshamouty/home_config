#!/bin/sh
#Start google
/usr/bin/google-chrome-stable &
#Start shell
/usr/bin/terminology &
#Start clipit
( sleep 10 ; clipit ) &
#Start evince
( sleep 5 ; evince ) &
#Start redshift
redshift &

(x0vncserver -display :0 -passwordfile ~/.vnc/passwd > /dev/null 2>&1) &
