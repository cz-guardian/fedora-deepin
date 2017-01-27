%global 		srcname deepin-ui

Name:           python2-%{srcname}
Version:        1.0.5
Release:        3%{?dist}
Summary:        UI toolkit for Linux Deepin
License:        GPL
URL:            https://github.com/martyr-deepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       libsoup
Requires:       pycairo
Requires:       pygtk2
Requires:       python-pillow
Requires:       python-xlib
Requires:       python2-deepin-gsettings
Requires:       python2-deepin-utils
Requires:       python2-scipy
Requires:       pywebkitgtk
BuildRequires:  cairo-devel
BuildRequires:  deepin-gettext-tools
BuildRequires:  gettext
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pygtk2-devel
BuildRequires:  python-devel
BuildRequires:  python2-setuptools
BuildRequires:  webkitgtk-devel

BuildArch:      noarch

Provides:       %{name}
Provides:       %{name}%{?_isa} = %{version}-%{release}

%description
%{summary}


%prep
%setup -q -n %{srcname}-%{version}
# fix python version
find -iname "*.py" -type f | xargs sed -i 's=\(^#! */usr/bin.*\)python *$=\1python2='

%build
%{__python2} setup.py build
deepin-generate-mo dtk/tools/locale_config.ini

%install
%{__python2} setup.py install -O1 --prefix=%{_prefix} --root=%{buildroot}

# locale files
rm -rf dtk/locale/deepin-ui.pot
pushd dtk/locale
for i in `ls *.po`
 do
    install -d %{buildroot}%{_datadir}/locale/${i%.*}/LC_MESSAGES/
    msgfmt $i -o %{buildroot}%{_datadir}/locale/${i%.*}/LC_MESSAGES/%{srcname}.mo
 done
popd

%find_lang %{srcname}

%clean
rm -rf %{buildroot}

%files -f %{srcname}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING FAQ TODO README
%{python_sitelib}/*


%changelog
* Fri Jan 27 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.5-3
- Rewrite of spec file
* Tue Jan 03 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.5-2
- Major rewrite of SPEC file
* Wed Oct 12 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.5-1
- Initial package build