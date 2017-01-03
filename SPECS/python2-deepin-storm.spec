%global 		srcname deepin-storm
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

%global 		commit          e6fe6aab1cadca5ed2ed6f086fb2db9699e00416
%global 		shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           python2-%{srcname}
Version:        0.4.git%{shortcommit}
Release:        1%{?dist}
Summary:        A download library and powerful download manager

License:        GPL
URL:            https://github.com/martyr-deepin/%{srcname}
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz#%{name}

BuildArch:      noarch

Requires:       python2
BuildRequires:  python2-devel

Provides:       %{name}

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
%{python2_sitelib}/*


%changelog
* Tue Jan 03 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.4.gite6fe6aa-1
- Initial package build
* Wed Oct 12 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.3.20140625
- Initial package build