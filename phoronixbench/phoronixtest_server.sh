#!/bin/sh
sudo apt-get install php5-cli php5-json phoronix-test-suite
phoronix-test-suite make-download-cache
cat phoronixtest |grep ^pts |cut -d ' ' -f1 |while read line; do  phoronix-test-suite download-test-files  $line; done

