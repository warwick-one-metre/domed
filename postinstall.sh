# Install python dependencies
# This is horrible, but it seems to be the only way that actually works!
pip3 install pyserial Pyro4

# Enable the service so that it starts immediately
systemctl enable domed.service
systemctl start domed.service
