Name:           dbus-factory
Version:        3.0.8
Release:        1%{?dist}
Summary:        QML DBus factory for DDE

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildRequires:  go-dbus-generator gcc-go

Provides:       %{name}

%description
QML DBus factory for DDE


%prep
%autosetup -p1 %{version}.tar.gz#%{name}

make

%install
%make_install GOPATH="%{_datadir}/gocode" DESTDIR="%{buildroot}" install

%clean
rm -rf %{buildroot}

%files
%{_datadir}/gocode/*


%changelog
* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.8-1
- Update to version 3.0.8
* Thu Sep 29 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.6-2
- Compilation rework
* Wed Sep 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.6-1
- Initial package build