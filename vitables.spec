%define tarname	ViTables
%define name	vitables
%define version 2.2a1
%define release 1 

Summary:	Graphical tool for browsing and editing HDF5 files
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.gz
License:	GPLv3+ 
Group:		Editors
Url:		http://vitables.org
BuildArch:	noarch
Requires:	python-tables >= 2.0, python-qt4 >= 4.3
BuildRequires:	python-tables >= 2.0, python-qt4 >= 4.3
BuildRequires:	python-sphinx
BuildRequires:	python3-devel
BuildRequires:	python-setuptools

%description
ViTables is a graphical tool for browsing and editing files in both PyTables
and HDF5 format. With ViTables you can easily navigate through the data
hierarchy, view and modify metadata, view actual data and more.

%prep
%setup -q -n %{tarname}-%{version}

%install
echo %{version} > VERSION
%__python setup.py install --root=%{buildroot}
%__rm -rf %{buildroot}/%{py_sitedir}/%{name}/examples
%__rm -rf %{buildroot}/%{py_sitedir}/%{name}/doc
find %{buildroot} -name "*.py" -exec chmod 755 {} \;

%files
%doc README.txt
%_bindir/*
%py_sitedir/*

