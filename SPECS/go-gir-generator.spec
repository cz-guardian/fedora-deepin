Name:           go-gir-generator
Version:        0.9.6
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
export GOPATH="$(pwd)/vendor:$(pwd):/usr/share/gocode/src/gir/"
make

%install
%make_install DESTDIR="%{buildroot}" install
mv %{buildroot}/usr/share/gocode/src %{buildroot}/usr/
rmdir %{buildroot}/usr/share/gocode/
rmdir %{buildroot}/usr/share

%clean
rm -rf %{buildroot}

%files
%{_bindir}/gir-generator
%{_prefix}/src/*


%changelog
* Fri Oct 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.6-1
- Compilation rework
* Thu Sep 29 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.5-2
- Compilation rework
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.5-1
- Initial package build