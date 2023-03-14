# If kversion isn't defined on the rpmbuild line, define it here.
%{!?kversion: %define kversion %(uname -r)}

Name: kiumd-headers
Version: 1.0
Release: r0
Summary: install kiumd uapi headers
BuildArch: noarch
License: GPL-2.0-only WITH Linux-syscall-note
Source0: %{name}-%{version}.tar.gz

BuildRequires:	kernel-automotive-devel-uname-r = %{kversion}

%description
This contains headers userspace API and DLKM conf files.

%prep
%setup -qn %{name}

KERNEL_SRC="/usr/src/kernels"
CURDIR=${PWD}
cd ${KERNEL_SRC}/%{kversion}/
scripts/headers_install.sh ${CURDIR}/kiumd.h ${CURDIR}/kiumd.h
scripts/headers_install.sh ${CURDIR}/scmioctl.h ${CURDIR}/scmioctl.h

%install
rm -rf "$RPM_BUILD_ROOT"
mkdir -p "$RPM_BUILD_ROOT/usr/include/uapi/misc/"
mkdir -p  "$RPM_BUILD_ROOT/usr/lib/modules-load.d"
cp kiumd.h  $RPM_BUILD_ROOT/usr/include/uapi/misc/
cp scmioctl.h  $RPM_BUILD_ROOT/usr/include/uapi/misc/
cp kiumd.conf "$RPM_BUILD_ROOT/usr/lib/modules-load.d"
cp vfioiommu.conf "$RPM_BUILD_ROOT/usr/lib/modules-load.d"
cp appspinctrl.conf "$RPM_BUILD_ROOT/usr/lib/modules-load.d"

%files
%{_includedir}/uapi/misc/kiumd.h
%{_includedir}/uapi/misc/scmioctl.h
/usr/lib/modules-load.d/kiumd.conf
/usr/lib/modules-load.d/vfioiommu.conf
/usr/lib/modules-load.d/appspinctrl.conf



