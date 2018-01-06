Name:           deepin-notifications
Version:        3.1.2
Release:        1%{?dist}
Summary:        System notifications for linuxdeepin desktop environment
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-notifications
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(dtkwidget) = 2.0
BuildRequires:  pkgconfig(gtk+-2.0)

%description
System notifications for linuxdeepin desktop environment.

%prep
%setup -q
sed -i 's|lib|libexec|' deepin-notifications.pro \
    files/com.deepin.Notifications.service.in

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{name}
%{_datadir}/dbus-1/services/com.deepin.Notifications.service

%changelog
* Fri Jan 05 2018 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 3.1.2-1
- Update to 3.1.2
* Sat Apr 22 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 3.0.4-1
- Update to 3.0.4
* Sun Apr 09 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.3-1
- Update to 3.0.3
* Sat Mar 18 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.2-1
- Updated to 3.0.2
* Sun Mar 05 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.0-1
- Updated to 3.0.0
* Sat Jan 21 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.10-1
- Updated to 2.3.10
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.9-1
- Updated to 2.3.9
* Thu Jan 05 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.8-4
- Fixed build dependecies
* Thu Dec 15 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.8-3
- Fixed path in dbus services
* Sun Dec 04 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.8-2
- Rebuild with newer deepin-tool-kit
* Sun Sep 25 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.8-1
- Initial package build