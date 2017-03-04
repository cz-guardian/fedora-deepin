Name:           deepin-wm-switcher
Version:        1.1.0
Release:        2%{?dist}
Summary:        Window manager switcher for Deepin
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       deepin-daemon
Requires:       deepin-metacity    
Requires:       deepin-wm
BuildRequires:  cmake
BuildRequires:  glib2-devel
BuildRequires:  libX11-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  xcb-util-keysyms-devel

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%prep
%autosetup %{version}.tar.gz#%{name}

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%make_build

%install
%make_install

%clean
rm -rf %{buildroot}

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%changelog
* Fri Jan 27 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.0-2
- Rewrite of spec file
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.0-1
- Update package to version 1.1.0
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.7-1
- Initial package build