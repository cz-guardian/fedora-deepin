%global 		srcname dde-control-center

Name:           deepin-control-center
Version:        4.0.2
Release:        1%{?dist}
Summary:        New control center for linux deepin
License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
Patch0:         deepin-control-center-4.0.2-disable-update.patch

Requires:       deepin-account-faces
Requires:       deepin-api
Requires:       deepin-daemon
Requires:       GeoIP-GeoLite-data
Requires:       GeoIP-GeoLite-data-extra
Requires:       startdde
Requires:       gtk-murrine-engine
BuildRequires:  deepin-tool-kit-devel
BuildRequires:  deepin-dock-devel
BuildRequires:  deepin-qt-dbus-factory-devel
BuildRequires:  GeoIP-devel
BuildRequires:  gtk2-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  desktop-file-utils

Provides:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{srcname}%{?_isa} < %{version}-%{release}

%description
%{summary}


%prep
%autosetup %{version}.tar.gz#%{name} -n %{srcname}-%{version} -p1
sed -i 's/lrelease/lrelease-qt5/g' translate_generation.sh

# Fix lib paths
find -name '*.pro' | xargs sed -i -e '/target.path/s|lib|%{_lib}|' \
	-e '/utils.path/s|lib|%{_lib}|'

sed -i '/%{srcname}/s|lib|%{_lib}|' plugins/notify/notifydata.cpp
sed -i '/deepin-daemon/s|lib|libexec|' modules/update/updatemodule.cpp

%build
%qmake_qt5 QMAKE_CFLAGS_ISYSTEM= PREFIX=%{_prefix} WITH_MODULE_GRUB=NO WITH_MODULE_REMOTE_ASSIST=NO WITH_MODULE_SYSINFO_UPDATE=NO
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_libdir}/%{srcname}/plugins/*
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/%{srcname}/*

%changelog
* Mon Jan 23 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.2-1
- Update to version 4.0.2
* Tue Dec 27 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.24-2
- Bump to newer release because of copr signature
* Fri Dec 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.24-1
- Upgrade to 3.0.24
* Sun Oct 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.21-1
- Initial package build