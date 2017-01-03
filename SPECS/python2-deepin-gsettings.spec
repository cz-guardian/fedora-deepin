%global 		srcname deepin-gsettings
%global     	python2_sitelib %(%{__python2} -c "import site; print(site.getsitepackages()[0])")

%global 		commit          a64de3ac195fe8d5878a07f2e862a058d49ce16d
%global 		shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           python2-%{srcname}
Version:        0.2.git%{shortcommit}
Release:        1%{?dist}
Summary:        Deepin gsettings python bindings

License:        GPL
URL:            https://github.com/martyr-deepin/%{srcname}
Source0:        %{url}/archive/%{commit}/%{srcname}-%{shortcommit}.tar.gz#%{name}

Requires:       python2 glib2
BuildRequires:  python2-setuptools python-devel glib2-devel

Provides:       %{name}

%description
%{summary}


%prep
%setup -q -n %{srcname}-%{commit}

# fix tests by using another key to test, since the old one was deprecated
sed -e 's|motion-threshold|drag-threshold|' \
  -e 's|idle-dim-battery|idle-dim|g' \
  -i example.py

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --root="%{buildroot}"

%clean
rm -rf %{buildroot}

%files
%{python2_sitelib}/*


%changelog
* Tue Jan 03 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.20131016
- Major rewrite of SPEC file
* Wed Oct 12 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.20131016
- Initial package build