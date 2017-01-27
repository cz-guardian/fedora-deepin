# for fedora 24
%global _qt5_qmldir %{_qt5_archdatadir}/qml

Name:           deepin-qml-widgets
Version:        2.3.4
Release:        3%{?dist}
Summary:        Deepin QML widgets
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
BuildRequires:  deepin-gettext-tools
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  pkgconfig
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtquick1-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qtx11extras-devel

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%prep
%autosetup %{version}.tar.gz#%{name}

%build
%qmake_qt5
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

pushd locale
for i in `ls *.po`
 do
    install -d %{buildroot}%{_datadir}/locale/${i%.*}/LC_MESSAGES/
    msgfmt $i -o %{buildroot}%{_datadir}/locale/${i%.*}/LC_MESSAGES/%{name}.mo
 done
popd

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%{_bindir}/*
%{_qt5_qmldir}/Deepin/*
%{_datadir}/dbus-1/services/*.service

%changelog
* Fri Jan 27 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.4-3
- Rewrite of spec file
* Thu Jan 12 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.4-2
- Bump to newer version because of copr
* Sun Dec 11 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.3.4-1
- Initial package build