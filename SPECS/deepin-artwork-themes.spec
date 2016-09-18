Name:           deepin-artwork-themes
Version:        15.12.3
Release:        1%{?dist}
Summary:        Deepin artwork themes

License:        LGPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildArch:      noarch
Requires:       deepin-desktop-base deepin-icon-theme
BuildRequires:  python2
# faenza-icon-theme flattr-icon-theme

Provides:       %{name}

%description
Deepin artwork themes


%prep
%autosetup %{version}.tar.gz#%{name}

%build
make build

%install
%make_install PREFIX="%{_prefix}"

%clean
rm -rf %{buildroot}

%files
%{_usr}/share/personalization/*

%changelog
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build