Name:           deepin-menu
Version:        3.2.0
Release:        1%{?dist}
Summary:        Deepin menu service
License:        GPLv3+
URL:            https://github.com/linuxdeepin/deepin-menu
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(dtkwidget) = 2.0
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
Requires:       python-qt5

%description
Deepin menu service for building beautiful menus.

%prep
%setup -q

# Remove python shebang
find -iname "*.py" | xargs sed -i '/env python/d'

# Modify lib path to reflect the platform
sed -i 's|/usr/bin|%{_libexecdir}|' data/com.deepin.menu.service \
    deepin-menu.desktop deepin-menu.pro

# Fix setup.py install path
sed -i '/data_files/s|list_files.*)|"")|' setup.py

%build
%__python2 setup.py build
%qmake_qt5 DEFINES+=QT_NO_DEBUG_OUTPUT
%make_build

%install
%__python2 setup.py install -O1 --skip-build --prefix=%{_prefix} --root=%{buildroot}
%make_install INSTALL_ROOT="%{buildroot}"

install -d %{buildroot}%{_datadir}/dbus-1/services/
install -m644 data/*.service %{buildroot}%{_datadir}/dbus-1/services/

install -d %{buildroot}%{_datadir}/applications/
install -m644 %{name}.desktop %{buildroot}%{_datadir}/applications/

install -d %{buildroot}/etc/xdg/autostart/
ln -sfv ../../..%{_datadir}/applications/%{name}.desktop \
    %{buildroot}%{_sysconfdir}/xdg/autostart/

%files
%doc README.md
%license LICENSE
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_libexecdir}/%{name}
%{python_sitelib}/deepin_menu*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/com.deepin.menu.service

%changelog
* Sun Jan 07 2018 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek - 3.2.0-1
- Update package to 3.2.0
* Sat Apr 22 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 3.1.2-1
- Update package to 3.1.2
* Thu Mar 09 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.10-1
- Update package to 3.0.10
* Thu Jan 26 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.7-2
- Rewrite of spec file
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.7-1
- Update package to 3.0.7
* Fri Jan 06 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.6-3
- Fixed library path for autostart on x86_64 systems
* Sun Dec 11 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.6-2
- Fixed library path on x86_64 systems
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.6-1
- Initial package build