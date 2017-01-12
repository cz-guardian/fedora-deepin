Name:           deepin-qml-widgets
Version:        2.3.4
Release:        2%{?dist}
Summary:        Deepin QML widgets

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       gtk2 qt5-qtx11extras dbus-factory qt5-qtquick1 qt5-qtdeclarative
BuildRequires:  gtk2-devel qt5-qtx11extras-devel dbus-factory qt5-qtquick1-devel qt5-qtdeclarative-devel

Provides:       %{name}

%global debug_package %{nil}

%description
Deepin QML widgets


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

qmake-qt5 PREFIX=%{_prefix}
make

%install
make INSTALL_ROOT="%{buildroot}" install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datarootdir}/*
%{_lib_dir}/*

%changelog
* Thu Jan 12 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.4-2
- Bump to newer version because of copr
* Sun Dec 11 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.4-1
- Initial package build