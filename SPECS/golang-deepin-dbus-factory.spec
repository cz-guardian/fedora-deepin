%global   debug_package   %{nil}
%global   repo            dbus-factory
%global   import_path     dbus

Name:           golang-deepin-%{repo}
Version:        3.1.12
Release:        1%{?dist}
Summary:        Golang DBus factory for Deepin Desktop Environment
License:        GPLv3+
URL:            https://github.com/linuxdeepin/dbus-factory
Source0:        %{url}/archive/%{version}/%{repo}-%{version}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

BuildRequires:  golang(pkg.deepin.io/lib)
BuildRequires:  deepin-dbus-generator
BuildRequires:  jq
BuildRequires:  libxml2
Provides:       deepin-go-%{repo} = %{version}-%{release}
Obsoletes:      deepin-go-%{repo} < %{version}-%{release}

%description
Golang DBus factory for Deepin Desktop Environment.

%package devel
Summary:        %{summary}
BuildArch:      noarch

%description devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%prep
%setup -q -n %{repo}-%{version}

%build
%make_build

%install
%make_install GOPATH=%{gopath}

%files devel
%doc README.md
%license LICENSE
%{gopath}/src/dbus/

%changelog
* Tue Jan 02 2018 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 3.1.12-1
- Update to version 3.1.12
* Wed Apr 19 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 3.1.4-1
- Update to version 3.1.4
* Sat Apr 08 2017 Jaroslav <jaroslav.stepanek@tinos.cz> Stepanek 3.1.3-1
- Update to version 3.1.3
* Sat Mar 18 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.2-1
- Update to version 3.1.2
* Sun Mar 05 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.1.0-1
- Update to version 3.1.0
* Wed Jan 25 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.9-2
- Spec file rewrite
* Mon Jan 16 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.9-1
- Update to version 3.0.9 and renamed to deepin-dbus-factory
* Sun Dec 18 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.8-1
- Update to version 3.0.8
* Thu Sep 29 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.6-2
- Compilation rework
* Wed Sep 28 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 3.0.6-1
- Initial package build