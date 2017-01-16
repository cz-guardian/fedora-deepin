Name:           deepin-artwork-themes
Version:        15.12.4
Release:        1%{?dist}
Summary:        Deepin artwork themes

License:        LGPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildArch:      noarch
Requires:       deepin-desktop-base deepin-icon-theme
BuildRequires:  python2

Provides:       %{name}

%description
%{summary}


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
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 15.12.4-1
- Update package to 15.12.4
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 15.12.3-1
- Initial package build