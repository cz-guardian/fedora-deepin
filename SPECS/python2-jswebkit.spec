%global     srcname jswebkit
%global     python2_sitelib %(%{__python2} -c "import site; print(site.getsitepackages()[0])")

Name:           python2-%{srcname}
Version:        0.0.3
Release:        1%{?dist}
Summary:        simple GTK+ HTML5 rich text editor

License:        GPL3
URL:            http://code.google.com/p/gwrite/
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/gwrite/python-%{srcname}-%{version}.tar.gz#%{srcname}
 
BuildRequires:  python-devel python-setuptools Cython

%description
simple GTK+ HTML5 rich text editor


%prep
%autosetup -n python-%{srcname}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --root="%{buildroot}"

%files
%{python2_sitelib}/*

%changelog
* Mon Dec 26 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.0.3-1
- Initial package build