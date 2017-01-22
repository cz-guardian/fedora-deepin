%global         srcname dde-launcher

Name:           deepin-launcher
Version:        4.0.4
Release:        1%{?dist}
Summary:        Deepin desktop-environment - Launcher module

License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       deepin-menu
Requires:       deepin-daemon
Requires:       deepin-file-manager-backend
Requires:       startdde
BuildRequires:  deepin-tool-kit-devel
BuildRequires:  deepin-qt-dbus-factory-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  gtk2-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  xcb-util-wm-devel

Provides:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{srcname}%{?_isa} = %{version}-%{release}
Obsoletes:      %{srcname}%{?_isa} < %{version}-%{release}

%description
%{summary}


%prep
%setup %{version}.tar.gz#%{name} -q -n %{srcname}-%{version}
sed -i 's/lrelease/lrelease-qt5/g' translate_generation.sh

%build
%qmake_qt5 PREFIX=%{_prefix} WITHOUT_UNINSTALL_APP=1
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datadir}/%{srcname}/*
%{_datadir}/dbus-1/services/*.service

%changelog
* Sun Jan 22 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.4-1
- Updated to version 4.0.4
* Sun Dec 04 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.3-1
- Updated to version 4.0.3
* Sat Oct 01 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.2-1
- Initial package build