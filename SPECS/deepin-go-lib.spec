%global 		srcname go-lib

Name:           deepin-%{srcname}
Version:        0.5.2
Release:        3%{?dist}
Summary:        Deepin GoLang Library

License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Provides:       %{name}
Provides:       %{srcname}

Obsoletes: 		%{srcname} < 0.5.2-3

%global debug_package %{nil}

%description
%{summary}


%prep
%setup %{version}.tar.gz#%{name} -q -n %{srcname}-%{version}

%build

%install
install -d -m 755 %{buildroot}%{gopath}/src/pkg.deepin.io/lib
cp -r %{_builddir}/%{srcname}-%{version}/* %{buildroot}%{gopath}/src/pkg.deepin.io/lib/

%clean
rm -rf %{buildroot}

%files
%{gopath}/*


%changelog
* Wed Jan 04 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.5.2-3
- Package renamed to deepin-go-lib
* Fri Dec 16 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.5.2-2
- Fixed lib path
* Fri Dec 16 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.5.2-1
- Update to version 0.5.2
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.5.1-1
- Initial package build