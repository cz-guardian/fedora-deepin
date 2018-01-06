%global repo dde-polkit-agent

Name:           deepin-polkit-agent
Version:        0.1.1
Release:        1%{?dist}
Summary:        Deepin Polkit Agent
License:        GPLv3
URL:            https://github.com/linuxdeepin/dde-polkit-agent
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

BuildRequires:  pkgconfig(dtkwidget) >= 2.0
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(polkit-qt5-1)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  qt5-linguist

%description
DDE Polkit Agent is the polkit agent used in Deepin Desktop Environment.

%prep
%setup -q -n %{repo}-%{version}
sed -i 's|lrelease|lrelease-qt5|' translate_generation.sh
sed -i 's|lib|libexec|' dde-polkit-agent.pro polkit-dde-authentication-agent-1.desktop

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%doc README.md
%license LICENSE
%{_sysconfdir}/xdg/autostart/*.desktop
%dir %{_libexecdir}/polkit-1-dde
%{_libexecdir}/polkit-1-dde/%{repo}
%{_datadir}/%{repo}/

%changelog
* Sat Jan 06 2018 Jaroslav <cz.guardian@gmail.com> Stepanek - 0.1.1-1
- Initial package build