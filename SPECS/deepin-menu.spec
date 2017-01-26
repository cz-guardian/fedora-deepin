Name:           deepin-menu
Version:        3.0.7
Release:        2%{?dist}
Summary:        Deepin menu service for building beautiful menus
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       python-qt5
Requires:       qt5-qtx11extras
BuildRequires:  desktop-file-utils
BuildRequires:  python-devel
BuildRequires:  python2-setuptools
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtx11extras-devel

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%prep
%autosetup %{version}.tar.gz#%{name}

# fix python version
find -iname "*.py" | xargs sed -i '1s|python$|python2|'

sed -i '/target.path/s|lib|libexec|' deepin-menu.pro

%build
%{__python2} setup.py build
%{qmake_qt5} DEFINES+=QT_NO_DEBUG_OUTPUT
%{make_build}

%install
%{__python2} setup.py install -O1 --skip-build --prefix=%{_prefix} --root=%{buildroot}
%{make_install} INSTALL_ROOT="%{buildroot}"

rm -rf %{buildroot}/usr/deepin_menu
install -d %{buildroot}%{_datadir}/dbus-1/services/
install -d %{buildroot}%{_datadir}/applications/
install -d %{buildroot}/etc/xdg/autostart/

# Modify lib path to reflect the platform
sed -i 's|/usr/lib|%{_libexecdir}|' com.deepin.menu.service deepin-menu.desktop

install -m644 *.service %{buildroot}%{_datadir}/dbus-1/services/
install -m644 *.desktop %{buildroot}%{_datadir}/applications/
ln -sfv %{_datadir}/applications/%{name}.desktop %{buildroot}%{_sysconfdir}/xdg/autostart/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_sysconfdir}/xdg/autostart/*.desktop
%{_libexecdir}/*
%{python_sitelib}/*
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service

%changelog
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