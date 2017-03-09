Name:           deepin-terminal
Version:        2.2.2
Release:        1%{?dist}
Summary:        Default terminal emulation application for Deepin
License:        GPL3
URL:            https://github.com/manateelazycat/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       deepin-manual
Requires:       deepin-menu
Requires:       deepin-shortcut-viewer
Requires:       xdg-utils
BuildRequires:  cmake
BuildRequires:  fontconfig-devel
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  json-glib-devel
BuildRequires:  libgee-devel
BuildRequires:  libsecret-devel
BuildRequires:  libwnck3-devel
BuildRequires:  vala
BuildRequires:  vte291-devel

Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}

%prep
%autosetup %{version}.tar.gz#%{name}
sed -i 's|return __FILE__;|return "%{_datadir}/%{name}/project_path.c";|' ./project_path.c

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%make_build

%install
%make_install
%find_lang %{name}

%preun
if [ $1 -eq 0 ]; then
  /usr/sbin/alternatives --remove x-terminal-emulator %{_bindir}/%{name}
fi

%post
if [ $1 -eq 1 ]; then
  /usr/sbin/alternatives --install %{_bindir}/x-terminal-emulator \
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

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/dman/%{name}/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/*.desktop

%changelog
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