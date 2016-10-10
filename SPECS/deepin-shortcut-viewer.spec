Name:           deepin-shortcut-viewer
Version:        1.01
Release:        1%{?dist}
Summary:        Deepin Shortcut Viewer

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       qt5-qtbase
BuildRequires:  qt5-qttools-devel

Provides:       %{name}

%global debug_package %{nil}

%description
Deepin Shortcut Viewer


%prep
%autosetup %{version}.tar.gz#%{name}

%build
qmake-qt5 PREFIX=%{_usr}
make

%install
make INSTALL_ROOT="%{buildroot}" install

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*


%changelog
* Mon Oct 10 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.01-1
- Initial package build