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
How to handle eggs.
"""

import os

from smizmar.managers import PackageManager


class Egg(PackageManager):
    """
    Egg package manager.
    """

    def __init__(self, egg_dir):
        self._base_dir = os.path.realpath(egg_dir)

    def info(self, package_name):
        for name in os.listdir(self._base_dir):
            if name.endswith('.egg'):
                base_name = name.split('-')[0]
                if package_name == base_name:
                    full_path = os.path.sep.join([self._base_dir, name])
                    if os.path.isdir(full_path):
                        pkg_info = open(os.path.sep.join([
                            full_path, 'EGG-INFO', 'PKG-INFO']))
                        print pkg_info.read()
                        pkg_info.close()
                    else:
                        pass

    def __repr__(self):
        return 'Egg(egg_dir="{0}")'.format(self._base_dir)
