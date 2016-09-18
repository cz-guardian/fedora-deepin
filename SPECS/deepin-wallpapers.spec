Name:           deepin-wallpapers
Version:        1.3
Release:        1%{?dist}
Summary:        Deepin Wallpapers provides wallpapers of dde

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildArch:      noarch

Provides:       %{name}

%description
Deepin Wallpapers provides wallpapers of dde


%prep

%build

%install
install -d -m 755 %{buildroot}/%{_prefix}/share/wallpapers
cp -r %{_builddir}/%{name}-%{version}/deepin %{buildroot}/%{_prefix}/share/wallpapers/

install -d -m 755 %{buildroot}/%{_localstatedir}/cache
cp -r %{_builddir}/%{name}-%{version}/image-blur %{buildroot}/%{_localstatedir}/cache/

%clean
rm -rf %{buildroot}

%files
%{_prefix}/
%{_localstatedir}/

%changelog
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package