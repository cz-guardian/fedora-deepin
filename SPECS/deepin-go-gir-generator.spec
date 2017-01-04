%global 		srcname go-gir-generator

Name:           deepin-%{srcname}
Version:        0.9.6
Release:        3%{?dist}
Summary:        Generate static golang bindings for GObject

License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       gobject-introspection
BuildRequires:  gcc-go gobject-introspection-devel libgudev-devel

Provides:       %{name}
Provides:       %{srcname}

Obsoletes: 		%{srcname} < 0.9.6-3

%description
%{summary}


%prep
%setup %{version}.tar.gz#%{name} -q -n %{srcname}-%{version}

%build
export GOPATH="$(pwd)/vendor:$(pwd):%{gopath}/src/gir/"
make

%install
%make_install DESTDIR="%{buildroot}"

%clean
rm -rf %{buildroot}

%files
%{_bindir}/gir-generator
%{gopath}/*


%changelog
* Wed Jan 04 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.6-3
- Renamed package to deepin-go-gir-generator
* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.6-2
- Changed lib path 
* Fri Oct 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.6-1
- Compilation rework
* Thu Sep 29 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.5-2
- Compilation rework
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.5-1
- Initial package build