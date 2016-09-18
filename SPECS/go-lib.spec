Name:           go-lib
Version:        0.5.1
Release:        1%{?dist}
Summary:        Deepin GoLang Library

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Provides:       %{name}

%global debug_package %{nil}

%description
Deepin GoLang Library


%prep
%autosetup %{version}.tar.gz#%{name}

%build

%install
install -d -m 755 %{buildroot}/usr/src/pkg.deepin.io/lib
cp -r %{_builddir}/%{name}-%{version}/* %{buildroot}/usr/src/pkg.deepin.io/lib/

%clean
rm -rf %{buildroot}

%files
%{_usrsrc}/*


%changelog
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build