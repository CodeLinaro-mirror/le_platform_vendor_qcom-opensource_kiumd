Name: gvm_net_config
Version: 1.1
Release: 2%{?dist}
Summary: configure network for GVM
BuildArch: noarch
License: BSD-3-Clause-Clear

BuildRequires: systemd-rpm-macros

%{?systemd_requires}
Requires: systemd

Source0: %{name}-%{version}.tar.gz

%define _binaries_in_noarch_packages_terminate_build   0

%description
This rpm will install the systemd service gvm_net_config.service.
gmv_net_config.service will be used to setup the network bridge for gvm.

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/usr/local/bin
install -DpZm 0755 gvm_net_config.sh %{buildroot}/usr/local/bin
install -DpZm 0644 gvm_net_config.service %{buildroot}%{_unitdir}

%files
/usr/local/bin/gvm_net_config.sh
%{_unitdir}/gvm_net_config.service

%post
systemctl enable gvm_net_config.service

%preun
%systemd_preun gvm_net_config.service

%postun
%systemd_postun_with_restart gvm_net_config.service
