#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-textdistance
Version  : 4.3.0
Release  : 19
URL      : https://files.pythonhosted.org/packages/06/7d/144b629a98782a777b014400eecc6e12630581577591dd4dbfa3a5353443/textdistance-4.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/06/7d/144b629a98782a777b014400eecc6e12630581577591dd4dbfa3a5353443/textdistance-4.3.0.tar.gz
Summary  : Compute distance between the two texts.
Group    : Development/Tools
License  : MIT
Requires: pypi-textdistance-license = %{version}-%{release}
Requires: pypi-textdistance-python = %{version}-%{release}
Requires: pypi-textdistance-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
# TextDistance
![TextDistance logo](logo.png)
[![Build Status](https://travis-ci.org/life4/textdistance.svg?branch=master)](https://travis-ci.org/life4/textdistance) [![PyPI version](https://img.shields.io/pypi/v/textdistance.svg)](https://pypi.python.org/pypi/textdistance) [![Status](https://img.shields.io/pypi/status/textdistance.svg)](https://pypi.python.org/pypi/textdistance) [![License](https://img.shields.io/pypi/l/textdistance.svg)](LICENSE)

%package license
Summary: license components for the pypi-textdistance package.
Group: Default

%description license
license components for the pypi-textdistance package.


%package python
Summary: python components for the pypi-textdistance package.
Group: Default
Requires: pypi-textdistance-python3 = %{version}-%{release}

%description python
python components for the pypi-textdistance package.


%package python3
Summary: python3 components for the pypi-textdistance package.
Group: Default
Requires: python3-core
Provides: pypi(textdistance)

%description python3
python3 components for the pypi-textdistance package.


%prep
%setup -q -n textdistance-4.3.0
cd %{_builddir}/textdistance-4.3.0
pushd ..
cp -a textdistance-4.3.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656513981
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-textdistance
cp %{_builddir}/textdistance-4.3.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-textdistance/1cd37cfcc5e8192f596e3a6bbef042ec23d05ce8
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-textdistance/1cd37cfcc5e8192f596e3a6bbef042ec23d05ce8

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
