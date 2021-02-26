#
# Conditional build:
%bcond_with	tests	# unit tests (broken with python 2.7 and 3+)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Mustache for Python 2
Summary(pl.UTF-8):	Mustache dla Pythona 2
Name:		python-pystache
Version:	0.5.4
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pystache/
Source0:	https://files.pythonhosted.org/packages/source/p/pystache/pystache-%{version}.tar.gz
# Source0-md5:	485885e67a0f6411d5252e69b20a35ca
URL:		https://pypi.org/project/pystache/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
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

%package -n python3-pystache
Summary:	Mustache for Python 3
Summary(pl.UTF-8):	Mustache dla Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-pystache
Pystache is a Python implementation of Mustache. Mustache is a
framework-agnostic, logic-free templating system inspired by ctemplate
and et. Like ctemplate, Mustache "emphasizes separating logic from
presentation: it is impossible to embed application logic in this
template language."

%description -n python3-pystache -l pl.UTF-8
Pystache to pythonowa implementacja Mustache. Mustache to niezależny
od szkieletu, wolny od logiki system szablonów, zainspirowany przez
ctemplate i et. Podobnie do ctemplate, Mustache kładzie nacisk na
oddzielenie logiki od prezentacji: nie da się osadzić logiki aplikacji
w tym języku szablonów".

%prep
%setup -q -n pystache-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/pystache/tests
%{__rm} $RPM_BUILD_ROOT%{py3_sitescriptdir}/pystache/commands/test* \
	$RPM_BUILD_ROOT%{py3_sitescriptdir}/pystache/commands/__pycache__/test* \
	$RPM_BUILD_ROOT%{_bindir}/pystache-test

%{__mv} $RPM_BUILD_ROOT%{_bindir}/pystache{,-3}
%endif

%if %{with python2}
%py_install

%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/pystache/tests
%{__rm} $RPM_BUILD_ROOT%{py_sitescriptdir}/pystache/commands/test* \
	$RPM_BUILD_ROOT%{_bindir}/pystache-test

%{__mv} $RPM_BUILD_ROOT%{_bindir}/pystache{,-2}
ln -sf pystache-2 $RPM_BUILD_ROOT%{_bindir}/pystache
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc HISTORY.md LICENSE README.md TODO.md
%attr(755,root,root) %{_bindir}/pystache
%attr(755,root,root) %{_bindir}/pystache-2
%{py_sitescriptdir}/pystache
%{py_sitescriptdir}/pystache-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pystache
%defattr(644,root,root,755)
%doc HISTORY.md LICENSE README.md TODO.md
%attr(755,root,root) %{_bindir}/pystache-3
%{py3_sitescriptdir}/pystache
%{py3_sitescriptdir}/pystache-%{version}-py*.egg-info
%endif
