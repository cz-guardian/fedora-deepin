Name:           deepin-screenshot
Version:        3.1.10
Release:        2%{?dist}
Summary:        Easy-to-use screenshot tool for linuxdeepin desktop environment

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       deepin-menu deepin-qml-widgets qt5-qtsvg deepin-gettext-tools python2-pyopengl gnome-python2-libwnck python2-xpybutil qt5-qtgraphicaleffects qt5-qtquickcontrols
BuildRequires:  deepin-menu deepin-qml-widgets qt5-qtsvg-devel deepin-gettext-tools

Provides:       %{name}

%global debug_package %{nil}

%description
Easy-to-use screenshot tool for linuxdeepin desktop environment

%prep
%autosetup %{version}.tar.gz#%{name}

%build

# fix python version
find -iname "*.py" | xargs sed -i 's=\(^#! */usr/bin.*\)python *$=\1python2='

make

%install
make DESTDIR="%{buildroot}" install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datarootdir}/*

%changelog
* Thu Jan 12 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.10-2
- Dependecy bump
* Sun Dec 11 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.10-1
- Initial package build
