Name:           deepin-social-sharing
Version:        1.1.4
Release:        1%{?dist}
Summary:        Deepin social sharing service

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       deepin-qml-widgets python2-requests-oauthlib python2-qt5
BuildRequires:  deepin-gettext-tools deepin-qml-widgets

Provides:       %{name}

#%global debug_package %{nil}

%description
Deepin social sharing service


%prep
%autosetup %{version}.tar.gz#%{name}

%build
# fix python version
find src -type f | xargs sed -i 's=\(^#! */usr/bin.*\)python *$=\1python2='

make

%install
%make_install DESTDIR="%{buildroot}"

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datarootdir}/*

%changelog
* Mon Dec 19 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.4-1
- Initial package build