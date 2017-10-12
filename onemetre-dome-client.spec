Name:      onemetre-dome-client
Version:   2.0.1
Release:   0
Url:       https://github.com/warwick-one-metre/domed
Summary:   Dome client for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
%if 0%{?suse_version}
Requires:  python3, python34-Pyro4, python34-warwick-observatory-common, python34-warwick-w1m-dome
%endif
%if 0%{?centos_ver}
Requires:  python34, python34-Pyro4, python34-warwick-observatory-common, python34-warwick-w1m-dome
%endif

%description
Part of the observatory software for the Warwick one-meter telescope.

dome is a commandline utility that provides access to domed.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/dome %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/dome %{buildroot}/etc/bash_completion.d/dome

%files
%defattr(0755,root,root,-)
%{_bindir}/dome
/etc/bash_completion.d/dome

%changelog
