#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	iptables
Summary:	Python 2 bindings for iptables
Summary(pl.UTF-8):	Wiązania Pythona 2 do iptables
Name:		python-%{module}
Version:	0.10.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://github.com/ldx/python-iptables/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c60e67cc14ad734b995016dbc29c29ee
URL:		https://github.com/ldx/python-iptables
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with doc}
BuildRequires:	sphinx-pdg
%endif
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-modules >= 1:3.3
%endif
Requires:	python-modules >= 1:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 bindings for iptables.

%description -l pl.UTF-8
Wiązania Pythona 2 do iptables.

%package -n python3-%{module}
Summary:	Python 3 bindings for iptables
Summary(pl.UTF-8):	Wiązania Pythona 3 do iptables
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-%{module}
Python 3 bindings for iptables.

%description -n python3-%{module} -l pl.UTF-8
Wiązania Pythona 3 do iptables.

%package apidocs
Summary:	API documentation for Python iptables module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona iptables
Group:		Documentation

%description apidocs
API documentation for Python iptables module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona iptables.

%prep
%setup -q

%build
%if %{with python2}
CC="%{__cc}" \
CFLAGS="%{rpmcppflags} %{rpmcflags}" \
%py_build
%endif

%if %{with python3}
CC="%{__cc}" \
CFLAGS="%{rpmcppflags} %{rpmcflags}" \
%py3_build
%endif

%if %{with doc}
cd doc
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%dir %{py_sitedir}/iptc
%{py_sitedir}/iptc/*.py[co]
%attr(755,root,root) %{py_sitedir}/libxtwrapper.so
%{py_sitedir}/python_iptables-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.md
%dir %{py3_sitedir}/iptc
%{py3_sitedir}/iptc/__pycache__
%{py3_sitedir}/iptc/*.py
%attr(755,root,root) %{py3_sitedir}/libxtwrapper.cpython-*.so
%{py3_sitedir}/python_iptables-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/*
%endif
