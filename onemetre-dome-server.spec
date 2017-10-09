Name:      onemetre-dome-server
Version:   2.0
Release:   0
Url:       https://github.com/warwick-one-metre/domed
Summary:   Dome daemon for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
%if 0%{?suse_version}
Requires:  python3, python3-Pyro4, python3-pyserial, python3-warwick-observatory-common, python34-warwick-w1m-dome, observatory-log-client, %{?systemd_requires}
BuildRequires: systemd-rpm-macros
%endif
%if 0%{?centos_ver}
Requires:  python34, python34-Pyro4, python34-pyserial, python34-warwick-observatory-common, python34-warwick-w1m-dome, observatory-log-client, %{?systemd_requires}
%endif

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

%pre
%if 0%{?suse_version}
%service_add_pre domed.service
%endif

%post
%if 0%{?suse_version}
%service_add_post domed.service
%endif
%if 0%{?centos_ver}
%systemd_post domed.service
%endif

%preun
%if 0%{?suse_version}
%stop_on_removal domed.service
%service_del_preun domed.service
%endif
%if 0%{?centos_ver}
%systemd_preun domed.service
%endif

%postun
%if 0%{?suse_version}
%restart_on_update domed.service
%service_del_postun domed.service
%endif
%if 0%{?centos_ver}
%systemd_postun_with_restart domed.service
%endif

%files
%defattr(0755,root,root,-)
%{_bindir}/domed
%defattr(0644,root,root,-)
%{_udevrulesdir}/10-onemetre-dome.rules
%{_udevrulesdir}/10-onemetre-dome-monitor.rules
%defattr(-,root,root,-)
%{_unitdir}/domed.service
%changelog
