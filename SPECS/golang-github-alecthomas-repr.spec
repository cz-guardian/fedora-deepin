%global   debug_package   %{nil}

%global   provider        github
%global   provider_tld    com
%global   project         alecthomas
%global   repo            repr
# https://github.com/alecthomas/repr
%global   provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global   import_path     %{provider_prefix}
%global   commit          37578405c47fe4f23cb672045b825fa4145a0816
%global   shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-%{provider}-%{project}-%{repo}
Version:        0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Python's repr() for Go
License:        MIT
URL:            https://%{provider_prefix}
Source0:        %{url}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%description
%{summary}.

%package devel
Summary:        %{summary}
BuildArch:      noarch
BuildRequires:  golang(github.com/stretchr/testify/assert)
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}.

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.

%package unit-test-devel
Summary:        Unit tests for %{name} package
BuildArch:      noarch
# test subpackage tests code from devel subpackage
Requires:       %{name}-devel = %{version}-%{release}

%description unit-test-devel
%{summary}.

This package contains unit tests for project
providing packages with %{import_path} prefix.


%prep
%setup -q -n %{repo}-%{commit}

%build

%install
# source codes for building projects
install -d %{buildroot}%{gopath}/src/%{import_path}/
install -m644 repr.go %{buildroot}%{gopath}/src/%{import_path}/
install -m644 repr_test.go %{buildroot}%{gopath}/src/%{import_path}/

%check
export GOPATH=%{buildroot}%{gopath}:%{gopath}

%files devel
%doc README.md
%license COPYING
%dir %{gopath}/src/%{provider}.%{provider_tld}/%{project}
%{gopath}/src/%{import_path}/repr.go

%files unit-test-devel
%{gopath}/src/%{import_path}/repr_test.go

%changelog
* Tue Jan 02 2018 Jaroslav <cz.guardian@gmail.com> Stepanek - 0-0.1.git3757840
- Initial package build