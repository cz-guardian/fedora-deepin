%global 		    srcname dde-file-manager

Name:           deepin-file-manager
Version:        1.4.1
Release:        1%{?dist}
Summary:        Deepin File Manager
License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       deepin-manual
Requires:       deepin-shortcut-viewer
Requires:       deepin-terminal
Requires:       file-roller
Requires:       gvfs-client
Requires:       xdg-user-dirs
BuildRequires:  atk-devel
BuildRequires:  deepin-tool-kit-devel
BuildRequires:  dtksettings-devel
BuildRequires:  ffmpegthumbnailer-devel
BuildRequires:  file-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  gtk2-devel
BuildRequires:  libsecret-devel
BuildRequires:  polkit-devel
BuildRequires:  polkit-qt5-1-devel
BuildRequires:  poppler-cpp-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtx11extras-devel

Provides:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{srcname}%{?_isa} < %{version}-%{release}

%description
%{summary}


%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}


%prep
%autosetup %{version}.tar.gz#%{name} -n %{srcname}-%{version}
sed -i 's|-0-2||g' %{srcname}*/*.pro usb-device-formatter/usb-device-formatter.pro
sed -i 's|lrelease|lrelease-qt5|g' %{srcname}*/generate_translations.sh usb-device-formatter/generate_translations.sh
sed -i 's|qmake|qmake-qt5|g' vendor/prebuild

%build
%qmake_qt5 PREFIX=%{_prefix} QMAKE_CFLAGS_ISYSTEM=
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%{_bindir}/dde-*
%{_bindir}/usb-device-formatter*
%{_datadir}/%{srcname}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/dman/*/
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/polkit-1/actions/*.policy
%{_datadir}/usb-device-formatter/
%{_libdir}/*.so.*
%{_sysconfdir}/dbus-1/system.d/*.conf
%{_sysconfdir}/xdg/autostart/*.desktop

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Thu Mar 09 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.4.1-1
- Update package to 1.4.1
* Sun Jan 22 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.3.8-1
- Update package to 1.3.8
* Sat Jan 21 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.3.7-1
- Update package to 1.3.7
* Thu Jan 12 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.3.6-3
- Fixed broken icon link noticed by Brenton Horne <brentonhorne77@gmail.com>
* Fri Jan 06 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.3.6-2
- Fixed build dependecies
* Fri Dec 30 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.3.6-1
- Update package to 1.3.6 and rename to deepin-file-manager
* Mon Dec 19 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.3.4-1
- Update package to 1.3.4
* Mon Oct 10 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.3.3-1
- Update package to 1.3.3
* Mon Oct 10 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.2.3-1
- Initial package build