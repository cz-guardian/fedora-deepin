Name:           dde-api
Version:        3.0.14
Release:        2%{?dist}
Summary:        Deepin GoLang API Library

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:		    gdk-pixbuf2-xlib poppler-glib librsvg2 libcanberra libgudev go-lib go-gir-generator deepin-metacity deepin-metacity dbus-factory
BuildRequires:  bzr gcc-go gdk-pixbuf2-xlib-devel poppler-glib-devel librsvg2-devel libcanberra-devel libgudev-devel git go-lib go-gir-generator deepin-metacity dbus-factory

Provides:       %{name}

#%global debug_package %{nil}

%description
Deepin GoLang API Library


%prep
%autosetup %{version}.tar.gz#%{name}

%build
export GOPATH="%{_builddir}/build:%{_builddir}:/usr/share/gocode/src/"

install -d -m 755 ../dde-api_src
cp -r ./* ../dde-api_src

make build-dep
go get gopkg.in/alecthomas/kingpin.v2
make

%install
export GOPATH="%{_builddir}/build:%{_builddir}:/usr/share/gocode/src/"
make DESTDIR="%{buildroot}" SYSTEMD_LIB_DIR=/usr/lib install

install -d -m 755 %{buildroot}/usr/src/pkg.deepin.io/dde/api
cp -r %{_builddir}/dde-api_src/* %{buildroot}/usr/src/pkg.deepin.io/dde/api/

%clean
rm -rf %{buildroot}
rm -rf %{_builddir}/dde-api_src/

%files
%{_prefix}/src/*
%{_prefix}/lib/*
%{_prefix}/share/*


%changelog
* Wed Dec 07 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.14-2
- Changed compilation procedure
* Wed Sep 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.14-1
- Initial package build