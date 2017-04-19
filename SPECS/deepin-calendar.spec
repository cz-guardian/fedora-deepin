%global 		srcname dde-calendar

Name:           deepin-calendar
Version:        1.0.7
Release:        1%{?dist}
Summary:        Calendar for Deepin Desktop Environment
License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  deepin-tool-kit-devel

Provides:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{srcname}%{?_isa} < %{version}-%{release}

%description
%{description}


%prep
%autosetup %{version}.tar.gz#%{name} -n %{srcname}-%{version}
sed -i 's/lrelease/lrelease-qt5/g' translate_generation.sh

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datadir}/%{srcname}/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg


%changelog
* Wed Apr 19 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.7-1
- Update to version 1.0.7
* Tue Jan 24 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.3-2
- Rename to deepin-calendar
* Mon Dec 19 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.3-1
- Update to version 1.0.3
* Sun Dec 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.2-2
- Rebuild with newer deepin-tool-kit
* Sun Oct 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.2-1
- Initial package build