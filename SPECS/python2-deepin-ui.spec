Name:           python2-deepin-ui
Version:        1.0.5
Release:        1%{?dist}
Summary:        UI toolkit for Linux Deepin

License:        GPL
URL:            https://github.com/martyr-deepin/deepin-ui
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       python2-deepin-utils python2-deepin-gsettings glib2 pygtk2 pycairo python2-scipy python-pillow python-xlib pywebkitgtk libsoup
BuildRequires:  python2-setuptools webkitgtk-devel deepin-gettext-tools

Provides:       %{name}

%description
UI toolkit for Linux Deepin


%prep
cd %{_builddir}
rm -rf deepin-ui-%{version}/
gzip -dc %{_sourcedir}/%{version}.tar.gz#%{name} | tar -xvvf -
if [ $? -ne 0 ]; then
  exit $?
fi
%define _builddir_pkg %{_builddir}/deepin-ui-%{version}
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
# fix python version
find -iname "*.py" | xargs sed -i 's=\(^#! */usr/bin.*\)python *$=\1python2='

python2 setup.py build
deepin-generate-mo dtk/tools/locale_config.ini

%install
cd %{_builddir_pkg}
python2 setup.py install --optimize=1 --root="%{buildroot}"

%clean
rm -rf %{buildroot}

%files
%{_prefix}/lib/python2.7/site-packages/*


%changelog
* Wed Oct 12 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.5-1
- Initial package build