Name:           dtkwidget
Version:        2.0.6
Release:        1%{?dist}
Summary:        Deepin tool kit widget modules
License:        GPLv3
URL:            https://github.com/linuxdeepin/dtkwidget
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

Requires:       qt5-qtbase
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-static
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xrender)
Provides:       deepin-tool-kit%{_isa} = %{version}-%{release}
Obsoletes:      deepin-tool-kit%{_isa} < %{version}-%{release}

%description
DtkWidget is Deepin graphical user interface for deepin desktop development.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q
sed -i 's|lrelease|lrelease-qt5|g' tools/translate_generation.sh
sed -i 's|/lib|/libexec|' tools/svgc/svgc.pro

%build
%qmake_qt5 PREFIX=%{_prefix} LIB_INSTALL_DIR=%{_libdir} DBUS_VERSION_0_4_2=YES
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE
%{_libdir}/lib%{name}.so.*
%{_libexecdir}/dtk2/dtk-svgc
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/translations/

%files devel
%{_includedir}/libdtk-*/
%{_libdir}/cmake/DtkWidget/*.cmake
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Mon Jan 22 2018 Jaroslav <cz.guardian@gmail.com> Stepanek - 2.0.6-1
- Update to version 2.0.6
* Fri Jan 05 2018 Jaroslav <cz.guardian@gmail.com> Stepanek - 2.0.5.3-2
- Added qt5-qtbase as dependency 
* Fri Jan 05 2018 Jaroslav <cz.guardian@gmail.com> Stepanek - 2.0.5.3-1
- Initial package build
