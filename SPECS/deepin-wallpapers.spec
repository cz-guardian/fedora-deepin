%global commit 704a515cfa304dcda37e42b5aa0330e02c1da54f
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           deepin-wallpapers
Version:        1.7
Release:        1%{?dist}
Summary:        Deepin Wallpapers provides wallpapers of dde
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-wallpapers
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
BuildArch:      noarch

%description
Deepin Wallpapers provides wallpapers of dde

%prep
%setup -q -n %{name}-%{commit}

%build

%install
install -d %{buildroot}/%{_datadir}/wallpapers/
cp -ar deepin %{buildroot}/%{_datadir}/wallpapers/

install -d %{buildroot}/%{_var}/cache/
cp -ar image-blur %{buildroot}/%{_var}/cache/

%files
%doc README.md
%license LICENSE
%{_datadir}/wallpapers/deepin/
%{_var}/cache/image-blur/

%changelog
* Fri Jan 05 2018 Jaroslav <cz.guardian@gmail.com> Stepanek 1.7-1
- Update to 1.7
* Fri Mar 17 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.4-1
- Update to 1.4
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.3-1
- Initial package build