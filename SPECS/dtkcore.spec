Name:           dtkcore
Version:        2.0.5.3
Release:        1%{?dist}
Summary:        Deepin tool kit core modules
License:        GPLv3
URL:            https://github.com/linuxdeepin/dtkcore
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(gsettings-qt)

%description
Deepin tool kit core modules.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q
sed -i 's|tests|tool|' dtkcore.pro
sed -i 's|/lib|/libexec|' tool/settings/settings.pro

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
%{_libdir}/lib*.so.*
%{_libexecdir}/dtk2/dtk-settings-tool

%files devel
%doc doc/Specification.md
%{_includedir}/libdtk-*/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
* Fri Jan 05 2018 Jaroslav <cz.guardian@gmail.com> Stepanek - 2.0.5.3-1
- Initial build
