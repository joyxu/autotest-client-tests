#!/bin/sh

apt-get install php5-cli php5-json phoronix-test-suite
mv -f phoronixbench/*  /root/.phoronix-test-suite/
cat phoronixtest |grep ^pts |cut -d ' ' -f1 |while read line; do  phoronix-test-suite batch-install $line; done
cat phoronixtest |grep ^pts |cut -d ' ' -f1 |while read line; do  phoronix-test-suite batch-run $line; done
