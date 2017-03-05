%global 		srcname dbus-factory
%global 		debug_package %{nil}

Name:           deepin-%{srcname}
Version:        3.1.0
Release:        1%{?dist}
Summary:        QML DBus factory for DDE
License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildRequires:  deepin-go-dbus-generator
BuildRequires:  deepin-go-lib
BuildRequires:  gcc-go

Provides:       %{name}
Provides:       %{srcname}
Provides:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{srcname}%{?_isa} = %{version}-%{release}
Obsoletes: 		%{srcname} < %{version}-%{release}
Provides:       %{srcname}%{?_isa} < %{version}-%{release}

%description
%{summary}


%prep
%setup %{version}.tar.gz#%{name} -q -n %{srcname}-%{version}

%build
%make_build

%install
%make_install GOPATH=%{gopath}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md
%{gopath}/src/dbus/*


%changelog
* Sun Mar 05 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.0-1
- Update to version 3.1.0
* Wed Jan 25 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.9-2
- Spec file rewrite
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.9-1
- Update to version 3.0.9 and renamed to deepin-dbus-factory
* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.8-1
- Update to version 3.0.8
* Thu Sep 29 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.6-2
- Compilation rework
* Wed Sep 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.6-1
- Initial package build