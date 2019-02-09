#
# This file is part of domed
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

"""Constants and status codes used by domed"""

# pylint: disable=too-few-public-methods
# pylint: disable=too-many-instance-attributes
# pylint: disable=too-many-arguments

class DomeConfig:
    """Helper class containing dome configuration values"""
    def __init__(self, log_name, daemon, control_ips, serial_port,
                 serial_baud=9600, serial_timeout_seconds=3, shutter_timeout_seconds=60,
                 command_delay_seconds=0.5, step_command_delay_seconds=2.0, legacy_controller=False,
                 heartbeat_port=None, heartbeat_baud=9600, heartbeat_timeout_seconds=3,
                 slow_open_steps=0):
        self.log_name = log_name
        self.daemon = daemon
        self.control_ips = control_ips
        self.serial_port = serial_port
        self.serial_baud = serial_baud
        self.serial_timeout_seconds = serial_timeout_seconds
        self.command_delay_seconds = command_delay_seconds
        self.step_command_delay_seconds = step_command_delay_seconds
        self.shutter_timeout_seconds = shutter_timeout_seconds
        self.legacy_controller = legacy_controller
        self.heartbeat_port = heartbeat_port
        self.heartbeat_baud = heartbeat_baud
        self.heartbeat_timeout_seconds = heartbeat_timeout_seconds
        self.slow_open_steps = slow_open_steps
