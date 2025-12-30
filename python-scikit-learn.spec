Summary:	A set of python modules for machine learning and data mining
Name:		python-scikit-learn
Version:	1.4.1.post1
Release:	3
License:	new BSD
Group:		Development/Python
URL:		https://pypi.org/project/scikit-learn/
Source0:	https://pypi.org/packages/source/s/scikit-learn/scikit-learn-%{version}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(scipy)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
A set of python modules for machine learning and data mining

%files
%{py_platsitedir}/sklearn
%{py_platsitedir}/scikit_learn-*.*-info

#----------------------------------------------------------------------

%prep
%autosetup -p1 -n scikit-learn-%{version}

%build
%py_build

%install
%py_install

