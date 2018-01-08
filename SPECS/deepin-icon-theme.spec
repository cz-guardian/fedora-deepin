Name:           deepin-icon-theme
Version:        15.12.52
Release:        1%{?dist}
Summary:        Icons for the Deepin Desktop Environment
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-icon-theme
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel

%description
Icons for the Deepin Desktop Environment.

%prep
%setup -q

%build

%install
%make_install PREFIX=%{_prefix}

%post
touch --no-create %{_datadir}/icons/deepin &>/dev/null || :
touch --no-create %{_datadir}/icons/Sea &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
  touch --no-create %{_datadir}/icons/deepin &>/dev/null
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/deepin &>/dev/null || :
  touch --no-create %{_datadir}/icons/Sea &>/dev/null
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Sea &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/deepin &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Sea &>/dev/null || :

%files
%license LICENSE
%{_datadir}/icons/deepin/
%{_datadir}/icons/Sea/

%changelog
* Mon Jan 08 2018 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 15.12.52-1
- Update to 15.12.52
* Tue May 23 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 15.12.42-1
- Update to 15.12.42
* Wed Apr 19 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 15.12.39-1
- Update to 15.12.39
* Mon Mar 20 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 15.12.35-1
- Update to 15.12.35
* Fri Mar 03 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 15.12.33-1
- Update to 15.12.33
* Thu Jan 26 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 15.12.32-2
- Rewrite of spec file
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 15.12.32-1
- Initial package build