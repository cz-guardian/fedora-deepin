# rpmlint gives this error for 37times (for almost every file I think):
#   E: incorrect-fsf-address
#   The Free Software Foundation address in this file seems to be outdated or
#   misspelled.  Ask upstream to update the address, or if this is a license file,
#   possibly the entire file with a new copy available from the FSF.


%{!?python3_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python3-xlib
Version:        0.15
Release:        1%{?dist}
Summary:        Python3 X Library

License:        GPLv2
URL:            https://github.com/LiuLang/python3-xlib
Source0:        https://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%description
python3-xlib is python3 version of python-xlib.

%prep
%setup -q


%build
%{__python3} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python3} setup.py install -O1 --skip-build --root="%{buildroot}"

 
%files
%{python3_sitelib}/*
%exclude %{python3_sitelib}/Xlib/__pycache__

%changelog
* Thu Dec 22 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.15-1
- Initial package build