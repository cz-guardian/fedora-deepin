Name:           deepin-desktop-schemas
Version:        3.1.1
Release:        1%{?dist}
Summary:        GSettings deepin desktop-wide schemas
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildArch:      noarch
Requires:       dconf
Requires:       deepin-artwork-themes
Requires:       deepin-gtk-theme
Requires:       deepin-sound-theme

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%prep
%autosetup %{version}.tar.gz#%{name}

# fix default background url
sed -i '/picture-uri/s|default_background.jpg|default.png|' overrides/x86/com.deepin.wrap.gnome.desktop.override
# don't override GNOME defaults
rm overrides/x86/{org.gnome.desktop,other}.override

%build
%make_build

%install
%make_install PREFIX="%{_prefix}"

%clean
rm -rf %{buildroot}

%files
%doc README.md
%{_datarootdir}/glib-2.0/schemas/*

%changelog
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