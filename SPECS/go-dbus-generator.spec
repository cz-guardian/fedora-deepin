Name:           go-dbus-generator
Version:        0.6.5
Release:        1%{?dist}
Summary:        Convert dbus interfaces to go-lang or qml wrapper code

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       glibc
BuildRequires:  gcc-go go-lib

Provides:       %{name}

%description
Convert dbus interfaces to go-lang or qml wrapper code


%prep
%autosetup %{version}.tar.gz#%{name}

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
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build