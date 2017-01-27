%global 		srcname dae
%{!?python3_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python3-%{srcname}
Version:        1.0.2
Release:        3%{?dist}
Summary:        Deepin desktop application engine

License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{srcname}
  
Requires:       python3 
Requires:       python3-qt5 
Requires:       python3-qt5-webkit 
Requires:       python3-xlib
BuildRequires:  python3-devel 
BuildRequires:  python3-qt5-devel

BuildArch:      noarch

Provides:       %{name}

%description
Deepin desktop application engine


%prep
%autosetup -n %{srcname}-%{version}

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --root="%{buildroot}" --optimize=1

%clean
rm -rf %{buildroot}

%files
%{python3_sitelib}/*

%changelog
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.2-1
- Update to version 1.0.2
* Thu Dec 29 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.1-3
- Major rewrite of SPEC file
* Thu Dec 22 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.1-2
- Fixed dependency for xlib
* Wed Dec 21 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.1-1
- Initial package build