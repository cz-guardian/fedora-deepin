%global 		srcname deepin-ui
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:           python2-%{srcname}
Version:        1.0.5
Release:        2%{?dist}
Summary:        UI toolkit for Linux Deepin

License:        GPL
URL:            https://github.com/martyr-deepin/%{srcname}
Source0:        %{url}/archive/%{version}.tar.gz#%{name}

Requires:       python2-deepin-utils python2-deepin-gsettings glib2 pygtk2 pycairo python2-scipy python-pillow python-xlib pywebkitgtk libsoup
BuildRequires:  python2-devel python2-setuptools webkitgtk-devel deepin-gettext-tools

Provides:       %{name}

%global debug_package %{nil}

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
%{__python2} setup.py install -O1 --root="%{buildroot}"

%clean
rm -rf %{buildroot}

%files
%{python2_sitelib}/*


%changelog
* Tue Jan 03 2017 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.5-2
- Major rewrite of SPEC file
* Wed Oct 12 2016 Jaroslav <cz.guardian@gmail.com> Stepanek 1.0.5-1
- Initial package build