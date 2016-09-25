Name:           deepin-notifications
Version:        2.3.8
Release:        1%{?dist}
Summary:        System notifications for linuxdeepin desktop environment

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       deepin-tool-kit qt5-qtsvg qt5-qtdeclarative gtk2
BuildRequires:  qt5-qtsvg-devel qt5-qtdeclarative-devel

Provides:       %{name}

#%global debug_package %{nil}

%description
System notifications for linuxdeepin desktop environment


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

qmake-qt5 PREFIX=%{_usr}
make

%install
make INSTALL_ROOT="%{buildroot}" install
%ifarch x86_64
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%clean
rm -rf %{buildroot}

%files
%{_datarootdir}/*
%{_lib_dir}/*


%changelog
* Sun Sep 25 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build