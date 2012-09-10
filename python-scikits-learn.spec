%define module	scikit-learn
%define name	python-%{module}
%define version	0.12
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel 1
%else
%define	release	%rel
%endif

Summary:	Python modules for machine learning and data mining
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://scikit-learn.sourceforge.net/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	blas-devel
BuildRequires:	python-setuptools
BuildRequires:	python-numpy-devel >= 1.3
BuildRequires:	python-scipy >= 0.7
# BuildRequires:	python-nose >= 0.10, python-coverage
%py_requires -d

%description
scikit-learn is a Python module for machine learning built on top of SciPy.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

# Disable checks because of semaphore problem on Mandriva build cluster:
#%check
#pushd %{buildroot}%{py_platsitedir}/scikits
#nosetests
#popd

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS.rst README.rst examples/ 
%py_platsitedir/scikit_learn*
%py_platsitedir/sklearn*
