Name:           deepin-sound-theme
Version:        15.10.1
Release:        2%{?dist}
Summary:        Deepin sound theme
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

BuildArch:      noarch

Provides:       %{name}

%description
Deepin sound theme


%prep
%autosetup %{version}.tar.gz#%{name}

%build

%install
%make_install PREFIX="%{_prefix}"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{_datadir}/sounds/deepin/
%dir %{_datadir}/sounds/deepin/stereo/
%{_datadir}/sounds/deepin/*.theme
%{_datadir}/sounds/deepin/stereo/*.ogg

%changelog
* Fri Jan 27 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 15.10.1-2
- Initial package build
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 15.10.1-1
- Initial package build