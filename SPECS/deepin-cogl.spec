Name:           deepin-cogl
Version:        1.22.3
Release:        3%{?dist}
Summary:        An object oriented GL/GLES Abstraction/Utility Layer for Deepin

License:        GPL2
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       glib2 mesa-libGLES mesa-libGL mesa-libwayland-egl libwayland-client mesa-libgbm libwayland-server mesa-libEGL libXrandr libXcomposite libXdamage libXfixes libXext libX11 cairo pango gdk-pixbuf2 gobject-introspection
BuildRequires:  intltool glib2-devel gtk-doc libtool mesa-libGLES-devel mesa-libGL-devel mesa-libwayland-egl-devel libwayland-client-devel mesa-libgbm-devel libwayland-server-devel mesa-libEGL-devel libXrandr-devel libXcomposite-devel libXdamage-devel libXfixes-devel libXext-devel libX11-devel cairo-devel pango-devel gdk-pixbuf2-devel gobject-introspection-devel

Conflicts:      cogl < %{version}
Conflicts:      cogl%{?_isa} < %{version}
Obsoletes:      cogl < %{version}
Obsoletes:      cogl%{?_isa} < %{version}
Provides:       cogl = %{version}-%{release}
Provides:       cogl%{?_isa} = %{version}-%{release}
Provides:       deepin-cogl = %{version}-%{release}

%description
An object oriented GL/GLES Abstraction/Utility Layer for Deepin


%package  devel
Summary:  Header and development files
Requires: %{name} = %{version}

Conflicts:      cogl-devel < %{version}
Obsoletes:      cogl-devel < %{version}
Provides:       cogl-devel = %{version}-%{release}
Provides:       deepin-cogl-devel = %{version}-%{release}

%description  devel
Header files and libraries for building and developing apps with %{name}.


%prep
%autosetup %{version}.tar.gz#%{name}

%build

NOCONFIGURE=1 ./autogen.sh

./configure --prefix=/usr \
    --enable-gles2 \
    --enable-{kms,wayland}-egl-platform \
    --enable-wayland-egl-server

sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool

make -j1

%install
%make_install DESTDIR="%{buildroot}"

#Remove libtool archives
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%ifarch x86_64
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING NEWS README ChangeLog
%{_libdir}/*.so.*
%{_libdir}/girepository-1.0/Cogl*.typelib

%files devel
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/cogl/
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/Cogl*.gir
%{_datadir}/cogl
%{_datadir}/locale

%changelog
* Sat Dec 17 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.22.3-3
- Redone package in a newer format
* Sat Dec 17 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.22.3-2
- Added conflict and obsolete for cogl library
* Fri Dec 16 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.22.3-1
- Initial package build