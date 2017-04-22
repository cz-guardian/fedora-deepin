%global         srcname dde-daemon

Name:           deepin-daemon
Version:        3.1.9
Release:        1%{?dist}
Summary:        Daemon handling the DDE session settings
License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
Source1:        dde-daemon.sysusers
Source2:        polkit-gnome-authentication-agent-1-deepin.desktop
    
Requires:       acpid
Requires:       bluez-libs
Requires:       deepin-desktop-base
Requires:       deepin-desktop-schemas
Requires:       deepin-grub2-themes
Requires:       deepin-notifications
Requires:       gvfs
Requires:       libudisks2
Requires:       polkit-gnome
Requires:       qt5-qtaccountsservice
Requires:       rfkill
Requires:       upower
Requires:       xdotool
Recommends:     iso-codes
Recommends:     mobile-broadband-provider-info
Recommends:     NetworkManager-l2tp-gnome
Recommends:     NetworkManager-openconnect-gnome
Recommends:     NetworkManager-openvpn-gnome
Recommends:     NetworkManager-pptp-gnome
Recommends:     NetworkManager-strongswan-gnome
Recommends:     NetworkManager-vpnc-gnome
BuildRequires:  deepin-api-devel
BuildRequires:  deepin-go-gir-generator
BuildRequires:  deepin-dbus-factory
BuildRequires:  deepin-go-lib
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  golang
BuildRequires:  golang-github-BurntSushi-xgb-devel
BuildRequires:  golang-github-BurntSushi-xgbutil-devel
BuildRequires:  golang-github-howeyc-fsnotify-devel
BuildRequires:  golang-github-mattn-go-sqlite3-devel
BuildRequires:  libgnome-keyring-devel
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libbamf3)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  poppler-glib-devel
BuildRequires:  systemd-devel

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{srcname}
Provides:       %{srcname}%{?_isa} = %{version}-%{release}
Obsoletes:      %{srcname} < 3.0.25.2-1
Obsoletes:      %{srcname}%{?_isa} < 3.0.25.2-1

%description
%{summary}


%prep
%setup %{version}.tar.gz#%{name} -q -n %{srcname}-%{version}

# Fix library exec path
sed -i '/deepin/s|lib|libexec|' Makefile
sed -i 's|/usr/lib|%{_libexecdir}|' \
    misc/*services/*.service \
    misc/applications/deepin-toggle-desktop.desktop \
    misc/dde-daemon/keybinding/system_actions.json \
    keybinding/shortcuts/system_shortcut.go \
    session/power/constant.go \
    session/power/lid_switch.go \
    bin/dde-system-daemon/main.go \
    bin/search/main.go \
    accounts/user.go

# Fix grub.cfg path
sed -i '/MenuFile/s|grub/|grub2/|' grub2/grub2.go

%build
export GOPATH="$(pwd)/build:%{gopath}"

go get gopkg.in/alecthomas/kingpin.v2 \
  github.com/disintegration/imaging \
  github.com/BurntSushi/freetype-go/freetype \
  github.com/BurntSushi/freetype-go/freetype/truetype \
  github.com/BurntSushi/graphics-go/graphics \
  github.com/fsnotify/fsnotify \
  golang.org/x/sys/unix

%make_build

%install
%make_install
install -Dm644 %{S:1} %{buildroot}/usr/lib/sysusers.d/deepin-daemon.conf
install -Dm644 %{S:2} %{buildroot}/etc/xdg/autostart/polkit-gnome-authentication-agent-1-deepin.desktop

%find_lang %{srcname}

%post
systemd-sysusers deepin-daemon.conf

%preun
rm -f /var/cache/deepin/mark-setup-network-services

%clean
rm -rf %{buildroot}

%files -f %{srcname}.lang
%doc README.md
%license LICENSE
%{_datadir}/%{srcname}/*
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/dde/data/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/polkit-1/actions/*.policy
%{_libexecdir}/%{name}/
%{_prefix}/lib/sysusers.d/*.conf
%{_sysconfdir}/xdg/autostart/*.desktop
%{_var}/cache/appearance/thumbnail/*

%changelog
* Sat Apr 22 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 3.1.9-1
- Update to 3.1.9
* Sun Apr 09 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 3.1.7-1
- Update to 3.1.7
* Sat Mar 18 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.5-1
- Update to version 3.1.5
* Sun Mar 05 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.3-1
- Update to version 3.1.3
* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.25.2-1
- Rewrite of spec file
* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.25.2-1
- Updated to version 3.0.25.2
* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.24-2
- Changed GOLANG dependencies
* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.24-1
- Upgrade to version 3.0.24
* Mon Oct 31 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.23-1
- Upgrade to version 3.0.23
* Sun Sep 25 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.22-1
- Initial package build