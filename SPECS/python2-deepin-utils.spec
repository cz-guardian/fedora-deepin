%global 		srcname deepin-utils
%global     	python2_sitelib %(%{__python2} -c "import site; print(site.getsitepackages()[0])")

%global 		commit          8aaf2a6f002eeba5506c11c64b25d1404de78744
%global 		shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           python2-%{srcname}
Version:        0.2.git%{shortcommit}
Release:        1%{?dist}
Summary:        Basic utils for all project in Linux Deepin

License:        GPL3
URL:            https://github.com/martyr-deepin/%{srcname}
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz#%{name}

Requires:       pygtk2 pycairo freetype webkitgtk python-xlib pywebkitgtk glib2 pygobject2
BuildRequires:  python2-setuptools glib2-devel pygtk2 pygobject2-devel pycairo-devel webkitgtk-devel

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
* Thu Dec 29 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.2.git8aaf2a6-1
- Major rewrite of SPEC file
* Wed Oct 12 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.20140509-1
- Initial package build