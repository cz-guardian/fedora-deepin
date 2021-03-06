#
# Now obsolete
#
Name:           deepin-tool-kit
Version:        1.0.0
Release:        1%{?dist}
Summary:        Base development tool of all C++/Qt Developer work on Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-tool-kit
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  dtksettings-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  libXrender-devel
BuildRequires:  startup-notification-devel
BuildRequires:  systemd-devel
BuildRequires:  xcb-util-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}

%description
Base development tool of all C++/Qt Developer work on Deepin.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q
sed -i 's|lrelease|lrelease-qt5|g' tool/translate_generation.sh
sed -i -E '/test|examples/d' dtk.pro

%build
%qmake_qt5 PREFIX=%{_prefix} LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT="%{buildroot}"

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md Specification.md
%license LICENSE
%{_libdir}/lib*.so.*
%{_datadir}/dtkwidget1/translations/*.qm

%files devel
%{_includedir}/libdtk-*/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
* Fri Jan 05 2018 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 1.0.0-1
- Update to version 1.0.0
* Sun Apr 23 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 0.2.9-2
- Bump version because of dtksettings update
* Thu Apr 20 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 0.2.9-1
- Updated package to 0.2.9
* Sun Apr 09 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.2.8-1
- Updated package to 0.2.8
* Sat Mar 18 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.2.7-1
- Updated package to 0.2.7
* Thu Mar 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.2.5-1
- Updated package to 0.2.5
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