%global repo dde-control-center

Name:           deepin-control-center
Version:        4.3.7
Release:        1%{?dist}
Summary:        New control center for Linux Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-control-center
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  deepin-dock-devel
BuildRequires:  pkgconfig(dtkwidget) = 2.0
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(geoip)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  qt5-linguist
BuildRequires:  gsettings-qt-devel
Requires:       deepin-account-faces
Requires:       deepin-api
Requires:       deepin-daemon
Requires:       deepin-qt5integration
Requires:       GeoIP-GeoLite-data
Requires:       GeoIP-GeoLite-data-extra
Requires:       gtk-murrine-engine
Requires:       redshift
Requires:       startdde

%description
New control center for Linux Deepin.

%prep
%setup -q -n %{repo}-%{version}
sed -i 's|lrelease|lrelease-qt5|g' translate_generation.sh

sed -i -E '/target.path|utils.path/s|lib|%{_lib}|' plugins/*/*.pro
sed -i 's|lib|%{_lib}|' frame/pluginscontroller.cpp
sed -i -E '/QProcess|target.path/s|lib|libexec|' modules/update/updatemodule.cpp \
    dialogs/reboot-reminder-dialog/reboot-reminder-dialog.pro

%build
%qmake_qt5 PREFIX=%{_prefix} \
    QMAKE_CFLAGS_ISYSTEM= \
    WITH_MODULE_GRUB=NO \
    WITH_MODULE_REMOTE_ASSIST=NO \
    WITH_MODULE_SYSINFO_UPDATE=NO \
    DISABLE_SYS_UPDATE=YES
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{repo}.desktop ||:

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE
%{_bindir}/%{repo}
%{_libdir}/%{repo}/
%{_libexecdir}/%{repo}/
%{_datadir}/applications/%{repo}.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/%{repo}/

%changelog
* Mon Jan 08 2018 Jaroslav <cz.guardian@gmail.com> Stepanek - 4.3.7-1
- Update to version 4.3.7
* Mon Jan 23 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.2-1
- Update to version 4.0.2
* Tue Dec 27 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.24-2
- Bump to newer release because of copr signature
* Sun Dec 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.24-1
- Upgrade to 3.0.24
* Sun Oct 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.21-1
- Initial package build