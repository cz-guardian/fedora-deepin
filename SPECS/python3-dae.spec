Name:           python3-dae
Version:        1.0.1
Release:        1%{?dist}
Summary:        Deepin desktop application engine

License:        GPL3
URL:            https://github.com/linuxdeepin/dae
Source0:        %{url}/archive/%{version}.tar.gz#dae
  
Requires:       python3 python3-qt5 python-xlib
BuildRequires:  python3 python3-qt5-devel

BuildArch:      noarch

Provides:       %{name}

#%global debug_package %{nil}

%description
Deepin desktop application engine


%prep
cd %{_builddir}
rm -rf dae-%{version}/
gzip -dc %{_sourcedir}/%{version}.tar.gz#dae | tar -xvvf -
if [ $? -ne 0 ]; then
  exit $?
fi
%define _builddir_pkg %{_builddir}/dae-%{version}
cd %{_builddir_pkg}
chmod -R a+rX,g-w,o-w .

%build
cd %{_builddir_pkg}
python3 setup.py build

%install
cd %{_builddir_pkg}
python3 setup.py install --root="%{buildroot}" --optimize=1

%clean
rm -rf %{buildroot}

%files
%{_prefix}/lib/python3.5/site-packages/*

%changelog
* Wed Dec 21 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.1-1
- Initial package build