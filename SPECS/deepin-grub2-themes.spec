Name:           deepin-grub2-themes
Version:        1.0.0
Release:        1%{?dist}
Summary:        Deepin grub2 themes

License:        LGPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Provides:       %{name}

%description
Deepin grub2 themes


%prep
%autosetup %{version}.tar.gz#%{name}

%install
make DESTDIR="%{buildroot}" install

%clean
rm -rf %{buildroot}

%files
/boot/grub/themes/*

%changelog
* Sat Dec 03 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.0-1
- Initial package build