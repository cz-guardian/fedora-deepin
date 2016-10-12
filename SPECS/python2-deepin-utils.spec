Name:           python2-deepin-utils
Version:        0.1.20140509
Release:        1%{?dist}
Summary:        Basic utils for all project in Linux Deepin

License:        GPL3
URL:            https://github.com/martyr-deepin/deepin-utils
Source0:        %{url}/archive/master.zip#%{name}

Requires:       pygtk2 pycairo freetype webkitgtk python-xlib pywebkitgtk
BuildRequires:  python2-setuptools

Provides:       %{name}

%description
Basic utils for all project in Linux Deepin


%prep
cd %{_builddir}
rm -rf deepin-utils-master/
/usr/bin/unzip -qq %{_sourcedir}/master.zip#%{name}
if [ $? -ne 0 ]; then
  exit $?
fi
%define _builddir_pkg %{_builddir}/deepin-utils-master
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
python2 setup.py build

%install
cd %{_builddir_pkg}
python2 setup.py install --optimize=1 --root="%{buildroot}"

%clean
rm -rf %{buildroot}

%files
%{_lib_dir}/python2.7/site-packages/*


%changelog
* Wed Oct 12 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.20140509-1
- Initial package build