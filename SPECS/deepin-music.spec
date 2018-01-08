Name:           deepin-music
Version:        3.1.7.2
Release:        1%{?dist}
Summary:        Deepin Music Player
Summary(zh_CN): 深度音乐播放器
License:        GPLv3
Url:            https://github.com/linuxdeepin/deepin-music
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-linguist
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkwidget) = 2.0
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libcue)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Multimedia)
Provides:       deepin-music-player%{?_isa} = %{version}-%{release}

%description
Deepin Music Player with brilliant and tweakful UI Deepin-UI based,
gstreamer front-end, with features likes search music by pinyin,
quanpin, colorful lyrics supports, and more powerful functions
you will found.

%description -l zh_CN
深度音乐播放器界面基于 Deepin-UI , 后端使用 gstreamer ,
其他特性如音乐搜索, 丰富多彩的歌词支持, 更多功能等待您发现.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q
sed -i 's|lrelease|lrelease-qt5|g' tool/translate_generation.*
sed -i '/%1/s|lib|%{_lib}|' music-player/core/pluginmanager.cpp
sed -i '/target.path/s|lib|%{_lib}|' libdmusic/libdmusic.pro \
    plugin/netease-meta-search/netease-meta-search.pro \
    vendor/src/dbusextended-qt/src/src.pro \
    vendor/src/mpris-qt/src/src.pro

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%post
/sbin/ldconfig
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null ||:
/usr/bin/update-desktop-database -q ||:

%postun
/sbin/ldconfig
if [ $1 -eq 0 ]; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null ||:
    /usr/bin/gtk-update-icon-cache -f -t -q %{_datadir}/icons/hicolor ||:
fi
/usr/bin/update-desktop-database -q ||:

%posttrans
/usr/bin/gtk-update-icon-cache -f -t -q %{_datadir}/icons/hicolor ||:

%files
%doc AUTHORS README.md
%license COPYING
%{_bindir}/%{name}
%{_libdir}/lib*.so.*
%{_libdir}/%{name}/plugins/lib*.so.*
%{_datadir}/%{name}/
%{_datadir}/dman/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/dbus-1/services/*.service

%files devel
%{_includedir}/DBusExtended/
%{_includedir}/MprisQt/
%{_qt5_archdatadir}/mkspecs/features/*-qt5.prf
%{_libdir}/lib*.so
%{_libdir}/%{name}/plugins/lib*.so
%{_libdir}/pkgconfig/*-qt5.pc

%changelog
* Tue Jan 09 2018 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.7.2-1
- Update to version 3.1.7.2
* Sun Apr 23 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.0-1
- Update to version 3.1.0
* Tue Jan 24 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.1-1
- Update to version 3.0.1
* Tue Dec 20 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.2-1
- Initial package build