Name:           deepin-mutter
Version:        3.20.17
Release:        1%{?dist}
Summary:        Base window manager for deepin, fork of gnome mutter
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       dconf
Requires:       deepin-desktop-schemas
Requires:       zenity
BuildRequires:  clutter-devel
BuildRequires:  deepin-cogl-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gnome-common
BuildRequires:  gnome-desktop3-devel
BuildRequires:  gnome-doc-utils
BuildRequires:  gobject-introspection-devel
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  gtk-doc
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libgudev-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  libxkbfile-devel
BuildRequires:  upower-devel
BuildRequires:  xkeyboard-config-devel
BuildRequires:  zenity

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for base window manager for deepin, fork of gnome mutter


%prep
%autosetup %{version}.tar.gz#%{name}

%build
./autogen.sh
%configure \
    --libexecdir=%{_libexecdir}/%{name} \
    --enable-gtk-doc \
    --enable-wayland \
    --enable-native-backend \
    --disable-static \
    --disable-schemas-compile \
    --enable-compile-warnings=minimum
%make_build

%install
%make_install PREFIX="%{_prefix}"

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%post -p /sbin/ldconfig

%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null ||:
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null ||:

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/GConf/gsettings/*.convert
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/gnome-control-center/keybindings/*.xml
%{_libdir}/%{name}/
%{_libdir}/*.so.*
%{_libexecdir}/%{name}/mutter-restart-helper
%{_mandir}/man1/*.1.gz

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*


%changelog
* Wed Apr 19 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 3.20.17-1
- Update to version 3.20.17
* Mon Mar 20 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.20.13-1
- Update to version 3.20.13
* Sat Mar 04 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.20.11-1
- Update to version 3.20.11
* Fri Jan 27 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.20.8-2
- Rewrite of spec file
* Fri Jan 20 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.20.8-1
- Update to version 3.20.8
* Fri Dec 16 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.20.6-1
- Update to version 3.20.6
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.20.5-1
- Initial package build