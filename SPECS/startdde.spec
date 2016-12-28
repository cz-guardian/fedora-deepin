Name:           startdde
Version:        3.0.13
Release:        2%{?dist}
Summary:        Starter of deepin desktop environment

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       dde-daemon deepin-wm-switcher
BuildRequires:  cmake coffee-script go-dbus-generator go-gir-generator libgo-devel python2 webkitgtk-devel gcc-go dbus-factory dde-api go-lib libcanberra-devel golang-github-BurntSushi-xgb-devel golang-github-BurntSushi-xgbutil-devel golang-github-howeyc-fsnotify-devel

Provides:       %{name}

%description
Starter of deepin desktop environment


%prep
%autosetup %{version}.tar.gz#%{name}

%build
export GOPATH="$(pwd)/build:%{gopath}"
make

%install
%make_install DESTDIR="%{buildroot}"
mv %{buildroot}/lib/* %{buildroot}/usr/lib/
rmdir %{buildroot}/lib/

# Fix broken symlink
rm -f %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/dde-readahead.service
ln -s /usr/lib/systemd/system/dde-readahead.service %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/dde-readahead.service

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datarootdir}/*
%{_usr}/lib/*

%changelog
* Wed Dec 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.13-2
- Updated GO dependencies
- Fixed wrong system path for dde-readahead
* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.13-1
- Update to package 3.0.13
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.12-1
- Update to package 3.0.12
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.11-1
- Initial package build