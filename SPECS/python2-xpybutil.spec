%global 		srcname xpybutil
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%global 	commit          c2d438d4ac246b60e25e1f04da2db0eab40acda5
%global 	shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           python2-%{srcname}
Version:        0.0.2.git%{shortcommit}
Release:    	1.git%{shortcommit}%{?dist}
Summary:        An incomplete xcb-util port plus some extras

License:        WTFPL
URL:            https://github.com/BurntSushi/%{srcname}
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz#%{name}
    
Requires:       python2 python-xpyb
BuildRequires:  python2-devel python-xpyb-devel

Provides:       %{name}

%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -n %{srcname}-%{commit}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --root="%{buildroot}"

%clean
rm -rf %{buildroot}

%files
%{_defaultdocdir}/*
%{python2_sitelib}/*

%changelog
* Thu Dec 29 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.0.2-1.gitc2d438d
- Major rewrite of SPEC file 
* Mon Dec 12 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.0.1.20151007-1
- Initial package build
