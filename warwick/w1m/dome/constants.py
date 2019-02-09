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
# pylint: disable=invalid-name

FMT_GREEN = u'\033[92m'
FMT_RED = u'\033[91m'
FMT_CYAN = u'\033[96m'
FMT_YELLOW = u'\033[93m'
FMT_BOLD = u'\033[1m'
FMT_CLEAR = u'\033[0m'

class CommandStatus:
    """Numeric return codes"""
    # General error codes
    Succeeded = 0
    Failed = 1
    Blocked = 2
    HeartbeatTimedOut = 3
    HeartbeatCloseInProgress = 4
    HeartbeatUnavailable = 5
    HeartbeatInvalidTimeout = 6
    EngineeringModeRequiresHeartbeatDisabled = 7
    EngineeringModeActive = 8
    InvalidControlIP = 10

    _messages = {
        # General error codes
        1: 'error: command failed',
        2: 'error: another command is already running',
        10: 'error: command not accepted from this IP',

        # dome specific codes
        3: 'error: heartbeat monitor has tripped',
        4: 'error: heartbeat monitor is closing the dome',
        5: 'error: heartbeat monitor is not available',
        6: 'error: heartbeat timeout must be less than 120s',
        7: 'error: heartbeat monitor must be disabled before enabling engineering mode',
        8: 'error: dome is in engineering mode',

        -100: 'error: terminated by user',
        -101: 'error: unable to communicate with dome daemon'
    }

    @classmethod
    def message(cls, error_code):
        """Returns a human readable string describing an error code"""
        if error_code in cls._messages:
            return cls._messages[error_code]
        return 'error: Unknown error code {}'.format(error_code)

class DomeShutterStatus:
    """Status of the dome shutters"""
    Closed, Open, PartiallyOpen, Opening, Closing, HeartbeatMonitorForceClosing = range(6)

    _labels = {
        0: FMT_RED + FMT_BOLD + 'CLOSED' + FMT_CLEAR,
        1: FMT_GREEN + FMT_BOLD + 'OPEN' + FMT_CLEAR,
        2: FMT_CYAN + FMT_BOLD + 'PARTIALLY OPEN' + FMT_CLEAR,
        3: FMT_YELLOW + FMT_BOLD + 'OPENING' + FMT_CLEAR,
        4: FMT_YELLOW + FMT_BOLD + 'CLOSING' + FMT_CLEAR,
        5: FMT_RED + FMT_BOLD + 'FORCE CLOSING' + FMT_CLEAR,
    }

    @classmethod
    def label(cls, status):
        """Returns a human readable string describing an error code"""
        if status in cls._labels:
            return cls._labels[status]
        return FMT_RED + FMT_BOLD + 'UNKNOWN STATUS' + FMT_CLEAR

class DomeHeartbeatStatus:
    """Status of the dome heartbeat monitoring"""
    Disabled, Active, TrippedClosing, TrippedIdle, Unavailable = range(5)

    _labels = {
        0: FMT_BOLD + 'DISABLED' + FMT_CLEAR,
        1: FMT_GREEN + FMT_BOLD + 'ACTIVE' + FMT_CLEAR,
        2: FMT_RED + FMT_BOLD + 'CLOSING DOME' + FMT_CLEAR,
        3: FMT_RED + FMT_BOLD + 'TRIPPED' + FMT_CLEAR,
        4: FMT_YELLOW + FMT_BOLD + 'UNAVAILABLE' + FMT_CLEAR,
    }

    @classmethod
    def label(cls, status):
        """Returns a human readable string describing an error code"""
        if status in cls._labels:
            return cls._labels[status]
        return FMT_RED + FMT_BOLD + 'UNKNOWN STATUS' + FMT_CLEAR
