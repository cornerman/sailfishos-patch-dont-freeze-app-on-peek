Name: sailfishos-patch-dont-freeze-app-on-peek
BuildArch: noarch
Summary: Do not freeze the pixmap of the current app when peeking at home
Version: 0.0.1
Release: 1
Group: System/Patches
License: TODO
Source0: %{name}-%{version}.tar.xz
Requires: patchmanager
Requires: sailfish-version >= 2.0.1

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/usr/share/patchmanager/patches/%{name}
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/%{name}

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/%{name}
