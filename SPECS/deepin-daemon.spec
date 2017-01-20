%global         srcname dde-daemon

Name:           deepin-daemon
Version:        3.0.25.2
Release:        1%{?dist}
Summary:        Daemon handling the DDE session settings

License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
Source1:        dde-daemon.sysusers
Source2:        polkit-gnome-authentication-agent-1-deepin.desktop
#Patch0:         dde-daemon_3.0.24_fix-compile.patch
    
Requires:       deepin-desktop-schemas gvfs libcanberra deepin-notifications upower libxkbfile deepin-desktop-base bamf libgnome-keyring pulseaudio qt5-qtaccountsservice libudisks2 polkit-gnome mobile-broadband-provider-info iso-codes bluez-libs acpid rfkill poppler-glib deepin-api libinput
BuildRequires:  deepin-go-dbus-generator deepin-go-gir-generator deepin-api librsvg2-devel pulseaudio-libs-devel libXtst-devel gdk-pixbuf2-xlib-devel golang-bin git deepin-dbus-factory deepin-go-lib libcanberra-devel bamf-devel libgudev-devel systemd-devel gettext libinput-devel golang-github-BurntSushi-xgb-devel golang-github-BurntSushi-xgbutil-devel golang-github-howeyc-fsnotify-devel golang-github-mattn-go-sqlite3-devel

Provides:       %{name}
Provides:       %{srcname}

Obsoletes:      %{srcname} < 3.0.25.2-1

%description
Daemon handling the DDE session settings


%prep
%setup %{version}.tar.gz#%{name} -q -n %{srcname}-%{version}

%build

%define _lib_dir %{nil}
%ifarch x86_64
  %define _lib_dir %{_usr}/lib64
%endif
%ifarch i386 i686
  %define _lib_dir %{_usr}/lib
%endif

export GOPATH="$(pwd)/build:%{gopath}"

go get gopkg.in/alecthomas/kingpin.v2 \
  github.com/disintegration/imaging \
  github.com/BurntSushi/freetype-go/freetype \
  github.com/BurntSushi/freetype-go/freetype/truetype \
  github.com/BurntSushi/graphics-go/graphics \
  github.com/fsnotify/fsnotify \
  golang.org/x/sys/unix

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