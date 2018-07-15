Name:      rasa-dome-server
Version:   2.1.1
Release:   0
Url:       https://github.com/warwick-one-metre/domed
Summary:   Dome daemon for the RASA prototype telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python34, python34-Pyro4, python34-pyserial, python34-warwick-observatory-common, python34-warwick-w1m-dome, observatory-log-client, %{?systemd_requires}

%description
Part of the observatory software for the RASA prototype telescope.

domed communicates with the dome controller PLC attached via a custom heartbeat board and
provides dome status and control via Pyro.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_udevrulesdir}

%{__install} %{_sourcedir}/domed %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/rasa_domed.service %{buildroot}%{_unitdir}
%{__install} %{_sourcedir}/10-rasa-dome.rules %{buildroot}%{_udevrulesdir}
%{__install} %{_sourcedir}/10-rasa-dome-monitor.rules %{buildroot}%{_udevrulesdir}

%post
%systemd_post rasa_domed.service

%preun
%systemd_preun rasa_domed.service

%postun
%systemd_postun_with_restart rasa_domed.service

%files
%defattr(0755,root,root,-)
%{_bindir}/domed
%defattr(0644,root,root,-)
%{_udevrulesdir}/10-rasa-dome.rules
%{_udevrulesdir}/10-rasa-dome-monitor.rules
%defattr(-,root,root,-)
%{_unitdir}/rasa_domed.service

%changelog
