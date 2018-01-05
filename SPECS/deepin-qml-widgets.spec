Name:           deepin-qml-widgets
Version:        2.3.6
Release:        1%{?dist}
Summary:        Deepin QML widgets
Group:          Development/Libraries
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-qml-widgets
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  deepin-gettext-tools
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(dtkwidget) = 2.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
Requires:       qt5-qtgraphicaleffects%{?_isa}
Requires:       qt5-qtquickcontrols%{?_isa}

%description
Extends QML by providing widgets that is used by Deepin applications.

%prep
%setup -q

%build
deepin-generate-mo locale/locale_config.ini
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

install -d %{buildroot}%{_datadir}/locale/
cp -r locale/mo/* %{buildroot}%{_datadir}/locale/

%find_lang %{name}

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/deepin-dialog
%{_qt5_qmldir}/Deepin/Locale/
%{_qt5_qmldir}/Deepin/StyleResources/
%{_qt5_qmldir}/Deepin/Widgets/
%{_datadir}/dbus-1/services/com.deepin.dialog.service

%changelog
* Fri Jan 27 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.6-1
- Update to 2.3.6
* Fri Jan 27 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.4-3
- Rewrite of spec file
* Thu Jan 12 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.4-2
- Bump to newer version because of copr
* Sun Dec 11 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.4-1
- Initial package build