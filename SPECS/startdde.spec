Name:           startdde
Version:        3.1.2
Release:        1%{?dist}
Summary:        Starter of deepin desktop environment

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       deepin-daemon
Requires:       deepin-wm-switcher
BuildRequires:  cmake
BuildRequires:  coffee-script
BuildRequires:  deepin-api-devel
BuildRequires:  deepin-dbus-factory
BuildRequires:  deepin-go-gir-generator
BuildRequires:  deepin-go-lib
BuildRequires:  golang
BuildRequires:  golang-github-BurntSushi-xgb-devel
BuildRequires:  golang-github-BurntSushi-xgbutil-devel
BuildRequires:  golang-github-howeyc-fsnotify-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libgo-devel
BuildRequires:  webkitgtk-devel

Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%prep
%autosetup %{version}.tar.gz#%{name}
# Fix lib path
sed -i 's;/usr/lib;%{_libexecdir};g' Makefile session.go dde-readahead/dde-readahead.service
# Fix systemd path
sed -i 's;/lib/systemd;/usr/lib/systemd;g' Makefile

%build
export GOPATH="%{gopath}"
%make_build

%install
%make_install

# Fix broken symlink
rm -f %{buildroot}%{_unitdir}/multi-user.target.wants/dde-readahead.service
ln -s %{_unitdir}/dde-readahead.service %{buildroot}%{_unitdir}/multi-user.target.wants/dde-readahead.service

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_libexecdir}/*
%{_unitdir}/*
%{_datadir}/xsessions/*.desktop

%changelog
* Sun Mar 05 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.2-1
- Updated to 3.1.2
* Sat Jan 21 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.14.1-1
- Updated to 3.0.14.1
* Wed Dec 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.13-2
- Updated GO dependencies
- Fixed wrong system path for dde-readahead
* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.13-1
- Update to package 3.0.13
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.12-1
- Update to package 3.0.12
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.11-1
- Initial package build