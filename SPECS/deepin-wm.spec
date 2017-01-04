Name:           deepin-wm
Version:        1.2
Release:        2%{?dist}
Summary:        Deepin Window Manager

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       deepin-mutter deepin-desktop-schemas clutter-gtk bamf gnome-desktop libgee libwnck3 libcanberra libcanberra-gtk3
BuildRequires:  gnome-common intltool vala vala-tools bamf-devel clutter-gtk-devel libgee-devel libwnck3-devel libcanberra-devel deepin-mutter-devel gnome-desktop3-devel gnome-desktop3 upower-devel libxkbcommon-x11-devel libgudev-devel libxkbfile-devel

Provides:       %{name}

%description
%{summary}


%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files and libraries for %{name}


%prep
%autosetup %{version}.tar.gz#%{name}

%build
./autogen.sh \
    --prefix='%{_usr}' \
    --disable-schemas-compile
make

%install
%make_install PREFIX="%{_prefix}"
#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Correct the library path for x86_64
%ifarch x86_64
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%clean
rm -rf %{buildroot}

%files
%{_bindir}/deepin-wm
%{_libdir}/lib*.so.*
%{_datarootdir}/locale/*
%{_libdir}/%{name}/*
%{_libdir}/pkgconfig/*
%{_datarootdir}/*

%files devel
%{_includedir}/*
%{_libdir}/lib*.so

%changelog
* Wed Jan 04 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.2.0-2
- Split the package to main and devel
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.2.0-1
- Update to version 1.2.0
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.1.2-1
- Initial package build