Name:           deepin-tool-kit
Version:        0.2.0
Release:        1%{?dist}
Summary:        Base development tool of all C++/Qt Developer work on Deepin

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       qt5-qtmultimedia qt5-qtx11extras startup-notification xcb-util libXrender
BuildRequires:  xcb-util-devel qt5-qtmultimedia-devel qt5-qtx11extras-devel startup-notification-devel qt5-qtbase-static libXrender-devel

Provides:       %{name}

%global debug_package %{nil}

%description
Base development tool of all C++/Qt Developer work on Deepin


%prep
%autosetup %{version}.tar.gz#%{name}

%build

sed -i 's/lrelease/lrelease-qt5/g' tool/translate_generation.sh
qmake-qt5 PREFIX=/usr
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
%{_usr}/include/*
%{_libdir}/*

%changelog
* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.2.0-1
- Updated package to 1.7
* Sat Dec 03 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.7-1
- Updated package to 1.7
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.6-1
- Initial package build