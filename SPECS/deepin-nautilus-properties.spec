Name:           deepin-nautilus-properties
Version:        3.14.3
Release:        1%{?dist}
Summary:        Provide file property dialog for Deepin desktop environment

License:        GPL
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       nautilus libnotify exempi glib2 gtk3 gnome-desktop3 libxml2 libX11
BuildRequires:  intltool gobject-introspection-devel libnotify-devel libexif-devel exempi-devel glib2-devel gtk3-devel gnome-desktop3-devel libxml2-devel libX11-devel

##   gail-3.0
#  x11


Provides:       %{name}

#%global debug_package %{nil}

%description
Provide file property dialog for Deepin desktop environment


%prep
%autosetup %{version}.tar.gz#%{name}

%build

%define _lib_dir %{nil}
%ifarch x86_64
  %define _lib_dir %{_usr}/lib64
%endif
%ifarch i386 i686
  %define _lib_dir %{_usr}/lib
%endif

libtoolize && aclocal && autoheader && automake --add-missing && autoconf

./configure --prefix=%{_prefix} \
              --libexecdir=%{_lib_dir}/nautilus \
              --disable-nst-extension \
              --disable-update-mimedb \
              --disable-packagekit \
              --disable-introspection \
              --disable-tracker

make

%install
cd src
install -dm755 "%{buildroot}/usr/bin"
libtool --mode=install /usr/bin/install -c deepin-nautilus-properties deepin-open-chooser "%{buildroot}/usr/bin"

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*

%changelog
* Sun Oct 02 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.14.3-1
- Initial package build