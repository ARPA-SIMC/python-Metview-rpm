%global releaseno 3

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
BuildRequires:  python3-pip
BuildRequires:  python3-pandas
BuildRequires:  python3-pyyaml
BuildRequires:  python3-requests
BuildRequires:  Metview >= 5.0.3
BuildRequires:  python3-pytest


%description
Python bindings for Metview

%package -n python3-Metview
Summary:        Python3 bindings for Magics
Requires:       python3-cffi
Requires:       python3-numpy
Requires:       python3-pandas
Requires:       python3-pyyaml
Requires:       python3-requests
Requires:       Metview >= 5.0.3
Obsoletes:      python-Metview

%description -n python3-Metview
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

%files -n python3-Metview
%doc README.rst
%{python3_sitelib}/metview/*
%{python3_sitelib}/metview*.egg-info/*
%exclude %{python3_sitelib}/tests/*

%changelog
* Wed May 21 2025 Daniele Branchini <dbranchini@arpae.it> - 1.16.1-3
- Renamed package to python3-Metview

* Tue May 20 2025 Daniele Branchini <dbranchini@arpae.it> - 1.16.1-2
- Added python3-pip for copr Fedora build

* Mon Apr  8 2025 Emanuele Di Giacomo <edigiacomo@arpae.it> - 1.16.1-1
- Initial package
