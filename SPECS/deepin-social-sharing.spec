%global debug_package %{nil}

Name:           deepin-social-sharing
Version:        1.1.4
Release:        2%{?dist}
Summary:        Deepin social sharing service
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       deepin-qml-widgets
Requires:       python-qt5
Requires:       python2-requests-oauthlib
BuildRequires:  deepin-gettext-tools

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%prep
%autosetup %{version}.tar.gz#%{name}

# fix python version
find src -type f | xargs sed -i '1s|python$|python2|'

%build
%make_build

%install
%make_install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_datadir}/dbus-1/services/*.service

%changelog
* Fri Jan 27 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.4-2
- Rewrite of spec file
* Mon Dec 19 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.4-1
- Initial package build