Name:           mock-elemc
Version:        19
Release:        1%{?dist}
Summary:        Mock config files for the Elemc repository

Group:          Development/Tools
License:        GPLv3
URL:            http://repo.elemc.name/repos
Source0:        http://repo.elemc.name/repos/sources/%{name}/%{name}-%{version}.tar.xz

BuildArch:      noarch
Requires:       mock

%description
Mock config files for the Elemc Repository


%prep
%setup -q -c


%build
#Nothing to build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/mock
install -pm 0644 *.cfg $RPM_BUILD_ROOT%{_sysconfdir}/mock


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/mock/elemc-*.cfg


%changelog
* Mon Aug 05 2013 Alexei Panov <me AT elemc DOT name> 19-1
- Initial package

