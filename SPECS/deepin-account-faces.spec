%global 		srcname dde-account-faces

Name:           deepin-account-faces
Version:        1.0.10
Release:        2%{?dist}
Summary:        Account faces for Linux Deepin
License:        GPL3
URL:            https://github.com/linuxdeepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildArch:      noarch
Provides:       %{name}

Provides:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{srcname}%{?_isa} < %{version}-%{release}

%description
%{description}


%prep
%autosetup %{version}.tar.gz#%{name} -n %{srcname}-%{version}

%build

%install
%make_install INSTALL_ROOT=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%{_var}/lib/AccountsService/icons/*


%changelog
* Mon Jan 23 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.10-2
- Renamed to deepin-account-faces
* Sun Oct 09 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.10-1
- Initial package build