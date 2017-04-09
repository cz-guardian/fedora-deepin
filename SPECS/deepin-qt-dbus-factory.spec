%global     srcname dde-qt-dbus-factory

Name:           deepin-qt-dbus-factory
Version:        0.1.0
Release:        1%{?dist}
Summary:        A repository stores auto-generated Qt5 dbus code
License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildRequires:  python-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)

Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}


%prep
%setup %{version}.tar.gz#%{name} -q -n %{srcname}-%{version}

%build
%qmake_qt5 LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%{_libdir}/libdframeworkdbus.so.*

%files devel
%{_includedir}/libdframeworkdbus-1.0/
%{_libdir}/pkgconfig/dframeworkdbus.pc
%{_libdir}/libdframeworkdbus.so


%changelog
* Sun Apr 09 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 0.1.0-1
- Updated to 0.1.0
* Sun Mar 19 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.0.6-1
- Update to version 0.0.6
* Wed Mar 08 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.0.4-1
- Update to version 0.0.4
* Sat Jan 21 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.0.3-1
- Initial package build