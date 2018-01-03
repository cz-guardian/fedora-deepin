%global repo dde-api
%global import_path pkg.deepin.io/dde/api

# out of memory on armv7hl
%ifarch %{arm}
%global _smp_mflags -j1
%endif

Name:           deepin-api
Version:        3.1.19
Release:        1%{?dist}
Summary:        Go-lang bingding for dde-daemon
License:        GPLv3+
URL:            https://github.com/linuxdeepin/dde-api
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
BuildRequires:  gcc-go
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo-ft)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xi)
BuildRequires:  deepin-gettext-tools
BuildRequires:  deepin-gir-generator
BuildRequires:  golang-deepin-dbus-factory-devel
BuildRequires:  golang(pkg.deepin.io/lib)
BuildRequires:  golang(github.com/BurntSushi/xgb)
BuildRequires:  golang(github.com/BurntSushi/xgbutil)
BuildRequires:  golang(github.com/disintegration/imaging)
BuildRequires:  golang(github.com/cryptix/wav)
BuildRequires:  golang(gopkg.in/alecthomas/kingpin.v2)
%{?systemd_requires}
Requires:       deepin-desktop-base
Requires:       rfkill

%description
Go-lang bingding for dde-daemon

%package -n golang-%{name}-devel
Summary:        %{summary}
BuildRequires:  golang(github.com/BurntSushi/xgb)
BuildRequires:  golang(github.com/BurntSushi/xgb/randr)
BuildRequires:  golang(github.com/BurntSushi/xgb/xproto)
BuildRequires:  golang(github.com/disintegration/imaging)
BuildRequires:  golang(github.com/nfnt/resize)
Requires:       golang(github.com/BurntSushi/xgb)
Requires:       golang(github.com/BurntSushi/xgb/randr)
Requires:       golang(github.com/BurntSushi/xgb/xproto)
Requires:       golang(github.com/disintegration/imaging)
Requires:       golang(github.com/nfnt/resize)
Provides:       golang(%{import_path}/blurimage) = %{version}-%{release}
Provides:       golang(%{import_path}/drandr) = %{version}-%{release}
Provides:       golang(%{import_path}/dxinput) = %{version}-%{release}
Provides:       golang(%{import_path}/dxinput/utils) = %{version}-%{release}
Provides:       golang(%{import_path}/i18n_dependent) = %{version}-%{release}
Provides:       golang(%{import_path}/lang_info) = %{version}-%{release}
Provides:       golang(%{import_path}/powersupply) = %{version}-%{release}
Provides:       golang(%{import_path}/powersupply/battery) = %{version}-%{release}
Provides:       golang(%{import_path}/session) = %{version}-%{release}
Provides:       golang(%{import_path}/soundutils) = %{version}-%{release}
Provides:       golang(%{import_path}/themes) = %{version}-%{release}
Provides:       golang(%{import_path}/themes/scanner) = %{version}-%{release}
Provides:       golang(%{import_path}/theme_thumb) = %{version}-%{release}
Provides:       golang(%{import_path}/theme_thumb/common) = %{version}-%{release}
Provides:       golang(%{import_path}/theme_thumb/cursor) = %{version}-%{release}
Provides:       golang(%{import_path}/theme_thumb/gtk) = %{version}-%{release}
Provides:       golang(%{import_path}/theme_thumb/icon) = %{version}-%{release}
Provides:       golang(%{import_path}/thumbnails) = %{version}-%{release}
Provides:       golang(%{import_path}/thumbnails/cursor) = %{version}-%{release}
Provides:       golang(%{import_path}/thumbnails/font) = %{version}-%{release}
Provides:       golang(%{import_path}/thumbnails/gtk) = %{version}-%{release}
Provides:       golang(%{import_path}/thumbnails/icon) = %{version}-%{release}
Provides:       golang(%{import_path}/thumbnails/images) = %{version}-%{release}
Provides:       golang(%{import_path}/thumbnails/loader) = %{version}-%{release}
Provides:       golang(%{import_path}/thumbnails/pdf) = %{version}-%{release}
Provides:       golang(%{import_path}/thumbnails/text) = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Obsoletes:      %{name}-devel < %{version}-%{release}

%description -n golang-%{name}-devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%prep
%setup -q -n %{repo}-%{version}

sed -i -e 's|/usr/lib|%{_libexecdir}|' misc/*services/*.service \
    misc/systemd/system/deepin-shutdown-sound.service \
    lunar-calendar/main.go \
    thumbnails/gtk/gtk.go 

sed -i 's|PREFIX}${libdir|LIBDIR|; s|libdir|LIBDIR|' Makefile

%build
export GOPATH="$(pwd)/build:%{gopath}"
%make_build

%install
export GOPATH="$(pwd)/build:%{gopath}"
%make_install SYSTEMD_SERVICE_DIR="%{_unitdir}" LIBDIR="%{_libexecdir}"

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null ||:
%systemd_post deepin-shutdown-sound.service

%preun
%systemd_preun deepin-shutdown-sound.service

%postun
if [ $1 -eq 0 ]; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null ||:
fi
%systemd_postun_with_restart deepin-shutdown-sound.service

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null ||:

%files
%doc README.md
%license LICENSE
%{_libexecdir}/%{name}/
%{_unitdir}/*.service
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/icons/hicolor/*/actions/*
%{_datadir}/dde-api/data/pkg_depends
%{_polkit_qt_policydir}/com.deepin.api.locale-helper.policy

%files -n golang-%{name}-devel
%{gopath}/src/%{import_path}/

%changelog
* Tue Jan 02 2018 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 3.1.19-1
- Update to version 3.1.19
* Wed Apr 19 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 3.1.7-1
- Update to version 3.1.7
* Sat Apr 08 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 3.1.6-1
- Update to version 3.1.6
* Sat Mar 18 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.4-2
- Rebuild
* Fri Mar 17 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.4-1
- Update to version 3.1.4
* Sun Mar 05 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.2-1
- Update to version 3.1.2
* Sat Jan 21 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.16.1-2
- Major spec rewrite
* Fri Jan 20 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.16.1-1
- Update to version 3.0.16.1
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.16-1
- Update to version 3.0.16
* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.15-1
- Update to version 3.0.15
* Wed Dec 07 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.14-2
- Changed compilation procedure
* Wed Sep 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.14-1
- Initial package build