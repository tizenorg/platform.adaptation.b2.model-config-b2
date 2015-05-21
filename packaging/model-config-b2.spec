Name:		model-config-b2
Summary:	A Model configuration
Version:	0.0.1
Release:	1
Group:		System/Configuration
License:	Apache License, Version 2.0
BuildArch:	noarch
Source0:	%{name}-%{version}.tar.gz

%description
Model configuration data package

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/etc/config
cp -f model-config.xml %{buildroot}/etc/config/model-config.xml

mkdir -p %{buildroot}%{_sharedstatedir}/buxton
mkdir -p %{buildroot}/usr/lib/buxton
cp -f init-buxton-config.sh %{buildroot}/usr/lib/buxton/init-buxton-config.sh

%posttrans
/usr/lib/buxton/init-buxton-config.sh
rm -rf /usr/lib/buxton/init-buxton-config.sh

%files
%dir %{_sharedstatedir}/buxton
/etc/config/model-config.xml
/usr/lib/buxton/init-buxton-config.sh
%manifest model-config.manifest
