Name:           go-dbus-generator
Version:        0.6.5
Release:        2%{?dist}
Summary:        Convert dbus interfaces to go-lang or qml wrapper code

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
Patch0:         go-dbus-generator_0.6.5_fedora-qmake-rename.patch

Requires:       glibc
BuildRequires:  gcc-go go-lib

Provides:       %{name}

%description
Convert dbus interfaces to go-lang or qml wrapper code


%prep
%autosetup -p1 %{version}.tar.gz#%{name}

%build
export GOPATH="$(pwd)/build"
make

%install
%make_install PREFIX="%{_prefix}"

%clean
rm -rf %{buildroot}

%files
%{_bindir}/dbus-generator


%changelog
* Thu Sep 29 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.6.5-2
- Qmake path fix for Fedora
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.6.5-1
- Initial package build