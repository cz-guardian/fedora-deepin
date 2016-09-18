Name:           deepin-icon-theme
Version:        15.12.32
Release:        1%{?dist}
Summary:        Deepin Icons

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildArch:      noarch
Requires:       deepin-wallpapers
BuildRequires:  inkscape
# faenza-icon-theme flattr-icon-theme

Provides:       %{name}

%description
Deepin Icons


%prep
%autosetup %{version}.tar.gz#%{name}

%build
mkdir -p build
python2 tools/convert.py deepin build

%install
%make_install PREFIX="%{_prefix}"

%clean
rm -rf %{buildroot}

%files
%{_usr}/share/icons/*

%changelog
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build