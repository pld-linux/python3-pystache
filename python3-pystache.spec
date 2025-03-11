#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Mustache for Python 3
Summary(pl.UTF-8):	Mustache dla Pythona 3
Name:		python3-pystache
Version:	0.6.0
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pystache/
Source0:	https://files.pythonhosted.org/packages/source/p/pystache/pystache-%{version}.tar.gz
# Source0-md5:	c834ab23ec0d4a0e47cfa281bf7bfcd1
URL:		https://pypi.org/project/pystache/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
Conflicts:	python-pystache < 0.5.4-8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pystache is a Python implementation of Mustache. Mustache is a
framework-agnostic, logic-free templating system inspired by ctemplate
and et. Like ctemplate, Mustache "emphasizes separating logic from
presentation: it is impossible to embed application logic in this
template language."

%description -l pl.UTF-8
Pystache to pythonowa implementacja Mustache. Mustache to niezależny
od szkieletu, wolny od logiki system szablonów, zainspirowany przez
ctemplate i et. Podobnie do ctemplate, Mustache kładzie nacisk na
oddzielenie logiki od prezentacji: nie da się osadzić logiki aplikacji
w tym języku szablonów".

%prep
%setup -q -n pystache-%{version}

%build
%py3_build %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/pystache/tests
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/pystache/commands/test* \
	$RPM_BUILD_ROOT%{py3_sitescriptdir}/pystache/commands/__pycache__/test* \
	$RPM_BUILD_ROOT%{_bindir}/pystache-test

%{__mv} $RPM_BUILD_ROOT%{_bindir}/pystache{,-3}
ln -sf pystache-3 $RPM_BUILD_ROOT%{_bindir}/pystache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HISTORY.md LICENSE README.md TODO.md
%attr(755,root,root) %{_bindir}/pystache
%attr(755,root,root) %{_bindir}/pystache-3
%{py3_sitescriptdir}/pystache
%{py3_sitescriptdir}/pystache-%{version}-py*.egg-info
