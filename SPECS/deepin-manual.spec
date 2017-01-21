# Set correct python version
%global __python %{__python3}
%global debug_package %{nil}

Name:           deepin-manual
Version:        1.0.6
Release:        1%{?dist}
Summary:        Deepin User Manual
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       deepin-qml-widgets
Requires:       python3-qt5
Requires:       pygobject2
Requires:       python3-dae
BuildRequires:  npm 
BuildRequires:  sassc

Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%prep
%autosetup -p1 %{version}.tar.gz#%{name}

sed -e 's;ln -sf /usr/bin/nodejs ./symdir/node;;' \
      -e 's/sass /sassc /' \
      -e 's/--unix-newlines//' \
      -i Makefile

%build
%make_build

%install
%make_install
 
cp -r manual %{buildroot}%{_datadir}/dman/dman
rm -r %{buildroot}%{_datadir}/dman/dman-daemon/
rm %{buildroot}/etc/xdg/autostart/dman-daemon.desktop
rmdir %{buildroot}/etc{/xdg/autostart,/xdg,}

%clean
rm -rf %{buildroot}

%files
%doc README.md
%{_bindir}/dman
%{_datadir}/%{name}/
%{_datadir}/dman/dman/
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%changelog
* Sat Jan 21 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.6-1
- Update to version 1.0.6
* Wed Dec 21 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.5-1
- Initial package build