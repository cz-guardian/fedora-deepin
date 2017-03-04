Name:           deepin-grub2-themes
Version:        1.0.0
Release:        2%{?dist}
Summary:        Deepin grub2 themes
License:        LGPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
Deepin grub2 themes


%prep
%autosetup %{version}.tar.gz#%{name}

%install
%make_install TARGET="%{buildroot}/boot/grub2/themes"

%clean
rm -rf %{buildroot}

%files
/boot/grub2/themes/deepin

%changelog
* Thu Jan 26 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.0-2
- Rewrite of spec file
* Sat Dec 03 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.0-1
- Initial package build