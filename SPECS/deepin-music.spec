Name:           deepin-music
Version:        3.0.1
Release:        1%{?dist}
Summary:        Deepin Music Player
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
  
BuildRequires:  deepin-tool-kit-devel
BuildRequires:  desktop-file-utils
BuildRequires:  ffmpeg-devel
BuildRequires:  libicu-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  taglib-devel

Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}


%prep
%autosetup %{version}.tar.gz#%{name}

sed -i 's/-0-2//g' music-player/music-player.pro
sed -i 's/lrelease/lrelease-qt5/g' tool/translate_generation.sh

sed -i '/%1/s|lib|%{_lib}|' music-player/core/pluginmanager.cpp
sed -i '/target.path/s|lib|%{_lib}|' libdmusic/libdmusic.pro \
    plugin/netease-meta-search/netease-meta-search.pro

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build    

%install
%make_install INSTALL_ROOT=%{buildroot}
 
%post
/usr/bin/update-desktop-database -q ||:

%postun
/usr/bin/update-desktop-database -q ||:

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS README.md
%license COPYING
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_libdir}/%{name}/plugins/lib*.so.*
%{_datadir}/%{name}/*
%{_datadir}/dman/%{name}/*
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service

%files devel
%{_qt5_headerdir}/*
%{_qt5_archdatadir}/mkspecs/features/*-qt5.prf
%{_libdir}/lib*.so
%{_libdir}/%{name}/plugins/lib*.so
%{_libdir}/pkgconfig/*-qt5.pc

%changelog
* Tue Jan 24 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.1-1
- Update to version 3.0.1
* Tue Dec 20 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.2-1
- Initial package build