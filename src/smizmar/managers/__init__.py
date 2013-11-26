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


class PackageManager(object):
    """
    Base class for all package managers.
    """

    def __init__(self, **kwargs):
        pass

    def info(self, package_name):
        """
        Returns metadata on a package by name.
        """
        raise NotImplementedError("info must be overriden")

    def list_packages(self, term=None):
        """
        Returns a list of packages.
        """
        raise NotImplementedError("list_packages must be overriden")

    def install(self, names, force=False):
        """
        Installs a package or packages.
        """
        raise NotImplementedError("install must be overriden")

    def remove(self, names, force=False):
        """
        Removes a package or packages.
        """
        raise NotImplementedError("remove must be overriden")

    def update(self, names, force=False):
        """
        Upgrades a package or packages.
        """
        raise NotImplementedError("update must be overriden")
