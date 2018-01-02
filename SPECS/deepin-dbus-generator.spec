%global 		srcname go-dbus-generator
%global 		debug_package %{nil}

Name:           deepin-%{srcname}
Version:        0.6.5
Release:        5%{?dist}
Summary:        Convert dbus interfaces to go-lang or qml wrapper code
License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildRequires:  deepin-go-lib
BuildRequires:  gcc-go
BuildRequires:  golang-gopkg-check-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{srcname}
Provides:       %{srcname}%{?_isa} = %{version}-%{release}
Obsoletes: 		%{srcname} < %{version}-%{release}

%description
%{summary}


%prep
%setup %{version}.tar.gz#%{name} -q -n %{srcname}-%{version} 
# qmake path
sed -i 's/qmake/qmake-qt5/' build_test.go template_qml.go

%build
export GOPATH="%{gopath}"
%make_build

%install
%make_install GOPATH="%{gopath}"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/dbus-generator


%changelog
* Thu Jan 26 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.6.5-5
- Rewrite of spec file
* Wed Jan 04 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.6.5-4
- Fixed missing binary file
* Wed Jan 04 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.6.5-3
- Renamed package to deepin-go-dbus-generator
* Thu Sep 29 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.6.5-2
- Qmake path fix for Fedora
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.6.5-1
- Initial package build