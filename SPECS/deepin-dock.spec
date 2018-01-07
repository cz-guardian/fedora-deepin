%global repo dde-dock

Name:           deepin-dock
Version:        4.5.9.1
Release:        1%{?dist}
Summary:        Deepin desktop-environment - Dock module
License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-dock
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  pkgconfig(dtkwidget) = 2.0
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xcb-composite)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  qt5-linguist
BuildRequires:  gsettings-qt-devel
Requires:       deepin-daemon
Requires:       deepin-launcher
Requires:       deepin-menu
Requires:       deepin-qt5integration

%description
Deepin desktop-environment - Dock module.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{repo}-%{version}
sed -i 's|lrelease|lrelease-qt5|g' translate_generation.sh
sed -i '/target.path/s|lib|%{_lib}|' plugins/*/*.pro
sed -i 's|lib|%{_lib}|' frame/controller/dockpluginloader.cpp

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE
%{_bindir}/%{repo}
%{_libdir}/%{repo}/
%{_datadir}/%{repo}/
%{_datadir}/dbus-1/services/*.service

%files devel
%{_includedir}/%{repo}/

%changelog
* Sun Jan 07 2018 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek - 4.5.9.1-1
- Updated to 4.5.9.1
* Thu Apr 20 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 4.2.1-1
- Updated to 4.2.1
* Sun Apr 09 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 4.1.9-1
- Updated to 4.1.9
* Sun Mar 19 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.1.7-1
- Update to version 4.1.7
* Thu Mar 09 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.1.4-1
- Update to version 4.1.4
* Sat Jan 21 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.8-1
- Update to version 4.0.8
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.7-1
- Update to version 4.0.7 and renamed to deepin-dock
* Mon Dec 19 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.6-1
- Update to version 4.0.6
* Sun Dec 04 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.5-2
- Rebuild with newer deepin-tool-kit
* Sun Oct 02 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.5-1
- Initial package build