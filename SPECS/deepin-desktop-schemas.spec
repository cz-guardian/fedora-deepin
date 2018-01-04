Name:           deepin-desktop-schemas
Version:        3.2.4
Release:        1%{?dist}
Summary:        GSettings deepin desktop-wide schemas
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-desktop-schemas
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python
BuildRequires:  glib2
Requires:       dconf
Requires:       deepin-gtk-theme
Requires:       deepin-sound-theme
Requires:       deepin-artwork-themes

%description
GSettings deepin desktop-wide schemas.

%prep
%setup -q

# fix default background url
sed -i '/picture-uri/s|default_background.jpg|default.png|' overrides/common/com.deepin.wrap.gnome.desktop.override

%build
%make_build ARCH=x86

%install
%make_install PREFIX=%{_prefix}

%check
make test

%files
%doc README.md
%license LICENSE
%{_datadir}/glib-2.0/schemas/*

%changelog
* Thu Jan 04 2018 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 3.2.4-1
- Update to version 3.2.4
* Mon May 01 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 3.1.6-1
- Update to version 3.1.6
* Sun Apr 09 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 3.1.5-1
- Update to version 3.1.5
* Sat Mar 18 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.3-1
- Update to version 3.1.3
* Sat Mar 04 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.1-1
- Update to version 3.1.1
* Wed Jan 25 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.13-2
- Rewrite of spec file
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.13-1
- Update to version 3.0.13
* Sat Dec 10 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.12-1
- Update to version 3.0.12
* Thu Oct 27 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.11-1
- Update to version 3.0.11
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.10-1
- Initial package build