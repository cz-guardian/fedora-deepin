Name:           python2-xpybutil
Version:        0.0.1.20151007
Release:        1%{?dist}
Summary:        An incomplete xcb-util port plus some extras

License:        WTFPL
URL:            https://github.com/BurntSushi/xpybutil
Source0:        %{url}/archive/master.zip#%{name}
    
Requires:       python2 python-xpyb
BuildRequires:  python2 python-xpyb-devel

Provides:       %{name}

%global debug_package %{nil}

%description
An incomplete xcb-util port plus some extras

%prep
cd %{_builddir}
rm -rf xpybutil-master/
/usr/bin/unzip -qq %{_sourcedir}/master.zip#%{name}
if [ $? -ne 0 ]; then
  exit $?
fi
%define _builddir_pkg %{_builddir}/xpybutil-master
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
python2 setup.py install -O1 --root="%{buildroot}"

%ifarch x86_64
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%clean
rm -rf %{buildroot}

%files
%{_datarootdir}/*
%{_lib_dir}/*

%changelog
* Mon Dec 12 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.0.1.20151007-1
- Initial package build
