Name:           gsettings-qt
Version:        0.1.20160329
Release:        1%{?dist}
Summary:        Qml bindings for GSettings

%define         _revision 82

License:        GPL
URL:            https://launchpad.net/%{name}
Source0:        http://bazaar.launchpad.net/~system-settings-touch/%{name}/trunk/tarball/%{_revision}?start_revid=%{_revision}

Requires:       qt5-qtdeclarative
BuildRequires:  qt5-qtdeclarative-devel glib2-devel

Provides:       %{name}


%description
Qml bindings for GSettings


%prep
cd %{_builddir}
rm -rf ~system-settings-touch
gzip -dc %{_sourcedir}/%{_revision} | tar -xvvf -
if [ $? -ne 0 ]; then
  exit $?
fi
%define _builddir_pkg %{_builddir}/~system-settings-touch/%{name}/trunk
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
qmake-qt5 PREFIX=%{_prefix}
make

%install
cd %{_builddir_pkg}
DISPLAY=:0 make INSTALL_ROOT="%{buildroot}" install

%clean
rm -rf %{buildroot}

%files
%{_lib_dir}/*
%{_includedir}/*

%changelog
* Sun Oct 02 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.20160329-1
- Initial package build