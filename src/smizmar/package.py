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
Common package class.
"""


class Package(object):

    def __init__(self, name, version, scope):
        self.__name = name
        self.__version = version
        self.__scope = scope

    def __repr__(self):
        return 'Package(name="{0}", version="{1}", scope="{2}")'.format(
            self.__name, self.__version, self.__scope)

    # Read-only properties
    name = lambda s: s.__name
    version = lambda s: s.__version
    scope = lambda s: s.__scope
