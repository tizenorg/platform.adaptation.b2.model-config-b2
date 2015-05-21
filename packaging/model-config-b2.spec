Name:		model-config-b2
Summary:	A Model configuration
Version:	0.0.1
Release:	1
Group:		System/Configuration
License:	Apache-2.0
BuildArch:	noarch
Source0:	%{name}-%{version}.tar.gz

%description
Model configuration data package

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/config
cp -f model-config.xml %{buildroot}%{_sysconfdir}/config/model-config.xml

mkdir -p %{buildroot}%{_sharedstatedir}/buxton
mkdir -p %{buildroot}%{_libdir}/buxton
cp -f init-buxton-config.sh %{buildroot}%{_libdir}/buxton/init-buxton-config.sh

%posttrans
%{_libdir}/buxton/init-buxton-config.sh
rm -rf %{_libdir}/buxton/init-buxton-config.sh

%files
%dir %{_sharedstatedir}/buxton
%config %{_sysconfdir}/config/model-config.xml
%{_libdir}/buxton/init-buxton-config.sh
%manifest model-config.manifest
