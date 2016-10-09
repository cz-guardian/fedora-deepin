Name:           dde-account-faces
Version:        1.0.10
Release:        1%{?dist}
Summary:        Account faces for Linux Deepin

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildArch:      noarch
Provides:       %{name}

#%global debug_package %{nil}

%description
Account faces for Linux Deepin


%prep
%autosetup %{version}.tar.gz#%{name}

%build

%install
make DESTDIR="%{buildroot}" install

%clean
rm -rf %{buildroot}

%files
%{_var}/lib/*


%changelog
* Sun Oct 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.10-1
- Initial package build