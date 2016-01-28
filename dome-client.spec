Name:      onemetre-dome-client
Version:   1.0
Release:   1
Url:       https://github.com/warwick-one-metre/domed
Summary:   Dome client for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3

%description
Part of the observatory software for the Warwick one-meter telescope.

dome is a commandline utility that provides access to domed.

%build
mkdir -p %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/dome %{buildroot}%{_bindir}

# Install python dependencies
# This is horrible, but it seems to be the only way that actually works!
pip3 install Pyro4

%files
%defattr(0755,root,root,-)
%{_bindir}/dome

%changelog
