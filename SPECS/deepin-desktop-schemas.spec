Name:           deepin-desktop-schemas
Version:        3.0.12
Release:        1%{?dist}
Summary:        GSettings deepin desktop-wide schemas

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildArch:      noarch
Requires:       dconf deepin-gtk-theme deepin-sound-theme deepin-artwork-themes

Provides:       %{name}

%description
GSettings deepin desktop-wide schemas


%prep
%autosetup %{version}.tar.gz#%{name}

%build
# fix default background url
sed -i "s#^picture-uri.*#picture-uri='file:///usr/share/backgrounds/deepin_default_background.jpg'#" overrides/x86/com.deepin.wrap.gnome.desktop.override
# don't override GNOME defaults
rm overrides/x86/{org.gnome.desktop,other}.override
make

%install
%make_install PREFIX="%{_prefix}"

%clean
rm -rf %{buildroot}

%files
%{_usr}/share/glib-2.0/schemas/*

%changelog
* Sat Dec 10 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.12-1
- Update to version 3.0.11
* Thu Oct 27 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.11-1
- Update to version 3.0.11
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.10-1
- Initial package build