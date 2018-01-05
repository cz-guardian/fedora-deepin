%global _terminals gnome-terminal mate-terminal xfce4-terminal lxterminal qterminal qterminal-qt5 terminology yakuake fourterm roxterm lilyterm termit xterm mrxvt

Name:           deepin-terminal
Version:        2.9.2
Release:        1%{?dist}
Summary:        Default terminal emulation application for Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-terminal
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}_unbundle_vte.patch

BuildRequires:  cmake
BuildRequires:  gettext
BuildRequires:  vala-devel
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(vte-2.91)
# right-click menu style
Requires:       deepin-menu
# run command by create_from_commandline
Requires:       deepin-shortcut-viewer
Requires:       expect
Requires:       xdg-utils
Recommends:     deepin-manual
Recommends:     zssh
Requires:       %{name}-data = %{version}-%{release}

%description
Default terminal emulation application for Deepin.

%package data
Summary:        Data files of Deepin Terminal
BuildArch:      noarch
Requires:       hicolor-icon-theme

%description data
The %{name}-data package provides shared data for Deepin Terminal.

%prep
%setup -q
%patch0 -p1 -b .unbundle_vte
sed -i 's|return __FILE__;|return "%{_datadir}/%{name}/project_path.c";|' project_path.c
sed -i 's|/usr/lib/%{name}/zssh|%{_bindir}/zssh|' ssh_login.sh
sed -i '/ssh_login/s|lib|libexec|' lib/utils.vala
sed -i 's|2.7|2.9|' lib/constant.vala

# remove es_419 locale
rm -rf po/es_419/
sed -i '/es_419/d' deepin-terminal.desktop

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%make_build

%install
%make_install

%find_lang %{name}

%preun
if [ $1 -eq 0 ]; then
  %{_sbindir}/alternatives --remove x-terminal-emulator %{_bindir}/%{name}
fi

%post
if [ $1 -ge 1 ]; then
  %{_sbindir}/alternatives --install %{_bindir}/x-terminal-emulator \
    x-terminal-emulator %{_bindir}/%{name} 20
fi

%triggerin -- konsole5 %_terminals
if [ $1 -ge 1 ]; then
  PRI=20
  for i in konsole %{_terminals}; do
    PRI=$((PRI-1))
    test -x %{_bindir}/$i && \
    %{_sbindir}/alternatives --install %{_bindir}/x-terminal-emulator \
      x-terminal-emulator %{_bindir}/$i $PRI
  done
fi

%triggerpostun -- konsole5 %_terminals
if [ $2 -eq 0 ]; then
  for i in konsole %{_terminals}; do
    test -x %{_bindir}/$i || \
    %{_sbindir}/alternatives --remove x-terminal-emulator %{_bindir}/$i &>/dev/null ||:
  done
fi

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_libexecdir}/%{name}/ssh_login.sh

%files data -f %{name}.lang
%{_datadir}/%{name}/
%{_datadir}/dman/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}*
%{_datadir}/applications/%{name}.desktop

%changelog
* Fri Jan 05 2018 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek - 2.9.2-1
- Updated to version 2.9.2
* Mon Apr 24 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 2.3.1-1
- Updated to version 2.3.1
* Mon Mar 20 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.2.6-1
- Updated to version 2.2.6
* Thu Mar 09 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.2.2-1
- Updated to version 2.2.2
* Mon Jan 23 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.1.9-1
- Updated to version 2.1.9
* Thu Jan 19 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.1.7-1
- Updated to version 2.1.7
* Thu Jan 12 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.1.6-1
- Updated to version 2.1.6
* Thu Dec 15 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.1.5-2
- Fixed icon path
* Mon Dec 12 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.1.5-1
- Initial package build