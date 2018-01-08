Name:           deepin-movie
Version:        3.2.0.2
Release:        1%{?dist}
Summary:        Deepin movie based on mpv
Summary(zh_CN): 深度影音
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-movie-reborn
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  pkgconfig(dtkcore)
BuildRequires:  pkgconfig(dtkwidget) = 2.0
BuildRequires:  pkgconfig(dvdnav)
BuildRequires:  pkgconfig(libffmpegthumbnailer)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavresample)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(mpv)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xcb-shape)

%description
Deepin movie for deepin desktop environment.

%description -l zh_CN
深度影音播放器, 后端基于MPV, 支持解码大多数视频格式.

%package devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}.

%prep
%setup -q -n %{name}-reborn-%{version}
sed -i '/dtk2/s|lib|libexec|' src/CMakeLists.txt

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%make_build

%install
%make_install

%find_lang %{name} --with-qt

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null ||:
/usr/bin/update-desktop-database -q ||:

%postun
if [ $1 -eq 0 ]; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null ||:
    /usr/bin/gtk-update-icon-cache -f -t -q %{_datadir}/icons/hicolor ||:
fi
/usr/bin/update-desktop-database -q ||:

%posttrans
/usr/bin/gtk-update-icon-cache -f -t -q %{_datadir}/icons/hicolor ||:

%files -f %{name}.lang
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libdir}/libdmr.so.*
%{_datadir}/dman/%{name}/
%{_datadir}/%{name}/translations/%{name}*.qm
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

%files devel
%{_includedir}/libdmr/*.h
%{_libdir}/pkgconfig/libdmr.pc
%{_libdir}/libdmr.so

%changelog
* Tue Jan 09 2018 Jaroslav <cz.guardian@gmail.com> Stepanek - 3.2.0.2-1
- Update to 3.2.0
* Sun Apr 23 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.2.13-1
- Update to 2.2.13
* Tue Jan 24 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.2.11-2
- Fix broken python-bottle dependency
* Tue Jan 24 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.2.11-1
- Update to version 2.2.11
* Wed Dec 21 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.2.10-1
- Initial package build