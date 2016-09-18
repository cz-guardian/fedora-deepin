Name:           go-gir-generator
Version:        0.9.5
Release:        1%{?dist}
Summary:        Generate static golang bindings for GObject

License:        GPL3
URL:            https://github.com/linuxdeepin/go-gir-generator
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       gobject-introspection
BuildRequires:  gcc-go

Provides:       %{name}

%description
Generate static golang bindings for GObject


%prep
%autosetup %{version}.tar.gz#%{name}

%build
export GOPATH="$(pwd)/vendor:$(pwd)"
cd ./src/gir-generator/
go build -gccgoflags "$(pkg-config --libs gobject-introspection-1.0) $CFLAGS $LDFLAGS" -o gir-generator

%install
install -D -m 755 src/gir-generator/gir-generator %{buildroot}/usr/bin/gir-generator

%clean
rm -rf %{buildroot}

%files
%{_bindir}/gir-generator


%changelog
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build