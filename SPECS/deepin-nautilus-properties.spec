%global debug_package %{nil}

Name:           deepin-nautilus-properties
Version:        3.14.3
Release:        2%{?dist}
Summary:        Provide file property dialog for Deepin desktop environment
License:        GPL
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}
    
BuildRequires:  exempi-devel
BuildRequires:  glib2-devel
BuildRequires:  gnome-desktop3-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libexif-devel
BuildRequires:  libnotify-devel
BuildRequires:  libX11-devel
BuildRequires:  libxml2-devel

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%prep
%autosetup %{version}.tar.gz#%{name}

%build
libtoolize && aclocal && autoheader && automake --add-missing && autoconf

%configure \
    --libexecdir=%{_libdir}/nautilus \
    --disable-nst-extension \
    --disable-update-mimedb \
    --disable-packagekit \
    --disable-introspection \
    --disable-tracker
%make_build

%install
cd src

install -d %{buildroot}%{_bindir}
install -m755 %{name} deepin-open-chooser %{buildroot}%{_bindir}/

%clean
rm -rf %{buildroot}

%files
%doc README
%license COPYING
%{_bindir}/*

%changelog
* Fri Jan 27 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.14.3-2
- Rewrite of spec file
* Sun Oct 02 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.14.3-1
- Initial package build