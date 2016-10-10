Name:           dde-file-manager
Version:        1.2.3
Release:        1%{?dist}
Summary:        Deepin File Manager

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       deepin-tool-kit gtk2 deepin-shortcut-viewer file qt5-qtsvg libsecret gsettings-qt
BuildRequires:  qt5-qttools-devel libsecret-devel file-devel

Provides:       %{name}

%global debug_package %{nil}

%description
Deepin File Manager


%prep
%autosetup %{version}.tar.gz#%{name}

%build
sed -i 's/lrelease/lrelease-qt5/g' generate_translations.sh
sed -i 's/qmake/qmake-qt5/g' vendor/prebuild

%define _lib_dir %{nil}
%ifarch x86_64
  %define _lib_dir %{_usr}/lib64
%endif
%ifarch i386 i686
  %define _lib_dir %{_usr}/lib
%endif

qmake-qt5 QMAKE_CFLAGS_ISYSTEM= PREFIX=%{_usr}
make

%install
make INSTALL_ROOT="%{buildroot}" install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datarootdir}/*
%{_sysconfdir}/xdg/autostart/*


%changelog
* Mon Oct 10 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.2.3-1
- Initial package build