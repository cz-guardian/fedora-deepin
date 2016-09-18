Name:           deepin-desktop-base
Version:        2016.02.02
Release:        1%{?dist}
Summary:        Base component for Deepin

License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildArch:      noarch
Requires:       deepin-wallpapers

Provides:       %{name}

%description
Base component for Deepin


%prep
%autosetup %{version}.tar.gz#%{name}

%build
make

%install
%make_install PREFIX="%{_prefix}"

# Remove Deepin distro's lsb-release
rm %{buildroot}/etc/lsb-release

# Don't override systemd timeouts
rm -r %{buildroot}/etc/systemd

# Rename default desktop file to avoid conflicts
mv %{buildroot}/usr/share/backgrounds/{desktop.jpg,deepin_default_background.jpg}

# Make a symlink for deepin-version
ln -s /usr/lib/deepin/desktop-version %{buildroot}/etc/deepin-version

# Remove apt-specific templates
rm -r %{buildroot}/usr/share/python-apt

%clean
rm -rf %{buildroot}

%files
%{_sysconfdir}/*
%{_usr}/lib/*
%{_usr}/share/*

%changelog
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek
- Initial package build