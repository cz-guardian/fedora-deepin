Name:           deepin-wm
Version:        1.2
Release:        1%{?dist}
Summary:        Deepin Window Manager

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       deepin-mutter deepin-desktop-schemas clutter-gtk bamf gnome-desktop libgee libwnck3 libcanberra libcanberra-gtk3
BuildRequires:  gnome-common intltool vala vala-tools bamf-devel clutter-gtk-devel libgee-devel libwnck3-devel libcanberra-devel deepin-mutter gnome-desktop3-devel gnome-desktop3

Provides:       %{name}

%description
Deepin Window Manager


%prep
%autosetup %{version}.tar.gz#%{name}

%build

%define _lib_dir %{nil}
%ifarch x86_64
  %define _lib_dir %{_usr}/lib64
%endif
%ifarch i386 i686
  %define _lib_dir %{_usr}/lib
%endif

./autogen.sh \
    --prefix='/usr' \
    --disable-schemas-compile
make

%install
%make_install PREFIX="%{_prefix}"
%ifarch x86_64
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%clean
rm -rf %{buildroot}

%files
%{_bindir}/deepin-wm
%{_usr}/include/*
%{_lib_dir}/*
%{_datarootdir}/locale/*
%{_datarootdir}/*


%changelog
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.2.0
- Update to version 1.2.0
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.2-1
- Initial package build