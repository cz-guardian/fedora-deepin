Name:           deepin-mutter
Version:        3.20.6
Release:        1%{?dist}
Summary:        Base window manager for deepin, fork of gnome mutter

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       clutter dconf gobject-introspection deepin-desktop-schemas libcanberra startup-notification zenity libSM gnome-desktop upower libxkbcommon-x11 libgudev gtk3 gsettings-desktop-schemas clutter gnome-desktop3 libxkbfile xkeyboard-config libxkbcommon-x11 libgudev deepin-cogl
BuildRequires:  gnome-common gnome-doc-utils gobject-introspection-devel gtk-doc intltool gtk3-devel gsettings-desktop-schemas-devel clutter-devel upower-devel gnome-desktop3-devel libxkbfile-devel xkeyboard-config-devel libxkbcommon-x11-devel libgudev-devel zenity deepin-cogl-devel

Provides:       %{name}

%description
Base window manager for deepin, fork of gnome mutter


%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for base window manager for deepin, fork of gnome mutter


%prep
%autosetup %{version}.tar.gz#%{name}

%build

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

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang %{name}

%ifarch x86_64
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

# Mutter contains a .desktop file so we just need to validate it
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%post -p /sbin/ldconfig

%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
  glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%clean
rm -rf %{buildroot}


%files -f %{name}.lang
%doc COPYING NEWS
%doc %{_mandir}/man1/deepin-mutter.1.gz
%{_bindir}/deepin-mutter
%{_datadir}/applications/*.desktop
%{_libdir}/lib*.so.*
%{_libdir}/deepin-mutter/
%{_datadir}/GConf/gsettings/deepin-mutter-schemas.convert
%{_datadir}/glib-2.0/schemas/com.deepin.wrap.gnome.mutter.gschema.xml
%{_datadir}/glib-2.0/schemas/com.deepin.wrap.gnome.mutter.wayland.gschema.xml
%{_datadir}/gnome-control-center/keybindings/50-deepin-mutter-*.xml


%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*


%changelog
* Fri Dec 16 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.20.6-1
- Update to version 3.20.6
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.20.5-1
- Initial package build