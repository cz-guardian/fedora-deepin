%global repo go-gir-generator

Name:           deepin-gir-generator
Version:        1.0.2
Release:        1%{?dist}
Summary:        Generate static golang bindings for GObject
License:        GPLv3
URL:            https://github.com/linuxdeepin/go-gir-generator
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz
Patch0:         deepin-gir-generator_SettingsBackendLike.patch

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gudev-1.0)

%description
Generate static golang bindings for GObject

%prep
%setup -q -n %{repo}-%{version}

GIO_VER=$(v=$(rpm -q --qf %{RPMTAG_VERSION} gobject-introspection); echo ${v//./})
if [ $GIO_VER -ge 1521 ]; then
# Our gobject-introspection is too new
# https://cr.deepin.io/#/c/16880/
%patch0 -p1
fi

%build
export GOPATH="%{gopath}"
%make_build

%install
%make_install

%files
%doc README.md
%license LICENSE
%{_bindir}/gir-generator
%{gopath}/src/gir/


%changelog
* Tue Jan 02 2018 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 1.0.2-1
- Update to version 1.0.2
* Sat Apr 08 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 1.0.1-1
- Update to version 1.0.1
* Thu Jan 26 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.6-4
- Rewrite of spec file
* Wed Jan 04 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.6-3
- Renamed package to deepin-go-gir-generator
* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.6-2
- Changed lib path 
* Fri Oct 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.6-1
- Compilation rework
* Thu Sep 29 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.5-2
- Compilation rework
* Sun Sep 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 0.9.5-1
- Initial package build