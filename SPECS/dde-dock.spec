Name:           dde-dock
Version:        4.0.5
Release:        1%{?dist}
Summary:        Deepin desktop-environment - Dock module

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       gtk2 qt5-qtsvg deepin-file-manager-backend deepin-tool-kit deepin-menu dde-daemon
BuildRequires:  qt5-qttools-devel xcb-util-image-devel

Provides:       %{name}

#%global debug_package %{nil}

%description
Deepin desktop-environment - Dock module


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
%ifarch x86_64
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_lib_dir}/*
%{_datarootdir}/*
%{_includedir}/*

%changelog
* Sun Oct 02 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.5-1
- Initial package build