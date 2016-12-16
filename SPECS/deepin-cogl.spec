Name:           deepin-cogl
Version:        1.22.3
Release:        1%{?dist}
Summary:        An object oriented GL/GLES Abstraction/Utility Layer for Deepin

License:        GPL2
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       glib2 mesa-libGLES mesa-libGL mesa-libwayland-egl libwayland-client mesa-libgbm libwayland-server mesa-libEGL libXrandr libXcomposite libXdamage libXfixes libXext libX11 cairo pango gdk-pixbuf2
BuildRequires:  intltool glib2-devel gtk-doc libtool mesa-libGLES-devel mesa-libGL-devel mesa-libwayland-egl-devel libwayland-client-devel mesa-libgbm-devel libwayland-server-devel mesa-libEGL-devel libXrandr-devel libXcomposite-devel libXdamage-devel libXfixes-devel libXext-devel libX11-devel cairo-devel pango-devel gdk-pixbuf2-devel

Provides:       %{name}

%description
An object oriented GL/GLES Abstraction/Utility Layer for Deepin


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

NOCONFIGURE=1 ./autogen.sh

./configure --prefix=/usr \
    --enable-gles2 \
    --enable-{kms,wayland}-egl-platform \
    --enable-wayland-egl-server

sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool

make -j1

%install
%make_install DESTDIR="%{buildroot}"
%ifarch x86_64
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%clean
rm -rf %{buildroot}

%files
%{_usr}/include/*
%{_lib_dir}/*
%{_datarootdir}/*


%changelog
* Fri Dec 16 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.22.3-1
- Initial package build