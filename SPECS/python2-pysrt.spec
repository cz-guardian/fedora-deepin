%global 		srcname pysrt
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python2-%{srcname}
Version:        1.1.1
Release:        1%{?dist}
Summary:        pysrt is a Python library used to edit or create SubRip files.

License:        GPL3
URL:            https://github.com/byroot/pysrt
Source0:        https://github.com/byroot/%{srcname}/archive/v%{version}.tar.gz#%{srcname}
 
BuildArch:      noarch
BuildRequires:  python-devel python-setuptools

%description
pysrt is a Python library used to edit or create SubRip files.


%prep
%autosetup -n %{srcname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --root="%{buildroot}"

%files
%{_bindir}/*
%{python2_sitelib}/*

%changelog
* Thu Dec 22 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.1-1
- Initial package build