%global 		srcname go-dbus-generator

Name:           deepin-%{srcname}
Version:        0.6.5
Release:        3%{?dist}
Summary:        Convert dbus interfaces to go-lang or qml wrapper code

License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
Patch0:         go-dbus-generator_0.6.5_fedora-qmake-rename.patch

Requires:       glibc
BuildRequires:  gcc-go deepin-go-lib

Provides:       %{name}
Provides:       %{srcname}

Obsoletes: 		%{srcname} < 0.6.5-3

%global debug_package %{nil}

%description
%{summary}


%prep
%setup %{version}.tar.gz#%{name} -q -n %{srcname}-%{version} 
%patch0 -p1

%build
export GOPATH="$(pwd)/build/:%{gopath}/"
make

%install
install -d -m 755 go-dbus-generator/out/dbus-generator %{buildroot}/%{_bindir}/dbus-generator

%clean
rm -rf %{buildroot}

%files
%{_bindir}/dbus-generator


%changelog
* Wed Jan 04 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.6.5-3
- Renamed package to deepin-go-dbus-generator
* Thu Sep 29 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.6.5-2
- Qmake path fix for Fedora
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.6.5-1
- Initial package build