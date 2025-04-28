%global releaseno 1

Name:           python-Metview
Version:        1.16.1
Release:        %{releaseno}%{?dist}
Summary:        Python bindings for Metview

License:        Apache License, Version 2.0
URL:            https://pypi.org/project/python-metview/
Source0:        https://pypi.org/packages/source/m/metview/metview-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-cffi
BuildRequires:  python3-numpy
BuildRequires:  python3-pandas
BuildRequires:  python3-pyyaml
BuildRequires:  python3-requests
BuildRequires:  Metview
BuildRequires:  python3-pytest

Requires:       python3-cffi
Requires:       python3-numpy
Requires:       python3-pandas
Requires:       python3-pyyaml
Requires:       python3-requests
Requires:       Metview


%description
Python bindings for Metview


%prep
%autosetup -n metview-%{version}

%build
%py3_build

%install
%py3_install

%check
# TODO: it seems that the tests are missing
# %{__python3} setup.py test

%files
%doc README.rst
%{python3_sitelib}/*


%changelog
