Name:           dde-session-ui
Version:        3.0.22
Release:        1%{?dist}
Summary:        Deepin desktop-environment - Session UI module

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       deepin-tool-kit gsettings-qt dde-daemon dde-control-center startdde lightdm-qt5 qt5-qtsvg gtk2 qt5-qtx11extras pam
BuildRequires:  deepin-tool-kit gsettings-qt dde-daemon dde-control-center startdde lightdm-qt5-devel qt5-qtsvg-devel gtk2-devel qt5-qtx11extras-devel pam-devel

Provides:       %{name}

%global debug_package %{nil}

%description
Deepin desktop-environment - Session UI module

%prep
%autosetup %{version}.tar.gz#%{name}

%build

sed -i 's/lrelease/lrelease-qt5/g' translate_generation.sh
qmake-qt5 PREFIX=%{_prefix}
make

%install
make INSTALL_ROOT="%{buildroot}" install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_sysconfdir}/dbus-1/system.d/*
%{_datarootdir}/*
%{_exec_prefix}/lib/*

%changelog
* Sun Dec 11 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.22-1
- Initial package build