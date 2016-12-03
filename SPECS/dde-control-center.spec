Name:           dde-control-center
Version:        3.0.21
Release:        1%{?dist}
Summary:        New control center for linux deepin

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       deepin-tool-kit desktop-file-utils gtk2 dde-account-faces dde-api dde-daemon dbus-factory startdde qt5-qtmultimedia qt5-qtx11extras
BuildRequires:  qt5-qttools-devel dde-dock gtk2-devel qt5-qtsvg-devel qt5-qtmultimedia-devel qt5-qtx11extras-devel

Provides:       %{name}

%global debug_package %{nil}

%description
New control center for linux deepin


%prep
%autosetup %{version}.tar.gz#%{name}

%build
sed -i 's/lrelease/lrelease-qt5/g' translate_generation.sh

qmake-qt5 QMAKE_CFLAGS_ISYSTEM= PREFIX=%{_usr} WITH_MODULE_GRUB=NO WITH_MODULE_REMOTE_ASSIST=NO WITH_MODULE_SYSINFO_UPDATE=NO
make

%install
make INSTALL_ROOT="%{buildroot}" install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datarootdir}/*
%{_exec_prefix}/lib/*


%changelog
* Sun Oct 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.21-1
- Initial package build