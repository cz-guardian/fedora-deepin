Name:           deepin-wm-switcher
Version:        1.1.0
Release:        1%{?dist}
Summary:        Window manager switcher for Deepin

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       dde-daemon deepin-wm deepin-metacity qt5-qtx11extras
BuildRequires:  cmake xcb-util-keysyms-devel

Provides:       %{name}

%description
Window manager switcher for Deepin


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

mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE=Release ../
make

%install
cd build
make DESTDIR="%{buildroot}" install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*


%changelog
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.0-1
- Update package to version 1.1.0
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.7-1
- Initial package build