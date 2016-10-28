Name:           deepin-metacity
Version:        3.20.5
Release:        1%{?dist}
Summary:        2D window manager for Deepin

License:        GPL
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       dconf deepin-desktop-schemas libcanberra startup-notification zenity gtk3 libgtop2 libSM yelp bamf
BuildRequires:  intltool itstool python yelp-devel autoconf-archive glib2-devel libtool gtk3-devel gsettings-desktop-schemas-devel libcanberra-devel bamf-devel json-glib-devel zenity

Provides:       %{name}

%description
2D window manager for Deepin


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
make

%install
%make_install PREFIX="%{_prefix}"
%ifarch x86_64
  mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_usr}/include/*
%{_lib_dir}/*
%{_datarootdir}/*


%changelog
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build