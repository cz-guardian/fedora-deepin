Name:           deepin-icon-theme
Version:        15.12.42
Release:        1%{?dist}
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

%install
%make_install DESTDIR="%{buildroot}"

%clean
rm -rf %{buildroot}

%files
%{_datadir}/icons/deepin/*
%{_datadir}/icons/Sea/*

%changelog
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