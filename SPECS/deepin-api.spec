%global     srcname dde-api

Name:           deepin-api
Version:        3.0.16.1
Release:        2%{?dist}
Summary:        Deepin GoLang API Library
License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       deepin-desktop-base
Requires:       rfkill
BuildRequires:  bzr
BuildRequires:  git
BuildRequires:  gcc-go
BuildRequires:  gtk3-devel
BuildRequires:  gdk-pixbuf2-xlib-devel
BuildRequires:  cairo-devel
BuildRequires:  libXi-devel
BuildRequires:  libcroco-devel
BuildRequires:  libcanberra-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libgudev-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  deepin-go-gir-generator
BuildRequires:  deepin-go-lib
BuildRequires:  deepin-dbus-factory
BuildRequires:  golang-github-BurntSushi-xgb-devel
BuildRequires:  golang-github-BurntSushi-xgbutil-devel
BuildRequires:  golang-github-go-fsnotify-fsnotify-devel

Provides:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{srcname}%{?_isa} = %{version}-%{release}
Obsoletes:      %{srcname}%{?_isa} < %{version}-%{release}

%description
%{summary}


%package devel
Summary:        Development package for %{name}

%description devel
Header files and libraries for %{name}


%prep
%setup %{version}.tar.gz#%{name} -q -n %{srcname}-%{version}

sed -i 's;/usr/lib;%{_libexecdir};' misc/*services/*.service misc/systemd/system/deepin-shutdown-sound.service thumbnails/gtk/gtk.go
sed -i 's/libdir/LIBDIR/g' Makefile

install -d %{buildroot}%{gopath}/src/pkg.deepin.io/dde/api
cp -r * %{buildroot}%{gopath}/src/pkg.deepin.io/dde/api/

%build
export GOPATH="$(pwd)/build:%{gopath}"

#make build-dep
go get github.com/disintegration/imaging \
    github.com/howeyc/fsnotify \
    launchpad.net/gocheck \
    gopkg.in/alecthomas/kingpin.v2

%make_build

%install
export GOPATH="$(pwd)/build:%{gopath}"
%make_install SYSTEMD_LIB_DIR="/usr/lib" LIBDIR="/libexec"

%clean
rm -rf %{buildroot}

%files
%{_libexecdir}/%{name}/*
%{_unitdir}/*.service
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/icons/hicolor/*/actions/*

%files devel
%{gopath}/src/pkg.deepin.io/dde/api/

%changelog
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