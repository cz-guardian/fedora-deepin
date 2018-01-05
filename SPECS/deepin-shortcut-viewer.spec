Name:           deepin-shortcut-viewer
Version:        1.3.3
Release:        1%{?dist}
Summary:        Deepin Shortcut Viewer
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-shortcut-viewer
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(dtkwidget) = 2.0
Provides:       bundled(CuteLogger)

%description
The program displays a shortcut key window when a JSON data is passed.

%prep
%setup -q

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT="%{buildroot}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Fri Jan 05 2018 Jaroslav <cz.guardian@gmail.com> Stepanek 1.3.3-1
- Updated to version 1.3.3
* Sun Dec 04 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.02-1
- Updated to version 1.02-1
* Mon Oct 10 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.01-1
- Initial package build