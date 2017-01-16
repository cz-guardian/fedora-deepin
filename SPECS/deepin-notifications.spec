Name:           deepin-notifications
Version:        2.3.9
Release:        1%{?dist}
Summary:        System notifications for linuxdeepin desktop environment

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       deepin-tool-kit qt5-qtsvg qt5-qtdeclarative gtk2
BuildRequires:  qt5-qtsvg-devel qt5-qtdeclarative-devel deepin-tool-kit-devel gtk2-devel

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

qmake-qt5 PREFIX=%{_usr}
make

%install
make INSTALL_ROOT="%{buildroot}" install
%ifarch x86_64
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
  sed -i 's:/usr/lib/deepin-notifications/deepin-notifications:/usr/lib64/deepin-notifications/deepin-notifications:g' %{buildroot}/usr/share/dbus-1/services/*.service
%endif

%clean
rm -rf %{buildroot}

%files
%{_datarootdir}/*
%{_lib_dir}/*


%changelog
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.9-1
- Updated to 2.3.9
* Thu Jan 05 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.8-4
- Fixed build dependecies
* Thu Dec 15 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.8-3
- Fixed path in dbus services
* Sun Dec 04 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.8-2
- Rebuild with newer deepin-tool-kit
* Sun Sep 25 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.8-1
- Initial package build