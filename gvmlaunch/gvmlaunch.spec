Summary: GVM Launch Support
Name: gvmlaunch
Version: 1.0
Release: R1
Source0:	 %{name}-%{version}.tar.gz
BuildRequires:		systemd-rpm-macros

License: BSD-3-Clause-Clear

%description
GVM Launch Support.

%global debug_package %{nil}

%prep
%setup -q -n %{name}

%build

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_unitdir}
%{__install} -D -m751 gvmlaunch.sh %{buildroot}/%{_bindir}/gvmlaunch.sh
%{__install} -D -m644 gvmlaunch.service %{buildroot}/%{_unitdir}/gvmlaunch.service


%files
%{_bindir}/gvmlaunch.sh
%{_unitdir}/gvmlaunch.service
