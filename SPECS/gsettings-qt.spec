%global 		project ~system-settings-touch
%global         _revision 82

Name:           gsettings-qt
Version:        0.1.20160329
Release:        2%{?dist}
Summary:        Qml bindings for GSettings

License:        GPL
URL:            https://launchpad.net/%{name}
Source0:        http://bazaar.launchpad.net/%{project}/%{name}/trunk/tarball/%{_revision}

Requires:       qt5-qtdeclarative
BuildRequires:  qt5-qtdeclarative-devel glib2-devel

Provides:       %{name}

%global debug_package %{nil}

%description
%{summary}

%prep
%setup -q -n %{project}/%{name}/trunk

%build
qmake-qt5 PREFIX=%{_prefix}
make

%install
DISPLAY=:0 make INSTALL_ROOT="%{buildroot}" install

%clean
rm -rf %{buildroot}

%files
%{_libdir}/*
%{_includedir}/*

%changelog
* Tue Jan 03 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.20160329-2
- Major rewrite of SPEC file
* Sun Oct 02 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.1.20160329-1
- Initial package build