Name:           deepin-file-manager-backend
Version:        0.1.16
Release:        1%{?dist}
Summary:        Deepin file manager backend

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       deepin-metacity libcanberra poppler-glib
BuildRequires:  go-dbus-generator go-gir-generator libgo-devel poppler-glib-devel gcc-go git dbus-factory go-lib dde-api libcanberra-devel librsvg2-devel deepin-metacity gdk-pixbuf2-xlib-devel gettext

Provides:       %{name}

%global debug_package %{nil}

%description
Deepin file manager backend


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
export CGO_LDTHREAD=-lpthread
go get github.com/howeyc/fsnotify github.com/mattn/go-sqlite3 gopkg.in/alecthomas/kingpin.v2
make USE_GCCGO=0

%install
make DESTDIR="%{buildroot}" install
%ifarch x86_64
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
  sed -i 's:/usr/lib/deepin-daemon:/usr/lib64/deepin-daemon/:g' %{buildroot}/usr/share/dbus-1/services/*.service
%endif

%post
glib-compile-schemas /usr/share/glib-2.0/schemas/

%clean
rm -rf %{buildroot}

%files
%{_lib_dir}/*
%{_datarootdir}/*

%changelog
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.16-1
- Initial package build