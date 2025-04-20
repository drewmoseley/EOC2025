#!/bin/bash -x

pwd
ls -l $(pwd)/build/hello-pi 
scp $(pwd)/build/hello-pi dmoseley@rpifarm:~/
ssh -n dmoseley@rpifarm "killall gdbserver 2>/dev/null; \
        nohup gdbserver --multi :2345 ~/hello-pi >~/gdbserver.log 2>&1 &"
sleep 1
