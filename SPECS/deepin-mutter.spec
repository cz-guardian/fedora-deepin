Name:           deepin-mutter
Version:        3.20.5
Release:        1%{?dist}
Summary:        Base window manager for deepin, fork of gnome mutter

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       clutter dconf gobject-introspection deepin-desktop-schemas libcanberra startup-notification zenity libSM gnome-desktop upower libxkbcommon-x11 libgudev gtk3 gsettings-desktop-schemas clutter gnome-desktop3 libxkbfile xkeyboard-config libxkbcommon-x11 libgudev
BuildRequires:  gnome-common gnome-doc-utils gobject-introspection-devel gtk-doc intltool gtk3-devel gsettings-desktop-schemas-devel clutter-devel upower-devel gnome-desktop3-devel libxkbfile-devel xkeyboard-config-devel libxkbcommon-x11-devel libgudev-devel zenity

Provides:       %{name}

%description
Base window manager for deepin, fork of gnome mutter


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

./autogen.sh \
    --prefix=/usr \
    --sysconfdir=/etc \
    --libexecdir=/usr/lib/deepin-mutter \
    --localstatedir=/var \
    --enable-gtk-doc \
    --enable-wayland \
    --enable-native-backend \
    --disable-static \
    --disable-schemas-compile \
    --enable-compile-warnings=minimum
make

%install
%make_install PREFIX="%{_prefix}"
%ifarch x86_64
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%clean
rm -rf %{buildroot}

%files
%{_bindir}/deepin-mutter
%{_usr}/include/*
%{_lib_dir}/*
%{_datarootdir}/locale/*
%{_datarootdir}/*


%changelog
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build