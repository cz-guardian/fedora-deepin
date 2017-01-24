Name:           deepin-movie
Version:        2.2.11
Release:        2%{?dist}
Summary:        Movie player based on QtAV
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
  
Requires:       dbus-python
Requires:       deepin-dbus-factory
Requires:       deepin-menu
Requires:       deepin-qml-widgets
Requires:       mediainfo
Requires:       python-bottle
Requires:       python-magic
Requires:       python-qt5
Requires:       python-xpyb
Requires:       python2-ass
Requires:       python2-deepin-utils
Requires:       python2-peewee
Requires:       python2-pyopengl
Requires:       python2-pysrt
Requires:       python2-requests
Requires:       python2-xpybutil
Requires:       qtav-qml-module
BuildRequires:  deepin-gettext-tools
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  python-devel

BuildArch:      noarch

Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%prep
%autosetup %{version}.tar.gz#%{name} -p1
# fix python version
find src -type f | xargs sed -i 's=\(^#! */usr/bin.*\)python *$=\1python2='

%build
%{__python2} configure.py
deepin-generate-mo locale/locale_config.ini

%install
%make_install PREFIX="%{_prefix}"
chmod 0755 %{buildroot}%{_datadir}/%{name}/main.py

%find_lang %{name}

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

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
%{_bindir}/*
%{_datadir}/%{name}/*
%{_datadir}/dman/%{name}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*

%changelog
* Tue Jan 24 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.2.11-2
- Fix broken python-bottle dependency
* Tue Jan 24 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2.2.11-1
- Update to version 2.2.11
* Wed Dec 21 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.2.10-1
- Initial package build