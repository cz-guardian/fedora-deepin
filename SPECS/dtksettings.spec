%global commit 34d321e517524d7eb3110dee2c9d3049771ede05
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           dtksettings
Version:        0.1.7
Release:        1.git%{shortcommit}%{?dist}
Summary:        Dtk module to generate user configuration and UI dialog from json
License:        GPLv3
URL:            https://github.com/linuxdeepin/dtksettings
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildRequires:  qt5-qtbase-devel

%description
This package provides a Dtk module which can generate user configuration and UI
dialog from json.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{name}-%{commit}

%build
%qmake_qt5 PREFIX=%{_prefix} LIB_INSTALL_DIR=%{_libdir}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE
%{_bindir}/dtk-settings-tool
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/libdtk-*/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
* Fri Jan 05 2018 Jaroslav <cz.guardian@gmail.com> Stepanek - 0.1.7-1
- Update to 0.1.7
* Sat Apr 22 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.6-1
- Update to 0.1.6
* Sat Mar 18 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.5-1
- Update to 0.1.5
* Sun Mar 05 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.3-1
- Initial package build