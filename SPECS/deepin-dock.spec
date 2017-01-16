%global 		srcname dde-dock

Name:           deepin-dock
Version:        4.0.7
Release:        1%{?dist}
Summary:        Deepin desktop-environment - Dock module

License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       gtk2 qt5-qtsvg deepin-file-manager-backend deepin-tool-kit deepin-menu dde-daemon
BuildRequires:  qt5-qttools-devel xcb-util-image-devel xcb-util-wm-devel gtk2-devel deepin-tool-kit-devel qt5-qtx11extras-devel qt5-qtsvg-devel libXtst-devel

Provides:       %{name}
Provides:       %{srcname}

Obsoletes: 		%{srcname} < 4.0.7-1

#%global debug_package %{nil}

%description
%{summary}


%prep
%setup %{version}.tar.gz#%{name} -q -n %{srcname}-%{version}

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
%{_prefix}/lib/*
%{_datarootdir}/*
%{_includedir}/*

%changelog
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.7-1
- Update to version 4.0.7 and renamed to deepin-dock
* Mon Dec 19 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.6-1
- Update to version 4.0.6
* Sun Dec 04 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.5-2
- Rebuild with newer deepin-tool-kit
* Sun Oct 02 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 4.0.5-1
- Initial package build