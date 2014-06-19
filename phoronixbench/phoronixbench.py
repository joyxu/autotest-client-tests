import os
import re
import shutil

from autotest.client import utils, test


class phoronixbench(test.test):
    version = 1

    def setup(self, tarball='phoronixbench.tar.gz'):

        shutil.copyfile(os.path.join(self.bindir, 'phoronixtest'),
                        os.path.join(self.srcdir, 'phoronixtest'))
        shutil.copyfile(os.path.join(self.bindir, 'phoronixtest_parse.sh'),
                        os.path.join(self.srcdir, 'phoronixtest_parse.sh'))
        tarball = utils.unmap_url(self.bindir, tarball, self.tmpdir)
        utils.extract_tarball_to_dir(tarball, os.path.join(self.srcdir, 'phoronixbench'))
#        shutil.copyfile(os.path.join(self.bindir, 'user-config.xml'),
#                        os.path.join(self.srcdir, 'user-config.xml'))
        utils.system('chmod +x %s' % os.path.join(self.srcdir, 'phoronixtest_parse.sh'))
#        utils.system('cp -rf %s /root/.phoronix-test-suite/user-config.xml' % os.path.join(self.srcdir, 'user-config.xml'))

    def initialize(self):
        self.results = []
        self.phoronix = os.path.join(self.srcdir, 'phoronixtest_parse.sh')

    def run_once(self, dir='.', nprocs=None, seconds=600, args=''):
        if not nprocs:
            nprocs = self.job.cpu_count()
        os.chdir(self.srcdir)
        self.results = utils.system_output(self.phoronix , retain_output=True)
