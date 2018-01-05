Name:           deepin-desktop-base
Version:        2017.11.1
Release:        1%{?dist}
Summary:        Base component for Deepin
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-desktop-base
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Recommends:     deepin-wallpapers

%description
This package provides some components for Deepin desktop environment.

- deepin logo
- deepin desktop version
- login screen background image
- language information

%prep
%setup -q

# Remove Deepin distro's lsb-release
# Don't override systemd timeouts
# Remove apt-specific templates
sed -i -E '/lsb-release|systemd|apt/d' Makefile

# Fix data path
sed -i 's|/usr/lib|%{_datadir}|' Makefile

%build
%make_build

%install
%make_install

# Make a symlink for deepin-version
ln -sfv %{_datadir}/deepin/desktop-version %{buildroot}/etc/deepin-version

%files
%license LICENSE
%config(noreplace) %{_sysconfdir}/appstore.json
%{_sysconfdir}/deepin-version
%dir %{_datadir}/backgrounds/deepin/
%{_datadir}/backgrounds/deepin/desktop.jpg
%dir %{_datadir}/deepin/
%{_datadir}/deepin/desktop-version
%{_datadir}/distro-info/deepin.csv
%{_datadir}/i18n/i18n_dependent.json
%{_datadir}/i18n/language_info.json
%{_datadir}/plymouth/deepin-logo.png
%{_var}/cache/image-blur/*.jpg

%changelog
* Fri Jan 05 2018 Jaroslav <cz.guardian@gmail.com> Stepanek 2017.11.1-1
- Update package to version 2017.11.1
* Tue Aug 08 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2016.12.6-1
- Update package to version 2016.12.6
* Fri Mar 17 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2016.11.30-1
- Update package to version 2016.11.30
* Sun Jan 22 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 2016.11.29-1
- Update package to version 2016.11.29
* Fri Dec 16 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2016.11.28-1
- Update package to version 2016.11.28
* Sat Dec 03 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2016.02.03-1
- Update package to version 2016.02.03
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2016.02.02-1
- Initial package build