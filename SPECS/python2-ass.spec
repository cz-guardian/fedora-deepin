%global 		srcname ass
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python2-%{srcname}
Version:        0.4.2
Release:        1%{?dist}
Summary:        Advanced SubStation Alpha subtitle files

License:        MIT
URL:            https://github.com/rfw/python-ass
Source0:        https://pypi.python.org/packages/source/a/%{srcname}/%{srcname}-%{version}.tar.gz
 
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools

%description
Advanced SubStation Alpha subtitle files


%prep
%autosetup -n %{srcname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --root="%{buildroot}"

%files
%{python2_sitelib}/*

%changelog
* Thu Dec 22 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.4.2-1
- Initial package build