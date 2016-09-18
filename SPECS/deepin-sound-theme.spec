Name:           deepin-sound-theme
Version:        15.10.1
Release:        1%{?dist}
Summary:        Deepin sound theme

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildArch:      noarch

Provides:       %{name}

%description
Deepin sound theme


%prep
%autosetup %{version}.tar.gz#%{name}

%build

%install
%make_install PREFIX="%{_prefix}"

%clean
rm -rf %{buildroot}

%files
%{_usr}/share/sounds/*

%changelog
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build