%global 		srcname go-gir-generator

Name:           deepin-%{srcname}
Version:        1.0.1
Release:        1%{?dist}
Summary:        Generate static golang bindings for GObject
License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildRequires:  gcc-go
BuildRequires:  gobject-introspection-devel
BuildRequires:  libgudev-devel

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}
Provides:       %{srcname}
Provides:       %{srcname}%{?_isa} = %{version}-%{release}
Obsoletes: 		  %{srcname} < %{version}-%{release}
Obsoletes:      %{srcname}%{?_isa} < %{version}-%{release}

%description
%{summary}


%prep
%setup %{version}.tar.gz#%{name} -q -n %{srcname}-%{version}

%build
export GOPATH="%{gopath}"
%make_build

%install
%make_install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/gir-generator
%{gopath}/src/gir/*


%changelog
* Sat Apr 08 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 1.0.1-1
- Update to version 1.0.1
* Thu Jan 26 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.6-4
- Rewrite of spec file
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