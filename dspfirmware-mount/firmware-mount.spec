Name: dsp-firmware-mount
Version: 1.0
Release: r0
Summary: mount dsp firmware
BuildArch: noarch
License: BSD-3-Clause-Clear
Source0: %{name}-%{version}.tar.gz

Requires: systemd
BuildRequires: systemd systemd-rpm-macros
%{?systemd_requires}

%description
This rpm mount dsp firmware.

%prep
%setup -qn %{name}

%install
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig/
install -D -m 777 firmware-qcom-sa8775p.automount %{buildroot}%{_unitdir}
install -D -m 777 firmware-qcom-sa8775p.mount %{buildroot}%{_unitdir}
install -D -m 777 firmware-vm-boot.automount %{buildroot}%{_unitdir}
install -D -m 777 firmware-vm-boot.mount %{buildroot}%{_unitdir}
install -D -m 777 vendor-dsp.automount %{buildroot}%{_unitdir}
install -D -m 777 vendor-dsp.mount %{buildroot}%{_unitdir}
install -D -m 777 lpass_cfg %{buildroot}%{_sysconfdir}/sysconfig/
install -D -m 777 cdsp0_cfg %{buildroot}%{_sysconfdir}/sysconfig/
install -D -m 777 cdsp1_cfg %{buildroot}%{_sysconfdir}/sysconfig/
install -D -m 777 gpdsp0_cfg %{buildroot}%{_sysconfdir}/sysconfig/
install -D -m 777 gpdsp1_cfg %{buildroot}%{_sysconfdir}/sysconfig/
install -D -m 777 99-persist-storage-ab.rules %{buildroot}%{_sysconfdir}/udev/rules.d/99-persist-storage-ab.rules

%post
systemctl enable --now firmware-qcom-sa8775p.automount
systemctl enable --now firmware-vm-boot.automount
systemctl enable --now vendor-dsp.automount

%files
%{_unitdir}/firmware-qcom-sa8775p.automount
%{_unitdir}/firmware-qcom-sa8775p.mount
%{_unitdir}/firmware-vm-boot.automount
%{_unitdir}/firmware-vm-boot.mount
%{_unitdir}/vendor-dsp.automount
%{_unitdir}/vendor-dsp.mount
%{_sysconfdir}/sysconfig/lpass_cfg
%{_sysconfdir}/sysconfig/cdsp0_cfg
%{_sysconfdir}/sysconfig/cdsp1_cfg
%{_sysconfdir}/sysconfig/gpdsp0_cfg
%{_sysconfdir}/sysconfig/gpdsp1_cfg
%{_sysconfdir}/udev/rules.d/99-persist-storage-ab.rules
