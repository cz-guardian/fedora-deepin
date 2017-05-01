Name:           deepin-screenshot
Version:        3.1.15
Release:        1%{?dist}
Summary:        Easy-to-use screenshot tool for linuxdeepin desktop environment
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       deepin-menu
Requires:       deepin-qml-widgets
Requires:       gnome-python2-libwnck
Requires:       python-qt5
Requires:       python2-xpybutil
Requires:       qt5-qtdeclarative
Requires:       qt5-qtgraphicaleffects
Requires:       qt5-qtmultimedia
Requires:       qt5-qtquickcontrols
Requires:       qt5-qtsvg
BuildRequires:  deepin-gettext-tools
BuildRequires:  gettext
BuildRequires:  python-devel

BuildArch:      noarch

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%prep
%autosetup %{version}.tar.gz#%{name}

# fix python version
find -iname "*.py" | xargs sed -i '1s|python$|python2|'

%build
%make_build

%install
%make_install

%find_lang %{name}

%preun
if [ $1 -eq 0 ]; then
  /usr/sbin/alternatives --remove x-window-screenshot %{_bindir}/%{name}
fi

%post
if [ $1 -eq 1 ]; then
  /usr/sbin/alternatives --install %{_bindir}/x-window-screenshot \
    x-window-screenshot %{_bindir}/%{name} 20
fi

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/dman/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg


%changelog
* Mon May 01 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.15-1
- Update to 3.1.15
* Mon Apr 24 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.14-1
- Update to 3.1.14
* Fri Jan 27 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.10-3
- Rewrite of spec file
* Thu Jan 12 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.10-2
- Dependecy bump
* Sun Dec 11 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.10-1
- Initial package build
