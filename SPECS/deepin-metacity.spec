Name:           deepin-metacity
Version:        3.22.0
Release:        2%{?dist}
Summary:        2D window manager for Deepin

License:        GPL
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       dconf deepin-desktop-schemas libcanberra startup-notification zenity gtk3 libgtop2 libSM yelp bamf
BuildRequires:  intltool itstool python yelp-devel autoconf-archive glib2-devel libtool gtk3-devel gsettings-desktop-schemas-devel libcanberra-devel bamf-devel json-glib-devel zenity yelp-tools startup-notification-devel

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

%define _lib_dir %{nil}
%ifarch x86_64
  %define _lib_dir %{_usr}/lib64
%endif
%ifarch i386 i686
  %define _lib_dir %{_usr}/lib
%endif

./autogen.sh --prefix=/usr --sysconfdir=/etc --localstatedir=/var --libexecdir=%{_lib_dir}/$pkgname \
               --disable-static --disable-schemas-compile
cat configure
make

%install
%make_install PREFIX="%{_prefix}"
%ifarch x86_64
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif
#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_libdir}/pkgconfig/*
%{_datarootdir}/*

%files devel
%{_includedir}/*
%{_libdir}/lib*.so

%changelog
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.22.0-1
- Update to version 3.22.0
* Thu Jan 05 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.20.6-2
- Split the package to main and devel
* Fri Dec 16 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.20.6-1
- Update to version 3.20.6
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.20.5-1
- Initial package build