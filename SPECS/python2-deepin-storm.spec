Name:           python2-deepin-storm
Version:        0.3.20140625
Release:        1%{?dist}
Summary:        A download library and powerful download manager

License:        GPL
URL:            https://github.com/martyr-deepin/deepin-storm
Source0:        %{url}/archive/master.zip#%{name}

Requires:       python2
#BuildRequires:  

Provides:       %{name}

%description
A download library and powerful download manager


%prep
cd %{_builddir}
rm -rf deepin-storm-master/
/usr/bin/unzip -qq %{_sourcedir}/master.zip#%{name}
if [ $? -ne 0 ]; then
  exit $?
fi
%define _builddir_pkg %{_builddir}/deepin-storm-master
cd %{_builddir_pkg}
chmod -R a+rX,g-w,o-w .

%build
cd %{_builddir_pkg}
python2 setup.py build

%install
cd %{_builddir_pkg}
python2 setup.py install -O1 --root="%{buildroot}"

%clean
rm -rf %{buildroot}

%files
%{_prefix}/lib/python2.7/site-packages/*


%changelog
* Wed Oct 12 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.3.20140625
- Initial package build