%global repo go-dbus-generator

Name:           deepin-dbus-generator
Version:        0.6.6
Release:        1%{?dist}
Summary:        Convert dbus interfaces to go-lang or qml wrapper code
License:        GPLv3+
URL:            https://github.com/linuxdeepin/go-dbus-generator
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 aarch64 %{arm}}
BuildRequires:  gcc-go
BuildRequires:  golang(gopkg.in/check.v1)
BuildRequires:  golang(pkg.deepin.io/lib)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Qml)

%description
Static dbus binding generator for dlib.

%prep
%setup -q -n %{repo}-%{version}
# qmake path
sed -i 's|qmake|qmake-qt5|' build_test.go template_qml.go

%build
export GOPATH="%{gopath}"
%make_build

%install
%make_install GOPATH="%{gopath}"

%files
%doc README.md
%license LICENSE
%{_bindir}/dbus-generator

%changelog
* Tue Jan 02 2018 Jaroslav <cz.guardian@gmail.com> Stepanek 0.6.6-1
- Package updated to version 0.6.6
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