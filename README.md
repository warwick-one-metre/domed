## W1m/NITES dome daemon [![Travis CI build status](https://travis-ci.org/warwick-one-metre/domed.svg?branch=master)](https://travis-ci.org/warwick-one-metre/domed)

Part of the observatory software for the Warwick one-meter and NITES telescopes.

`domed` communicates with the Astrohaven dome controller (PLC or legacy) attached via RS232 adaptor, and with the [dome heartbeat monitor](https://github.com/warwick-one-metre/dome-heartbeat-monitor) attached via USB.  Control is exposed via Pyro.

`dome` is a commandline utility that provides access to the W1m dome.

`python34-warwick-w1m-dome` is a python module with the common dome code.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the W1m software architecture and instructions for developing and deploying the code.

### Software Setup (W1m)

After installation, the `onemetre-dome-server` must be enabled using:
```
sudo systemctl enable domed.service
```

The service will automatically start on system boot, or you can start it immediately using:
```
sudo systemctl start domed.service
```

Finally, open a port in the firewall so that other machines on the network can access the daemon:
```
sudo firewall-cmd --zone=public --add-port=9004/tcp --permanent
sudo firewall-cmd --reload
```

### Hardware Setup

The dome is expected to be connected to the physical serial port; `/dev/ttyS0` is automatically remapped to `/dev/dome`.
If the dome is moved to a USB-RS232 adaptor then `10-onemetre-dome.rules` should be updated to match against the specific vendor/product/serial details.

The dome monitor is matched against its unique serial number.  If the Arduino is replaced then the serial number should be updated in `10-onemetre-dome-monitor.rules`.
