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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-tables >= 2.0, python-qt4 >= 4.3
BuildRequires:	python-tables >= 2.0, python-qt4 >= 4.3
BuildRequires:	python-sphinx
BuildRequires:	python3-devel

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


%changelog
* Wed Aug 08 2012 Lev Givon <lev@mandriva.org> 2.1-1
+ Revision: 812887
- Update to 2.1.

* Sat Oct 30 2010 Michael Scherer <misc@mandriva.org> 2.0-3mdv2011.0
+ Revision: 590586
- rebuild for python 2.7

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 2.0-2mdv2010.0
+ Revision: 445696
- rebuild

* Tue Jan 20 2009 Lev Givon <lev@mandriva.org> 2.0-1mdv2009.1
+ Revision: 332059
- import vitables


