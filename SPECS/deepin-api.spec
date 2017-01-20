%global     srcname dde-api

Name:           deepin-api
Version:        3.0.16.1
Release:        1%{?dist}
Summary:        Deepin GoLang API Library

License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:		    gdk-pixbuf2-xlib poppler-glib librsvg2 libcanberra libgudev deepin-go-lib deepin-go-gir-generator deepin-metacity deepin-dbus-factory
BuildRequires:  bzr gcc-go gdk-pixbuf2-xlib-devel poppler-glib-devel librsvg2-devel libcanberra-devel libgudev-devel git deepin-go-lib deepin-go-gir-generator deepin-metacity deepin-dbus-factory golang-github-BurntSushi-xgb-devel golang-github-BurntSushi-xgbutil-devel golang-github-howeyc-fsnotify-devel

Provides:       %{name}
Provides:       %{srcname}

Obsoletes:    %{srcname} < 3.0.16-1

#%global debug_package %{nil}

%description
%{summary}


%prep
%setup %{version}.tar.gz#%{name} -q -n %{srcname}-%{version}

%build
export GOPATH="%{_builddir}/build:%{_builddir}:%{gopath}"

install -d -m 755 ../dde-api_src
cp -r ./* ../dde-api_src

#make build-dep
go get github.com/disintegration/imaging
go get launchpad.net/gocheck
go get gopkg.in/alecthomas/kingpin.v2
make

%install
export GOPATH="%{_builddir}/build:%{_builddir}:%{gopath}"
make DESTDIR="%{buildroot}" SYSTEMD_LIB_DIR=/usr/lib install

install -d -m 755 %{buildroot}%{gopath}/src/pkg.deepin.io/dde/api
cp -r %{_builddir}/dde-api_src/* %{buildroot}%{gopath}/src/pkg.deepin.io/dde/api/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/dde-api_src/

%files
%{_prefix}/lib/*
%{gopath}/*
%{_datarootdir}/*


%changelog
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