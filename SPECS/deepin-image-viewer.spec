Name:           deepin-image-viewer
Version:        1.2.13
Release:        1%{?dist}
Summary:        Deepin Image Viewer
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  deepin-tool-kit-devel
BuildRequires:  freeimage-devel
BuildRequires:  LibRaw-devel
BuildRequires:  libexif-devel
BuildRequires:  startup-notification-devel
BuildRequires:  xcb-util-devel

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%prep
%autosetup %{version}.tar.gz#%{name}

sed -i 's/lrelease/lrelease-qt5/g' viewer/generate_translations.sh
sed -i 's|<exif-data.h|<libexif/exif-data.h|' viewer/utils/imageutils_libexif.h

%build
%qmake_qt5 PREFIX=%{_prefix}
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

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

%files
%{_bindir}/*
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/dman/%{name}/
%{_datadir}/icons/deepin/apps/scalable/*.svg
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_qt5_plugindir}/imageformats/*.so

%changelog
* Fri Apr 21 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 1.2.13-1
- Update to version 1.2.13
* Sun Apr 09 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 1.2.12-1
- Update to version 1.2.12
* Thu Jan 26 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.2.1-2
- Rewrite of spec file
* Fri Jan 20 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.2.1-1
- Update to version 1.2.1
* Fri Jan 06 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.3-2
- Fixed build dependecies
* Sat Dec 10 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.3-1
- Initial package build