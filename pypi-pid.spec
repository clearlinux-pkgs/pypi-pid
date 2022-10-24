#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD6E95F20305701A1 (trbs@trbs.net)
#
Name     : pypi-pid
Version  : 3.0.4
Release  : 21
URL      : https://files.pythonhosted.org/packages/46/45/9e551a0e30d68d18334bc6fd8971b3ab1485423877902eb4f26cc28d7bd5/pid-3.0.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/46/45/9e551a0e30d68d18334bc6fd8971b3ab1485423877902eb4f26cc28d7bd5/pid-3.0.4.tar.gz
Source1  : https://files.pythonhosted.org/packages/46/45/9e551a0e30d68d18334bc6fd8971b3ab1485423877902eb4f26cc28d7bd5/pid-3.0.4.tar.gz.asc
Summary  : Pidfile featuring stale detection and file-locking, can also be used as context-manager or decorator
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-pid-license = %{version}-%{release}
Requires: pypi-pid-python = %{version}-%{release}
Requires: pypi-pid-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(psutil)
BuildRequires : pypi-pytest

%description
===

%package license
Summary: license components for the pypi-pid package.
Group: Default

%description license
license components for the pypi-pid package.


%package python
Summary: python components for the pypi-pid package.
Group: Default
Requires: pypi-pid-python3 = %{version}-%{release}

%description python
python components for the pypi-pid package.


%package python3
Summary: python3 components for the pypi-pid package.
Group: Default
Requires: python3-core
Provides: pypi(pid)
Requires: pypi(psutil)

%description python3
python3 components for the pypi-pid package.


%prep
%setup -q -n pid-3.0.4
cd %{_builddir}/pid-3.0.4
pushd ..
cp -a pid-3.0.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656394173
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python -m pytest
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pid
cp %{_builddir}/pid-3.0.4/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pid/790bd88a7078375e9e85a058079a7d663ccf9273
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pid/790bd88a7078375e9e85a058079a7d663ccf9273

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
