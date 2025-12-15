Name:		python-accessible-pygments
Version:	0.0.5
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/a/accessible_pygments/accessible_pygments-%{version}.tar.gz
Summary:	A collection of accessible pygments styles
URL:		https://pypi.org/project/accessible-pygments/
License:	BSD-3-Clause
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-fancy-pypi-readme)

%description
A collection of accessible pygments styles

%files
%{py_sitedir}/a11y_pygments
%{py_sitedir}/accessible_pygments-*.*-info
