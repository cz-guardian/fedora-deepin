Name:           deepin-metacity
Version:        3.22.8
Release:        1%{?dist}
Summary:        2D window manager for Deepin
License:        GPL
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       dconf
Requires:       deepin-desktop-schemas
BuildRequires:  autoconf-archive
BuildRequires:  bamf-devel
BuildRequires:  glib2-devel
BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  json-glib-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libgtop2-devel
BuildRequires:  libtool
BuildRequires:  startup-notification-devel
BuildRequires:  yelp-tools
BuildRequires:  zenity

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}


%prep
%autosetup %{version}.tar.gz#%{name}

%build
./autogen.sh
%configure \
    --disable-static \
    --disable-schemas-compile
%make_build

%install
%make_install PREFIX=%{_prefix}
#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%clean
rm -rf %{buildroot}

%files
%doc README
%license COPYING
%{_bindir}/*
%{_libdir}/*.so.*
%{_datadir}/GConf/gsettings/*.convert
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/com.deepin.*.xml
%{_datadir}/gnome-control-center/keybindings/50-%{name}-*.xml
%{_datadir}/gnome/wm-properties/*.desktop
%{_datadir}/help/
%{_datadir}/locale/
%{_datadir}/themes/
%{_mandir}/man1/*

%files devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib%{name}*.so

%changelog
* Wed Apr 19 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 3.22.8-1
- Update to 3.22.8
* Mon Mar 20 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.22.5-1
- Update to 3.22.5
* Sun Mar 05 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.22.3-1
- Update to 3.22.3
* Thu Jan 26 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.22.0-2
- Rewrite of spec file
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.22.0-1
- Update to version 3.22.0
* Thu Jan 05 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.20.6-2
- Split the package to main and devel
* Fri Dec 16 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.20.6-1
- Update to version 3.20.6
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.20.5-1
- Initial package build