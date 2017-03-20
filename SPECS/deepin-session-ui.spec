%global         srcname dde-session-ui

Name:           deepin-session-ui
Version:        4.0.1
Release:        1%{?dist}
Summary:        Deepin desktop-environment - Session UI module
License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       deepin-control-center
Requires:       deepin-daemon
Requires:       startdde
Requires:       lightdm
BuildRequires:  deepin-tool-kit-devel
BuildRequires:  deepin-qt-dbus-factory-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  gtk2-devel
BuildRequires:  lightdm-qt5-devel
BuildRequires:  pam-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  systemd-devel

Provides:       %{name}%{?_isa} = %{version}-%{release}
Provides:       lightdm-deepin-greeter%{?_isa} = %{version}-%{release}
Provides:       %{srcname}%{?_isa} = %{version}-%{release}
Obsoletes:      %{srcname}%{?_isa} < %{version}-%{release}

%description
%{summary}

%prep
%setup %{version}.tar.gz#%{name} -q -n %{srcname}-%{version}
sed -i 's/lrelease/lrelease-qt5/g' translate_generation.sh

sed -i 's/lib/libexec/' \
    misc/applications/deepin-toggle-desktop.desktop \
    dde-osd/com.deepin.dde.osd.service \
    dde-offline-upgrader/dde-offline-upgrader.pro \
    dde-wallpaper-chooser/dde-wallpaper-chooser.pro \
    dde-suspend-dialog/dde-suspend-dialog.pro \
    dde-lowpower/dde-lowpower.pro \
    dde-osd/dde-osd.pro \
    dde-zone/dde-zone.pro \
    dde-zone/mainwindow.h

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

install -d %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d
cat > %{buildroot}%{_sysconfdir}/lightdm/lightdm.conf.d/deepin.conf <<EOF
[Seat:*]
greeter-session=lightdm-deepin-greeter
EOF

%clean
rm -rf %{buildroot}

%files
%doc README.md
%license LICENSE
%config(noreplace) %{_sysconfdir}/lightdm/lightdm.conf.d/deepin.conf
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/com.deepin.dde.lock.conf
%{_bindir}/*
%{_libexecdir}/deepin-daemon/*
%{_datadir}/%{srcname}/*
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/xgreeters/*.desktop

%changelog
* Mon Mar 20 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.1-1
- Update to version 4.0.1
* Sun Jan 22 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.23-1
- Update to version 3.0.23
* Sun Dec 11 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.22-1
- Initial package build
