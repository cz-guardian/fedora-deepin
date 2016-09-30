Name:           dbus-factory
Version:        3.0.6
Release:        1%{?dist}
Summary:        QML DBus factory for DDE

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
Patch0:         dbus-factory_3.0.6_fix-arch.patch

Requires:       qt5-qtdeclarative
BuildRequires:  go-dbus-generator 

Provides:       %{name}

%description
QML DBus factory for DDE


%prep
%autosetup -p1 %{version}.tar.gz#%{name}

%build
%define _lib_dir %{nil}
%ifarch x86_64
  %define _lib_dir %{_usr}/lib64
%endif
%ifarch i386 i686
  %define _lib_dir %{_usr}/lib
%endif

make

%install
%make_install DESTDIR="%{buildroot}" install
mv %{buildroot}/usr/lib/go/src/ %{buildroot}/usr/src/
rmdir %{buildroot}/usr/lib/go/
%ifarch x86_64
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%clean
rm -rf %{buildroot}

%files
%{_lib_dir}/*
%{_prefix}/src/*


%changelog
* Thu Sep 29 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.6-2
- Compilation rework
* Wed Sep 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.6-1
- Initial package build