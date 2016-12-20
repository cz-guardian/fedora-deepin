Name:           python2-deepin-gsettings
Version:        0.1.20131016
Release:        1%{?dist}
Summary:        Deepin gsettings python bindings

License:        GPL
URL:            https://github.com/martyr-deepin/deepin-gsettings
Source0:        %{url}/archive/master.zip#%{name}

Requires:       python2 glib2
BuildRequires:  python2-setuptools python-devel glib2-devel

Provides:       %{name}

%description
Deepin gsettings python bindings


%prep
cd %{_builddir}
rm -rf deepin-gsettings-master/
/usr/bin/unzip -qq %{_sourcedir}/master.zip#%{name}
if [ $? -ne 0 ]; then
  exit $?
fi
%define _builddir_pkg %{_builddir}/deepin-gsettings-master
cd %{_builddir_pkg}
chmod -R a+rX,g-w,o-w .

%build
%define _lib_dir %{nil}
%ifarch x86_64
  %define _lib_dir %{_usr}/lib64
%endif
%ifarch i386 i686
  %define _lib_dir %{_usr}/lib
%endif

cd %{_builddir_pkg}
# fix tests by using another key to test, since the old one was deprecated
sed -e 's|motion-threshold|drag-threshold|' \
  -e 's|idle-dim-battery|idle-dim|g' \
  -i example.py

python2 setup.py build

%install
cd %{_builddir_pkg}
python2 setup.py install --optimize=1 --root="%{buildroot}"

%clean
rm -rf %{buildroot}

%files
%{_lib_dir}/python2.7/site-packages/*


%changelog
* Wed Oct 12 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.20131016
- Initial package build