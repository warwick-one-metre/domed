Name:      onemetre-dome-server
Version:   1.1
Release:   1
Url:       https://github.com/warwick-one-metre/domed
Summary:   Dome daemon for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, %{?systemd_requires}
BuildRequires: systemd-rpm-macros

%description
Part of the observatory software for the Warwick one-meter telescope.

domed communicates with the dome controller PLC attached via RS232 adaptor and
provides dome status and control via Pyro.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/domed %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/domed.service %{buildroot}%{_unitdir}

%pre
%service_add_pre domed.service

%post
%service_add_post domed.service
%fillup_and_insserv -f -y domed.service

# Install python dependencies
# This is horrible, but it seems to be the only way that actually works!
pip3 install pyserial Pyro4

%preun
%stop_on_removal domed.service
%service_del_preun domed.service

%postun
%restart_on_update domed.service
%service_del_postun domed.service

%files
%defattr(0755,root,root,-)
%{_bindir}/domed
%defattr(-,root,root,-)
%{_unitdir}/domed.service

%changelog
