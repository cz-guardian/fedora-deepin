Name:           deepin-cogl
Version:        1.22.5
Release:        1%{?dist}
Summary:        An object oriented GL/GLES Abstraction/Utility Layer for Deepin
License:        GPL2
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildRequires:  cairo-devel
BuildRequires:  gdk-pixbuf2-devel
BuildRequires:  glib2-devel gtk-doc
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool libtool
BuildRequires:  libwayland-client-devel
BuildRequires:  libwayland-server-devel
BuildRequires:  libX11-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  libXrandr-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLES-devel
BuildRequires:  mesa-libwayland-egl-devel
BuildRequires:  pango-devel

Conflicts:      cogl < %{version}
Conflicts:      cogl%{?_isa} < %{version}
Obsoletes:      cogl < %{version}
Obsoletes:      cogl%{?_isa} < %{version}
Provides:       cogl = %{version}-%{release}
Provides:       cogl%{?_isa} = %{version}-%{release}
Provides:       deepin-cogl = %{version}-%{release}

%description
%{description}


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
NOCONFIGURE=1 ./autogen.sh

%build
%configure --prefix=%{_prefix} \
    --enable-gles2 \
    --enable-{kms,wayland}-egl-platform \
    --enable-wayland-egl-server

sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
make -j1

%install
%make_install

#Remove libtool archives
find %{buildroot} -name '*.la' -exec rm -f {} ';'

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
* Wed Apr 19 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 1.22.5-1
- Update package to version 1.22.5
* Sat Dec 17 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.22.3-4
- Rewrite of spec file
* Sat Dec 17 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.22.3-3
- Redone package in a newer format
* Sat Dec 17 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.22.3-2
- Added conflict and obsolete for cogl library
* Fri Dec 16 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.22.3-1
- Initial package build