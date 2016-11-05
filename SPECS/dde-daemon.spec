Name:           dde-daemon
Version:        3.0.23
Release:        1%{?dist}
Summary:        Daemon handling the DDE session settings

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
Source1:        dde-daemon.sysusers
Source2:        polkit-gnome-authentication-agent-1-deepin.desktop
    
Requires:       deepin-desktop-schemas gvfs libcanberra deepin-notifications upower libxkbfile deepin-desktop-base bamf libgnome-keyring pulseaudio qt5-qtaccountsservice libudisks2 polkit-gnome mobile-broadband-provider-info iso-codes bluez-libs acpid rfkill poppler-glib dde-api
BuildRequires:  go-dbus-generator go-gir-generator dde-api librsvg2-devel pulseaudio-libs-devel libXtst-devel gdk-pixbuf2-xlib-devel gcc-go git dbus-factory go-lib libcanberra-devel bamf-devel libgudev-devel systemd-devel gettext

Provides:       %{name}

%description
Daemon handling the DDE session settings


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

export GOPATH="$(pwd)/build"

go get github.com/BurntSushi/xgb github.com/BurntSushi/xgbutil github.com/howeyc/fsnotify \
  github.com/mattn/go-sqlite3 gopkg.in/alecthomas/kingpin.v2 github.com/disintegration/imaging \
  github.com/BurntSushi/freetype-go/freetype github.com/BurntSushi/freetype-go/freetype/truetype \
  github.com/BurntSushi/graphics-go/graphics

make

%install
make DESTDIR="%{buildroot}" install
install -Dm644 %{_sourcedir}/dde-daemon.sysusers "%{buildroot}/usr/lib/sysusers.d/deepin-daemon.conf"
install -Dm644 %{_sourcedir}/polkit-gnome-authentication-agent-1-deepin.desktop "%{buildroot}/etc/xdg/autostart/polkit-gnome-authentication-agent-1-deepin.desktop"

%post
systemd-sysusers deepin-daemon.conf

%preun
rm -f /var/cache/deepin/mark-setup-network-services

%clean
rm -rf %{buildroot}

%files
%{_datarootdir}/*
%{_prefix}/lib/*
%{_var}/cache/*
%{_sysconfdir}/xdg/autostart/polkit-gnome-authentication-agent-1-deepin.desktop


%changelog
* Mon Oct 31 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.23-1
- Upgrade to version 3.0.23
* Sun Sep 25 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.22-1
- Initial package build