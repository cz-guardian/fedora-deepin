Name:           deepin-icon-theme
Version:        15.12.32
Release:        2%{?dist}
Summary:        Deepin Icons
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildArch:      noarch

BuildRequires:  inkscape
BuildRequires:  python-devel

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%prep
%autosetup %{version}.tar.gz#%{name}
sed -i 's/flattr/Flattr/' deepin/index.theme

%build
mkdir -p build
%{__python2} tools/convert.py deepin build

%install
%make_install PREFIX="%{_prefix}"

%clean
rm -rf %{buildroot}

%files
%{_datadir}/icons/deepin

%changelog
* Thu Jan 26 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 15.12.32-2
- Rewrite of spec file
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 15.12.32-1
- Initial package build