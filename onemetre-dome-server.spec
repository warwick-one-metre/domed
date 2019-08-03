Name:      onemetre-dome-server
Version:   2.4.1
Release:   0
Url:       https://github.com/warwick-one-metre/domed
Summary:   Dome daemon for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python36, python36-Pyro4, python36-pyserial, python36-warwick-observatory-common, python36-warwick-observatory-dome
Requires:  observatory-log-client, %{?systemd_requires}

%description
Part of the observatory software for the Warwick one-meter telescope.

domed communicates with the dome controller PLC attached via RS232 adaptor and
provides dome status and control via Pyro.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/domed %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/domed.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/10-onemetre-dome.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/10-onemetre-dome-monitor.rules %{buildroot}%{_udevrulesdir}

%post
%systemd_post domed.service

%preun
%systemd_preun domed.service

%postun
%systemd_postun_with_restart domed.service

%files
%defattr(0755,root,root,-)
%{_bindir}/domed
%defattr(0644,root,root,-)
%{_udevrulesdir}/10-onemetre-dome.rules
%{_udevrulesdir}/10-onemetre-dome-monitor.rules
%defattr(-,root,root,-)
%{_unitdir}/domed.service

%changelog
