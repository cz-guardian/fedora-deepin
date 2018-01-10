Name:           deepin-sound-theme
Version:        15.10.2
Release:        1%{?dist}
Summary:        Deepin sound theme
License:        GPLv3
URL:            https://github.com/linuxdeepin/deepin-sound-theme
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
Sound files for the Deeping Desktop Environment.

%prep
%setup -q

%build

%install
%make_install

%files
%doc README.md
%license LICENSE
%dir %{_datadir}/sounds/deepin/
%dir %{_datadir}/sounds/deepin/stereo/
%{_datadir}/sounds/deepin/index.theme
%{_datadir}/sounds/deepin/stereo/*.ogg

%changelog
* Wed Jan 10 2018 Jaroslav <cz.guardian@gmail.com> Stepanek - 15.10.2-1
- Update to 15.10.2
* Fri Jan 27 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 15.10.1-2
- Initial package build
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 15.10.1-1
- Initial package build