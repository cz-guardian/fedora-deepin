%global 		srcname dbus-factory

Name:           deepin-%{srcname}
Version:        3.0.9
Release:        1%{?dist}
Summary:        QML DBus factory for DDE

License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildRequires:  deepin-go-dbus-generator gcc-go

Provides:       %{name}
Provides:       %{srcname}

Obsoletes: 		%{srcname} < 3.0.9-1

%description
%{summary}


%prep
%setup %{version}.tar.gz#%{name} -q -n %{srcname}-%{version}

make

%install
%make_install GOPATH="%{gopath}" DESTDIR="%{buildroot}"

%clean
rm -rf %{buildroot}

%files
%{gopath}/*


%changelog
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.9-1
- Update to version 3.0.9 and renamed to deepin-dbus-factory
* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.8-1
- Update to version 3.0.8
* Thu Sep 29 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.6-2
- Compilation rework
* Wed Sep 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.6-1
- Initial package build