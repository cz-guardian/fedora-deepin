%global 		srcname dde-dock

Name:           deepin-dock
Version:        4.1.7
Release:        1%{?dist}
Summary:        Deepin desktop-environment - Dock module
License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/v%{version}.tar.gz#%{name}
    
BuildRequires:  deepin-tool-kit-devel
BuildRequires:  deepin-qt-dbus-factory-devel
BuildRequires:  gtk2-devel
BuildRequires:  libXtst-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-image-devel

Provides:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{srcname}%{?_isa} = %{version}-%{release}
Obsoletes:      %{srcname}%{?_isa} < %{version}-%{release}

%description
%{summary}


%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}


%prep
%setup v%{version}.tar.gz#%{name} -q -n %{srcname}-%{version}

sed -i 's/lrelease/lrelease-qt5/g' translate_generation.sh
sed -i '/target.path/s|lib|%{_lib}|' plugins/*/*.pro
sed -i 's|lib|%{_lib}|' frame/controller/dockpluginloader.cpp

%build
%qmake_qt5 PREFIX=%{_prefix}
#%make_build
make

%install
%make_install INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*

%files devel
%{_includedir}/*

%changelog
* Sun Mar 19 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.1.7-1
- Update to version 4.1.7
* Thu Mar 09 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.1.4-1
- Update to version 4.1.4
* Sat Jan 21 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.8-1
- Update to version 4.0.8
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.7-1
- Update to version 4.0.7 and renamed to deepin-dock
* Mon Dec 19 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.6-1
- Update to version 4.0.6
* Sun Dec 04 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.5-2
- Rebuild with newer deepin-tool-kit
* Sun Oct 02 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.5-1
- Initial package build