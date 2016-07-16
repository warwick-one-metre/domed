#!/usr/bin/env python3
#
# This file is part of domed.
#
# domed is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# domed is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with domed.  If not, see <http://www.gnu.org/licenses/>.

import threading
import Pyro4
import warwick.observatory as observatory

class FakeLog:
    @Pyro4.expose
    def log_info(self, table, message):
        print('LOG INFO ' + table + ': ' + message)

    @Pyro4.expose
    def log_warning(self, table, message):
        print('LOG WARNING ' + table + ': ' + message)

    @Pyro4.expose
    def log_error(self, table, message):
        print('LOG ERROR ' + table + ': ' + message)

def __fake_log():
    observatory.daemons.observatory_log.launch(FakeLog())

observatory.daemons.observatory_log.host = '127.0.0.1'
threading.Thread(target=__fake_log).start()
