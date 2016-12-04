Name:           dde-launcher
Version:        4.0.3
Release:        1%{?dist}
Summary:        Deepin desktop-environment - Launcher module

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       gtk2 qt5-qtsvg qt5-qtx11extras deepin-file-manager-backend startdde deepin-tool-kit deepin-menu dde-daemon gsettings-qt
BuildRequires:  qt5-qttools-devel xcb-util-wm-devel deepin-tool-kit gsettings-qt gtk2-devel qt5-qtx11extras-devel qt5-qtsvg-devel

Provides:       %{name}

%global debug_package %{nil}

%description
Deepin desktop-environment - Launcher module


%prep
%autosetup %{version}.tar.gz#%{name}

%build
sed -i 's/lrelease/lrelease-qt5/g' translate_generation.sh
qmake-qt5 PREFIX=%{_prefix}
make

%install
make INSTALL_ROOT="%{buildroot}" install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datarootdir}/*

%changelog
* Sun Dec 04 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.3-1
- Updated to version 4.0.3
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.2-1
- Initial package build