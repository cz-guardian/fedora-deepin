Name:           deepin-manual
Version:        1.0.5
Release:        1%{?dist}
Summary:        Deepin User Manual

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
Patch0:         deepin-manual_1.0.5_angular.patch

Requires:       deepin-qml-widgets python3-qt5 pygobject2 python3-dae
BuildRequires:  npm sassc

Provides:       %{name}

#%global debug_package %{nil}

# Set correct python version
%global __python %{__python3}

%description
Deepin User Manual


%prep
%autosetup -p1 %{version}.tar.gz#%{name}

sed -e 's;ln -sf /usr/bin/nodejs ./symdir/node;;' \
      -e 's/sass /sassc /' \
      -e 's/--unix-newlines//' \
      -i Makefile

%build
make

%install
%make_install DESTDIR="%{buildroot}"
 
cp -r manual "%{buildroot}"/usr/share/dman/dman
rm -r "%{buildroot}"/usr/share/dman/dman-daemon/
rm "%{buildroot}"/etc/xdg/autostart/dman-daemon.desktop
rmdir "%{buildroot}"/etc{/xdg/autostart,/xdg,}

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datarootdir}/*

%changelog
* Wed Dec 21 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.5-1
- Initial package build