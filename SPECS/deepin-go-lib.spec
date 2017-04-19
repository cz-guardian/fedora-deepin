%global 		srcname go-lib
%global 		debug_package %{nil}

Name:           deepin-%{srcname}
Version:        1.0.3
Release:        1%{?dist}
Summary:        Deepin GoLang Library
License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildArch:      noarch

BuildRequires:  golang

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

%install
install -d %{buildroot}%{gopath}/src/pkg.deepin.io/lib/
cp -r * %{buildroot}%{gopath}/src/pkg.deepin.io/lib/
rm -rf %{buildroot}%{gopath}/src/pkg.deepin.io/lib/debian

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{gopath}/src/pkg.deepin.io/lib/


%changelog
* Wed Apr 19 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 1.0.3-1
- Update to version 1.0.3
* Sat Apr 08 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 1.0.1-1
- Update to version 1.0.1
* Fri Mar 17 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.5.6-1
- Update to version 0.5.6
* Sun Mar 05 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.5.5-1
- Update to version 0.5.5
* Thu Jan 26 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.5.3-2
- Rewrite of spec file
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.5.3-1
- Update to version 0.5.3
* Wed Jan 04 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.5.2-3
- Package renamed to deepin-go-lib
* Fri Dec 16 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.5.2-2
- Fixed lib path
* Fri Dec 16 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.5.2-1
- Update to version 0.5.2
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.5.1-1
- Initial package build