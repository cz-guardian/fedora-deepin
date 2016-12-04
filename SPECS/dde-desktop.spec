Name:           dde-desktop
Version:        3.0.15
Release:        2%{?dist}
Summary:        Deepin desktop-environment - Desktop module

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       deepin-file-manager-backend gtk2 qt5-qtsvg deepin-nautilus-properties deepin-tool-kit deepin-menu dde-dock gsettings-qt deepin-nautilus-properties qt5-qtx11extras libqtxdg
BuildRequires:  qt5-qttools-devel boost-devel libqtxdg-devel gtk2-devel xcb-util-wm-devel gsettings-qt deepin-tool-kit qt5-qtx11extras-devel

Provides:       %{name}

%global debug_package %{nil}

%description
Deepin desktop-environment - Desktop module


%prep
%autosetup %{version}.tar.gz#%{name}

%build

%define _lib_dir %{nil}
%ifarch x86_64
  %define _lib_dir %{_usr}/lib64
%endif
%ifarch i386 i686
  %define _lib_dir %{_usr}/lib
%endif

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
* Sun Dec 04 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.15-2
- Rebuild with newer deepin-tool-kit
* Sun Oct 02 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.15-1
- Initial package build