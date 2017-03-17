Name:           deepin-wallpapers
Version:        1.4
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
%autosetup %{version}.tar.gz#%{name}

%build

%install
install -d -m 755 %{buildroot}/%{_prefix}/share/wallpapers
cp -r %{_builddir}/%{name}-%{version}/deepin %{buildroot}/%{_prefix}/share/wallpapers/

install -d -m 755 %{buildroot}/%{_localstatedir}/cache
cp -r %{_builddir}/%{name}-%{version}/image-blur %{buildroot}/%{_localstatedir}/cache/

%clean
rm -rf %{buildroot}

%files
%{_prefix}/*
%{_localstatedir}/*

%changelog
* Fri Mar 17 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.4-1
- Update to 1.4
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.3-1
- Initial package build