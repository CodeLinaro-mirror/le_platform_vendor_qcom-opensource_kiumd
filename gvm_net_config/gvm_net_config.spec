Name: gvm_net_config
Version: 1.0
Release: 2%{?dist}
Summary: configure network for GVM
BuildArch: noarch
License: BSD-3-Clause-Clear
Source0: %{name}-%{version}.tar.gz

%define _binaries_in_noarch_packages_terminate_build   0

%description
This rpm configure gvm.

%prep
%setup -qn %{name}

%install
mkdir -p "$RPM_BUILD_ROOT/firmware/"
install -D -m 777 install.sh "$RPM_BUILD_ROOT/firmware/"

%files
/firmware/install.sh

%post
/firmware/install.sh
