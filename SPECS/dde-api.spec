Name:           dde-api
Version:        3.0.14
Release:        1%{?dist}
Summary:        Deepin GoLang Library

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildArch:      noarch
Provides:       %{name}

%global debug_package %{nil}

%description
Deepin GoLang Library


%prep
%autosetup %{version}.tar.gz#%{name}

%build

%install
install -d -m 755 %{buildroot}/usr/src/pkg.deepin.io/dde/api
cp -r %{_builddir}/%{name}-%{version}/* %{buildroot}/usr/src/pkg.deepin.io/dde/api/

%clean
rm -rf %{buildroot}

%files
%{_usrsrc}/*


%changelog
* Wed Sep 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build