Name:           deepin-image-viewer
Version:        1.1.3
Release:        2%{?dist}
Summary:        Deepin Image Viewer

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       deepin-tool-kit freeimage LibRaw libexif xcb-util startup-notification qt5-qtx11extras qt5-qtsvg
BuildRequires:  qt5-qttools-devel deepin-tool-kit-devel freeimage-devel LibRaw-devel libexif-devel xcb-util-devel startup-notification-devel qt5-qtx11extras-devel qt5-qtsvg-devel

Provides:       %{name}

#%global debug_package %{nil}

%description
%{summary}


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

sed -i 's/lrelease/lrelease-qt5/g' viewer/generate_translations.sh
sed -i 's|#include <exif-data.h>|#include <libexif/exif-data.h>|' viewer/utils/imageutils_libexif.h
qmake-qt5 PREFIX=%{_prefix} QMAKE_CFLAGS_ISYSTEM=
make

%install
make INSTALL_ROOT="%{buildroot}" install

# Fix broken /share folder
mv %{buildroot}/share/kde4 %{buildroot}/usr/share/kde4
rmdir %{buildroot}/share

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datarootdir}/*
%{_lib_dir}/*

%changelog
* Fri Jan 06 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.3-2
- Fixed build dependecies
* Sat Dec 10 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.3-1
- Initial package build