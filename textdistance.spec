#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : textdistance
Version  : 4.2.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/a9/4c/96d7ff24f1bee11ade34b1daea9f70fc4c115781bbf380089470c053ef4d/textdistance-4.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/a9/4c/96d7ff24f1bee11ade34b1daea9f70fc4c115781bbf380089470c053ef4d/textdistance-4.2.0.tar.gz
Summary  : Compute distance between the two texts.
Group    : Development/Tools
License  : MIT
Requires: textdistance-license = %{version}-%{release}
Requires: textdistance-python = %{version}-%{release}
Requires: textdistance-python3 = %{version}-%{release}
Requires: numpy
BuildRequires : buildreq-distutils3
BuildRequires : numpy

%description
# TextDistance
![TextDistance logo](logo.png)
[![Build Status](https://travis-ci.org/life4/textdistance.svg?branch=master)](https://travis-ci.org/life4/textdistance) [![PyPI version](https://img.shields.io/pypi/v/textdistance.svg)](https://pypi.python.org/pypi/textdistance) [![Status](https://img.shields.io/pypi/status/textdistance.svg)](https://pypi.python.org/pypi/textdistance) [![Code size](https://img.shields.io/github/languages/code-size/life4/textdistance.svg)](https://github.com/life4/textdistance) [![License](https://img.shields.io/pypi/l/textdistance.svg)](LICENSE)

%package license
Summary: license components for the textdistance package.
Group: Default

%description license
license components for the textdistance package.


%package python
Summary: python components for the textdistance package.
Group: Default
Requires: textdistance-python3 = %{version}-%{release}

%description python
python components for the textdistance package.


%package python3
Summary: python3 components for the textdistance package.
Group: Default
Requires: python3-core
Provides: pypi(textdistance)

%description python3
python3 components for the textdistance package.


%prep
%setup -q -n textdistance-4.2.0
cd %{_builddir}/textdistance-4.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609284628
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/textdistance
cp %{_builddir}/textdistance-4.2.0/LICENSE %{buildroot}/usr/share/package-licenses/textdistance/1cd37cfcc5e8192f596e3a6bbef042ec23d05ce8
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/textdistance/1cd37cfcc5e8192f596e3a6bbef042ec23d05ce8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
