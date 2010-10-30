%define tarname	ViTables
%define name	vitables
%define version 2.0
%define release %mkrel 3

Summary:	Graphical tool for browsing and editing HDF5 files
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{tarname}-%{version}.tar.lzma
License:	GPLv3+ 
Group:		Editors
Url:		http://vitables.org
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-tables >= 2.0, python-qt4 >= 4.3
BuildRequires:	python-tables >= 2.0, python-qt4 >= 4.3
%py_requires -d

%description
ViTables is a graphical tool for browsing and editing files in both PyTables
and HDF5 format. With ViTables you can easily navigate through the data
hierarchy, view and modify metadata, view actual data and more.

%prep
%setup -q -n %{tarname}-%{version}

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}
%__rm -rf %{buildroot}/%{py_sitedir}/%{name}/examples
%__rm -rf %{buildroot}/%{py_sitedir}/%{name}/doc

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ANNOUNCE.txt ChangeLog.txt LICENSE.txt README.txt TODO.txt doc/*.pdf examples/
%_bindir/*
%py_sitedir/*
