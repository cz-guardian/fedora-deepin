%global debug_package %{nil}

Name:           deepin-file-manager-backend
Version:        0.1.16
Release:        2%{?dist}
Summary:        Deepin file manager backend
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
BuildRequires:  deepin-api-devel
BuildRequires:  deepin-dbus-factory
BuildRequires:  deepin-go-dbus-generator
BuildRequires:  deepin-go-gir-generator
BuildRequires:  deepin-go-lib
BuildRequires:  deepin-metacity-devel
BuildRequires:  gcc-go
BuildRequires:  gdk-pixbuf2-xlib-devel
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  golang-github-alecthomas-kingpin-devel
BuildRequires:  golang-github-howeyc-fsnotify-devel
BuildRequires:  golang-github-mattn-go-sqlite3-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libgo-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libX11-devel
BuildRequires:  poppler-glib-devel

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%prep
%autosetup %{version}.tar.gz#%{name}

sed -i 's/lib/libexec/' services/*.service
sed -i '3s/lib/libexec/' Makefile
sed -i 's/DFMB/%{name}/' locale/Makefile i18n.go

%build

%define _lib_dir %{nil}
%ifarch x86_64
  %define _lib_dir %{_usr}/lib64
%endif
%ifarch i386 i686
  %define _lib_dir %{_usr}/lib
%endif

export GOPATH="$(pwd)/build:%{gopath}"
export CGO_LDTHREAD=-lpthread
go get -u gopkg.in/alecthomas/kingpin.v2
make USE_GCCGO=0

%install
%make_install

%find_lang %{name}

%post
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas/

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_libexecdir}/deepin-daemon/*

%changelog
* Thu Jan 26 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.16-2
- Rewrite of spec file
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.16-1
- Initial package build