Summary:	A set of python modules for machine learning and data mining
Name:		python-scikit-learn
Version:	1.3.2
Release:	1
License:	new BSD
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/s/scikit-learn/scikit-learn-%{version}.tar.gz
URL:		https://pypi.org/project/scikit-learn/
BuildRequires:	python%{pyver}dist(pip)

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

