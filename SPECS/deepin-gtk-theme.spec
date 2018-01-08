Name:           deepin-gtk-theme
Version:        17.10.5
Release:        1%{?dist}
Summary:        Deepin GTK Theme
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-gtk-theme
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
Deepin GTK Theme

%prep
%setup -q

%build

%install
%make_install PREFIX=%{_prefix}

%files
%doc README.md
%license LICENSE
%{_datadir}/themes/deepin/
%{_datadir}/themes/deepin-dark/

%changelog
* Mon Jan 08 2018 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek - 17.10.5-1
- Update to version 17.10.5
* Tue May 23 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 17.10.2-1
- Update to version 17.10.2
* Sun Apr 09 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 17.10.1-1
- Update to version 17.10.1
* Sat Mar 18 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 17.10.0-1
- Update to 17.10.0
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 15.12.8-1
- Initial package build