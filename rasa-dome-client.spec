Name:      rasa-dome-client
Version:   2.4.2
Release:   0
Url:       https://github.com/warwick-one-metre/domed
Summary:   Dome daemon for the RASA prototype telescope.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python3, python3-Pyro4, python3-warwick-observatory-common, python3-warwick-observatory-dome

%description
Part of the observatory software for the RASA prototype telescope.

dome is a commandline utility that provides access to domed.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}/etc/bash_completion.d
%{__install} %{_sourcedir}/dome %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/completion/rasa-dome %{buildroot}/etc/bash_completion.d/rasa-dome

%files
%defattr(0755,root,root,-)
%{_bindir}/dome
/etc/bash_completion.d/rasa-dome

%changelog
