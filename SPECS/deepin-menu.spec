Name:           deepin-menu
Version:        3.0.6
Release:        1%{?dist}
Summary:        Deepin menu service for building beautiful menus

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       python-qt5 qt5-qtx11extras
BuildRequires:  qt5-qtdeclarative-devel python2-setuptools qt5-qtx11extras-devel

Provides:       %{name}

%global debug_package %{nil}

%description
Deepin menu service for building beautiful menus


%prep
%autosetup %{version}.tar.gz#%{name}

%build

%define _lib_dir %{nil}
%ifarch x86_64
  %define _lib_dir %{_usr}/lib64
%endif
%ifarch i386 i686
  %define _lib_dir %{_usr}/lib
%endif

# fix python version
find -iname "*.py" | xargs sed -i 's=\(^#! */usr/bin.*\)python *$=\1python2='
python2 setup.py build
qmake-qt5 DEFINES+=QT_NO_DEBUG_OUTPUT
make

%install
python2 setup.py install --root="%{buildroot}" --optimize=1
make INSTALL_ROOT="%{buildroot}" install

%ifarch x86_64
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

install -dm 755 %{buildroot}/usr/share/dbus-1/services/
install -dm 755 %{buildroot}/etc/xdg/autostart/

rm -r %{buildroot}/usr/deepin_menu

install -m 644 *.service %{buildroot}/usr/share/dbus-1/services/
install -m 644 *.desktop %{buildroot}/etc/xdg/autostart/

%clean
rm -rf %{buildroot}

%files
%{_sysconfdir}/*
%{_lib_dir}/*
%{_datarootdir}/*

%changelog
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.6-1
- Initial package build