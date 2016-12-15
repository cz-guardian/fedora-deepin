Name:           deepin-terminal
Version:        2.1.5
Release:        2%{?dist}
Summary:        Default terminal emulation application for Deepin

License:        GPL3
URL:            https://github.com/manateelazycat/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
Requires:       vala glib2 gtk3 json-glib libsecret vte291 libgee libwnck3
BuildRequires:  cmake vala glib2-devel gtk3-devel json-glib-devel libsecret-devel vte291-devel libgee-devel libwnck3-devel gettext

Provides:       %{name}

#%global debug_package %{nil}

%description
Default terminal emulation application for Deepin

%prep
%autosetup %{version}.tar.gz#%{name}
mkdir -p build
sed -i 's|return __FILE__;|return "/usr/share/deepin-terminal/project_path.c";|' ./project_path.c

%build
cd build
cmake \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DCMAKE_BUILD_TYPE=Release \
  ../
make

%install
make -C build DESTDIR="%{buildroot}" install

%clean
srm -rf %{buildroot}

%files
%{_bindir}/*
%{_datarootdir}/*

%changelog
* Thu Dec 15 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.1.5-2
- Fixed icon path
* Mon Dec 12 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 2.1.5-1
- Initial package build