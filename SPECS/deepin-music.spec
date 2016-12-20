Name:           deepin-music
Version:        2.3.2
Release:        1%{?dist}
Summary:        Awesome music player with brilliant and tweakful UI Deepin-UI based.

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
  
#'sonata'
Requires:       python-gstreamer1 gstreamer-python gstreamer-plugins-bad gstreamer-plugins-good gstreamer1-plugins-ugly python-mutagen python-chardet python-pyquery dbus-python python-CDDB python-pycurl python2-deepin-ui python-keybinder
BuildRequires:  deepin-gettext-tools

Provides:       %{name}

#%global debug_package %{nil}

%description
Awesome music player with brilliant and tweakful UI Deepin-UI based.


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
* Tue Dec 20 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.2-1
- Initial package build