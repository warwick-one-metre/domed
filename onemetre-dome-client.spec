Name:      onemetre-dome-client
Version:   2.3.0
Release:   0
Url:       https://github.com/warwick-one-metre/domed
Summary:   Dome client for the Warwick one-metre telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python36, python36-Pyro4, python36-warwick-observatory-common, python36-warwick-observatory-dome

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
