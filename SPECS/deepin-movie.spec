Name:           deepin-movie
Version:        2.2.10
Release:        1%{?dist}
Summary:        Movie player based on QtAV

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
Patch0:         deepin-movie-2.2.10-xcffib.patch
Patch1:         deepin-movie-2.2.10-ctypes.patch
  
Requires:       dbus-python deepin-menu python-qt5 python2-ass deepin-qml-widgets qtav-qml-module mediainfo deepin-manual python2-xpybutil python2-pysrt python2-peewee dbus-python python-magic python2-pyopengl qt5-qtbase
BuildRequires:  deepin-gettext-tools

Provides:       %{name}

#%global debug_package %{nil}

%description
Movie player based on QtAV


%prep
%autosetup %{version}.tar.gz#%{name} -p1

%build
# fix python version
find src -type f | xargs sed -i 's=\(^#! */usr/bin.*\)python *$=\1python2='

deepin-generate-mo locale/locale_config.ini

%install
%make_install DESTDIR="%{buildroot}" PREFIX="/usr"
 
%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datarootdir}/*

%changelog
* Wed Dec 21 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.2.10-1
- Initial package build