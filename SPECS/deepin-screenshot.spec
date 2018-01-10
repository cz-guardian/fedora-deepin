Name:           deepin-screenshot
Version:        4.0.10.4
Release:        1%{?dist}
Summary:        Deepin Screenshot Tool
License:        GPLv3
Url:            https://github.com/linuxdeepin/deepin-screenshot
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-appdata.xml

BuildRequires:  pkgconfig(dtkwidget) = 2.0
BuildRequires:  pkgconfig(dtkwm)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
Requires:       desktop-file-utils
Requires:       hicolor-icon-theme
Recommends:     deepin-shortcut-viewer

%description
Provide a quite easy-to-use screenshot tool. Features:
  * Global hotkey to triggle screenshot tool
  * Take screenshot of a selected area
  * Easy to add text and line drawings onto the screenshot

%prep
%setup -q

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}
install -Dm644 %SOURCE1 %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop ||:
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml

%preun
if [ $1 -eq 0 ]; then
  /usr/sbin/alternatives --remove x-window-screenshot %{_bindir}/%{name}
fi

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null ||:
/usr/bin/update-desktop-database -q ||:
if [ $1 -eq 1 ]; then
  /usr/sbin/alternatives --install %{_bindir}/x-window-screenshot \
    x-window-screenshot %{_bindir}/%{name} 20
fi

%postun
if [ $1 -eq 0 ]; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null ||:
    /usr/bin/gtk-update-icon-cache -f -t -q %{_datadir}/icons/hicolor ||:
fi
/usr/bin/update-desktop-database -q ||:

%posttrans
/usr/bin/gtk-update-icon-cache -f -t -q %{_datadir}/icons/hicolor ||:

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/dman/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/dbus-1/services/com.deepin.Screenshot.service
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/deepin/apps/scalable/%{name}.svg

%changelog
* Wed Jan 10 2018 Jaroslav <cz.guardian@gmail.com> Stepanek - 4.0.10.4-1
- Update to 4.0.10.4
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
