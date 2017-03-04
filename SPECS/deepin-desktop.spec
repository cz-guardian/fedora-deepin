%global         srcname dde-desktop

Name:           deepin-desktop
Version:        4.0.1
Release:        2%{?dist}
Summary:        Deepin desktop-environment - Desktop module
License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       deepin-menu
Requires:       deepin-dock
Requires:       deepin-daemon
Requires:       deepin-qt5integration
Requires:       startdde
BuildRequires:  boost-devel
BuildRequires:  deepin-file-manager-devel
BuildRequires:  deepin-tool-kit-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  gtk2-devel
BuildRequires:  libqtxdg-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  xcb-util-wm-devel

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{srcname}
Provides:       %{srcname}%{?_isa} = %{version}-%{release}
Obsoletes:      %{srcname} < %{version}-%{release}
Obsoletes:      %{srcname}%{?_isa} < %{version}-%{release}

%description
%{summary}


%prep
%setup %{version}.tar.gz#%{name} -q -n %{srcname}-%{version}
sed -i 's/-0-2//g' build.pri
sed -i 's/lrelease/lrelease-qt5/g' app/translate_generation.sh

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%doc README.md
%{_bindir}/*
%{_datadir}/%{srcname}/*
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service

%changelog
* Fri Jan 27 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.1-2
- Dependency fix
* Sat Jan 21 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.1-1
- Update to version 4.0.1
* Mon Dec 19 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.0-1
- Update to version 4.0.0
* Sun Dec 04 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.15-2
- Rebuild with newer deepin-tool-kit
* Sun Oct 02 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.15-1
- Initial package build