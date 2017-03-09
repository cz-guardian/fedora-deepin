Name:           deepin-menu
Version:        3.0.10
Release:        1%{?dist}
Summary:        Deepin menu service for building beautiful menus
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       python-qt5
BuildRequires:  deepin-qt-dbus-factory-devel
BuildRequires:  deepin-tool-kit-devel
BuildRequires:  desktop-file-utils
BuildRequires:  python2-devel
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

# Modify lib path to reflect the platform
sed -i 's|/usr/lib|%{_libexecdir}|' data/com.deepin.menu.service \
    deepin-menu.desktop deepin-menu.pro

# Fix setup.py install path
sed -i '/data_files/s|list_files.*)|"")|' setup.py

%build
%{__python2} setup.py build
%{qmake_qt5} DEFINES+=QT_NO_DEBUG_OUTPUT
%{make_build}

%install
%{__python2} setup.py install -O1 --skip-build --prefix=%{_prefix} --root=%{buildroot}
%{make_install} INSTALL_ROOT="%{buildroot}"

install -d %{buildroot}%{_datadir}/dbus-1/services/
install -m644 data/*.service %{buildroot}%{_datadir}/dbus-1/services/

install -d %{buildroot}%{_datadir}/applications/
desktop-file-install --remove-key=OnlyShowIn --mode=644 \
    --dir=%{buildroot}%{_datadir}/applications deepin-menu.desktop

install -d %{buildroot}/etc/xdg/autostart/
ln -sfv %{_datadir}/applications/%{name}.desktop \
    %{buildroot}%{_sysconfdir}/xdg/autostart/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%doc README.md
%license LICENSE
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/com.deepin.menu.service
%{_libexecdir}/*
%{_sysconfdir}/xdg/autostart/*.desktop
%{python_sitelib}/*

%changelog
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