Name:           deepin-tool-kit
Version:        0.1.6
Release:        1%{?dist}
Summary:        Base development tool of all C++/Qt Developer work on Deepin

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       qt5-qtmultimedia qt5-qtx11extras startup-notification xcb-util
BuildRequires:  xcb-util-devel qt5-qtmultimedia-devel qt5-qtx11extras-devel startup-notification-devel

Provides:       %{name}

%global debug_package %{nil}

%description
Base development tool of all C++/Qt Developer work on Deepin


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

qmake-qt5 PREFIX=%{buildroot}/usr
make

%install
make INSTALL_ROOT="%{buildroot}" install
%ifarch x86_64
  rm -rf %{buildroot}/usr/lib64/qt5
  mv %{buildroot}/usr/lib/* %{buildroot}/usr/lib64/
  rmdir %{buildroot}/usr/lib/
%endif
%ifarch i386 i686
  rm -rf %{buildroot}/usr/lib64/
%endif

%clean
rm -rf %{buildroot}

%files
#%{_bindir}/*
%{_usr}/include/*
%{_lib_dir}/*
#%{_datarootdir}/*


%changelog
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build