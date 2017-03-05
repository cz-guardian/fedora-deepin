Name:           deepin-tool-kit
Version:        0.2.4
Release:        1%{?dist}
Summary:        Base development tool of all C++/Qt Developer work on Deepin
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildRequires:  dtksettings-devel
BuildRequires:  libXrender-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  startup-notification-devel
BuildRequires:  xcb-util-devel

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}


%prep
%autosetup %{version}.tar.gz#%{name}
sed -i 's/lrelease/lrelease-qt5/g' tool/translate_generation.sh
sed -i -E '/test|examples/d' dtk.pro

%build
%qmake_qt5 PREFIX=%{_prefix} LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT="%{buildroot}"

%clean
rm -rf %{buildroot}

%files
%doc README.md Specification.md
%license LICENSE
%{_libdir}/lib*.so.*
%{_datadir}/dtkwidget/translations/*.qm

%files devel
%{_includedir}/libdtk-*/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
* Sun Mar 05 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.2.4-1
- Updated package to 0.2.4
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.2.1-2
- Rewrite of spec file
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.2.1-1
- Updated package to 0.2.1
* Thu Jan 05 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.2.0-2
- Split the package to main and devel
* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.2.0-1
- Updated package to 1.7
* Sat Dec 03 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.7-1
- Updated package to 1.7
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.6-1
- Initial package build