Name:           dde-control-center
Version:        3.0.21
Release:        1%{?dist}
Summary:        New control center for linux deepin

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       deepin-tool-kit desktop-file-utils gtk2 dde-account-faces dde-api dde-daemon dbus-factory startdde
BuildRequires:  qt5-qttools-devel dde-dock

Provides:       %{name}

%global debug_package %{nil}

%description
New control center for linux deepin


%prep
%autosetup %{version}.tar.gz#%{name}

%build
sed -i 's/lrelease/lrelease-qt5/g' translate_generation.sh

%define _lib_dir %{nil}
%ifarch x86_64
  %define _lib_dir %{_usr}/lib64
%endif
%ifarch i386 i686
  %define _lib_dir %{_usr}/lib
%endif

qmake-qt5 QMAKE_CFLAGS_ISYSTEM= PREFIX=%{_usr} WITH_MODULE_GRUB=NO WITH_MODULE_REMOTE_ASSIST=NO WITH_MODULE_SYSINFO_UPDATE=NO
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
%{_datarootdir}/*
%{_lib_dir}/*


%changelog
* Sun Oct 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.21-1
- Initial package build