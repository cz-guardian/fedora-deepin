Name:           startdde
Version:        3.0.11
Release:        1%{?dist}
Summary:        Starter of deepin desktop environment

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       dde-daemon deepin-wm-switcher
BuildRequires:  cmake coffee-script go-dbus-generator go-gir-generator libgo-devel python2 webkitgtk-devel

Provides:       %{name}

%description
Starter of deepin desktop environment


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
go get github.com/BurntSushi/xgb github.com/BurntSushi/xgbutil github.com/howeyc/fsnotify
make

%install
make DESTDIR="%{buildroot}" install
%ifarch x86_64
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif
mv %{buildroot}/lib %{buildroot}/usr/

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datarootdir}/*
%{_lib_dir}/*
%{_usr}/lib/*


%changelog
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.11-1
- Initial package build