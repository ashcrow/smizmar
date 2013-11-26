# Copyright (C) 2013 Steve Milner
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
How to handle rpms.
"""

from smizmar.managers import PackageManager
from smizmar.package import Package


class RPM(PackageManager):
    """
    Rpm package manager.
    """
    import rpm

    def _get_rpm_hdr(self, package_name):
        """
        Find an rpm header object by name.
        """
        tx = self.rpm.ts()
        results = tx.dbMatch(self.rpm.RPMTAG_NAME, package_name)

        if results.count() > 1:
            raise Exception('More than 1 package have the name.')

        try:
            return results.next()
        except StopIteration:
            raise Exception('No package with the provided name.')

    def _install(self, filenames, upgrade=False):
        """
        Internal install/upgrade shared code.
        """
        tx = self.rpm.ts()

        flag = 'i'
        if upgrade:
            flag = 'u'

        for filename in filename:
            tx.addInstall(filename, how=flag)
        tx.run()

    def info(self, package_name):
        """
        Returns metadata on a package by name.
        """
        result = self._get_rpm_hdr(package_name)
        return Package(
            result[self.rpm.RPMTAG_NAME],
            result[self.rpm.RPMTAG_VERSION],
            self.rpm.ts().rootDir
        )

    def list_packages(self, term=None):
        """
        Returns a list of packages.
        """
        tx = self.rpm.ts()
        results = tx.dbMatch()
        if term:
            results.pattern(self.rpm.RPMTAG_NAME, self.rpm.RPMMIRE_REGEX, term)

        for result in results:
            yield Package(
                result[self.rpm.RPMTAG_NAME],
                result[self.rpm.RPMTAG_VERSION],
                tx.rootDir,
            )

    def install(self, package_names):
        """
        Installs a package or packages.
        """
        self._install(package_names, 'i')

    def remove(self, package_names):
        """
        Removes a package or packages.
        """
        try:
            for package_name in package_names:
                # Verify it exists ...
                rpm_hdr = self._get_rpm_hdr(package_name)
                # Then remove it
                tx = rpm.ts()
                tx.addErase(rpm_hdr)
            tx.run()
        except Exception, ex:
            print "Could not remove", ex

    def upgrade(self, package_names):
        """
        Upgrades a package or packages.
        """
        self._install(package_names, 'u')

    def __repr__(self):
        return 'Rpm()'
