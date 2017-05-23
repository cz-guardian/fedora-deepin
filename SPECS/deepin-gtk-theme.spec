Name:           deepin-gtk-theme
Version:        17.10.2
Release:        1%{?dist}
Summary:        Deepin GTK Theme

License:        LGPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildArch:      noarch

Provides:       %{name}

%description
Deepin GTK Theme


%prep
%autosetup %{version}.tar.gz#%{name}

%build

%install
%make_install PREFIX="%{_prefix}"

%clean
rm -rf %{buildroot}

%files
%{_usr}/share/themes/*

%changelog
* Tue May 23 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 17.10.2-1
- Update to version 17.10.2
* Sun Apr 09 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 17.10.1-1
- Update to version 17.10.1
* Sat Mar 18 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 17.10.0-1
- Update to 17.10.0
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 15.12.8-1
- Initial package build