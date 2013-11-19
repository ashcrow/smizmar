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
Tests for the managers.PackageManager class.
"""

from . import TestCase

from smizmar.managers import PackageManager


class TestPackageManager(TestCase):

    def setUp(self):
        """
        Create the PackageManager instance for every test.
        """
        self.pm = PackageManager()

    def test_info(self):
        """
        Verify PackageManager.info() requires overriding.
        """
        self.assertRaises(NotImplementedError, self.pm.info, None)

    def test_list_packages(self):
        """
        Verify PackageManager.list_packages() requires overriding.
        """
        self.assertRaises(NotImplementedError, self.pm.list_packages)

    def test_install(self):
        """
        Verify PackageManager.install() requires overriding.
        """
        self.assertRaises(NotImplementedError, self.pm.install, 'packagename')

    def test_update(self):
        """
        Verify PackageManager.update() requires overriding.
        """
        self.assertRaises(NotImplementedError, self.pm.update, 'packagename')
