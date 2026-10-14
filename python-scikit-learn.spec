%define module scikit-learn
%define oname scikit_learn

Name:		python-scikit-learn
Summary:	A set of python modules for machine learning and data mining
Version:	1.9.0
Release:	2
License:	BSD-3-Clause
Group:		Development/Python
URL:		https://scikit-learn.org/
Source0:	https://github.com/scikit-learn/scikit-learn/archive/%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(meson-python)
BuildRequires:	python%{pyver}dist(narwhals)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(scipy)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(threadpoolctl)
BuildRequires:	python%{pyver}dist(wheel)

%description
A set of python modules for machine learning and data mining

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%files
%{python_sitearch}/sklearn
%{python_sitearch}/%{oname}-%{version}.dist-info
