%global     srcname dbus-factory

Name:           deepin-%{srcname}-qml306
Version:        3.0.6
Release:        1%{?dist}
Summary:        QML DBus factory 3.0.6 for DDE

License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildRequires:  go-dbus-generator gcc-go

Provides:       %{name}

%description
QML DBus factory 3.0.6 for DDE


%prep
%autosetup -p1 %{version}.tar.gz#%{name} -n %{srcname}-%{version}

%build
make build-qml

%install
%make_install QT5_LIBDIR="%{_libdir}/qt5" DESTDIR="%{buildroot}" install-qml

%clean
rm -rf %{buildroot}

%files
%{_libdir}/qt5/qml/*
%exclude /src/*

%changelog
* Fri Dec 23 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.6-1
- Initial package build