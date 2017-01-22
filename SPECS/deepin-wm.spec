Name:           deepin-wm
Version:        1.9.2
Release:        %{?dist}
Summary:        Deepin Window Manager
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       deepin-desktop-schemas
Requires:       gnome-desktop
Requires:       libcanberra-gtk3
BuildRequires:  intltool
BuildRequires:  gnome-common
BuildRequires:  gnome-desktop3-devel
BuildRequires:  granite-devel
BuildRequires:  vala
BuildRequires:  vala-tools
BuildRequires:  bamf-devel
BuildRequires:  clutter-gtk-devel
BuildRequires:  deepin-mutter-devel
BuildRequires:  upower-devel
BuildRequires:  libgee-devel
BuildRequires:  libgudev-devel
BuildRequires:  libwnck3-devel
BuildRequires:  libcanberra-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  libxkbfile-devel

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

# fix background path
sed -i 's/default_background.jpg/default.png/' src/Background/BackgroundSource.vala

%build
./autogen.sh
%configure --disable-schemas-compile
%make_build

%install
%make_install PREFIX="%{_prefix}"

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/vala/vapi/%{name}*

%files devel
%{_includedir}/%{name}/%{name}.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/lib*.so

%changelog
* Sat Jan 21 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.9.2-1
- Update to version 1.9.2
* Wed Jan 04 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.2.0-2
- Split the package to main and devel
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.2.0-1
- Update to version 1.2.0
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.2-1
- Initial package build