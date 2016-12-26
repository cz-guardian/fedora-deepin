Name:           deepin-game
Version:        2014.2
Release:        1%{?dist}
Summary:        Deepin Game Center

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
  
Requires:       python2-deepin-ui python2-deepin-storm dbus-python hicolor-icon-theme python2-jswebkit
BuildRequires:  deepin-gettext-tools

BuildArch:      noarch
Provides:       %{name}

%description
Deepin Game Center


%prep
%autosetup %{version}.tar.gz#%{name}

%build
# fix python version
find src -type f | xargs sed -i 's=\(^#! */usr/bin.*\)python *$=\1python2='

deepin-generate-mo tools/locale_config.ini

%install
%make_install DESTDIR="%{buildroot}" PREFIX="/usr"
 
%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datarootdir}/*

%changelog
* Mon Dec 26 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2014.2-1
- Initial package build