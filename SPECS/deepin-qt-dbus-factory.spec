%global soname dframeworkdbus
%global repo   dde-qt-dbus-factory

Name:           deepin-qt-dbus-factory
Version:        0.4.2
Release:        1%{?dist}
Summary:        A repository stores auto-generated Qt5 dbus code
# The entire source code is GPLv3+ except
# libdframeworkdbus/qtdbusextended/ which is LGPLv2+
License:        GPLv3+ and LGPLv2+
URL:            https://github.com/linuxdeepin/dde-qt-dbus-factory
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  python-devel
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)

%description
A repository stores auto-generated Qt5 dbus code.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{repo}-%{version}

%build
%qmake_qt5 LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README
%license LICENSE
%{_libdir}/lib%{soname}.so.*

%files devel
%{_includedir}/lib%{soname}-1.0/
%{_libdir}/pkgconfig/%{soname}.pc
%{_libdir}/lib%{soname}.so

%changelog
* Sat Jan 06 2018 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 0.4.2-1
- Updated to 0.4.2
* Sun Apr 09 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 0.1.0-1
- Updated to 0.1.0
* Sun Mar 19 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.0.6-1
- Update to version 0.0.6
* Wed Mar 08 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.0.4-1
- Update to version 0.0.4
* Sat Jan 21 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.0.3-1
- Initial package build