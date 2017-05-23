%global srcname qt5integration

Name:           deepin-%{srcname}
Version:        0.1.8
Release:        1%{?dist}
Summary:        Qt platform theme integration plugins for DDE
License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildRequires:  atk-devel
BuildRequires:  cairo-devel
BuildRequires:  dbus-devel
BuildRequires:  deepin-tool-kit-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  libICE-devel
BuildRequires:  libinput-devel
BuildRequires:  libqtxdg-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  libXrender-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mtdev-devel
BuildRequires:  pango-devel
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-renderutil-devel
BuildRequires:  xcb-util-wm-devel

%description
%{summary}

%prep
%autosetup %{version}.tar.gz#%{name} -n %{srcname}-%{version}

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%{_qt5_plugindir}/platforms/*.so
%{_qt5_plugindir}/platformthemes/*.so
%{_qt5_plugindir}/styles/*.so

%changelog
* Tue May 23 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek - 0.1.8-1
- Updated to 0.1.8
* Sun Apr 23 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek - 0.1.7-1
- Updated to 0.1.7
* Mon Mar 20 2017 Jaroslav <cz.guardian@gmail.com> Stepanek - 0.1.3-1
- Updated to 0.1.3
* Mon Jan 23 2017 Jaroslav <cz.guardian@gmail.com> Stepanek - 0.0.6-1
- Initial build
