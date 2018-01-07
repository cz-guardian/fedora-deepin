Name:           deepin-wm-switcher
Version:        1.1.9
Release:        1%{?dist}
Summary:        Window manager switcher for Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-wm-switcher
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake(Qt5)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(x11)
Requires:       deepin-daemon
Requires:       deepin-wm
Requires:       deepin-metacity

%description
Deepin Window Manager monitoring and auto-switching service.

It is capable of:

- monitoring health of 3d wm and falling back to 2d if bad things happened.
- detecting platform capability and choose 2d/3d wm accordingly.

%prep
%setup -q

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%make_build

%install
%make_install

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}

%changelog
* Sun Jan 07 2018 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.9-1
- Update to 1.1.9
* Fri Jan 27 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.0-2
- Rewrite of spec file
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.0-1
- Update package to version 1.1.0
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.7-1
- Initial package build