%define origname	nltk_lite

Summary:		Natural Language Toolkit for Python
Name:			python-%{origname}
Version:		0.6.5
Release:		%mkrel 2
Epoch:			0
Group:			Development/Python
Url:			http://nltk.sourceforge.net/
Source0:		http://download.sourceforge.net/nltk/nltk_lite-%{version}.tar.bz2
Source1:		http://download.sourceforge.net/nltk/nltk_lite-corpora-%{version}.tar.bz2
Source2:		http://download.sourceforge.net/nltk/nltk_lite-doc-%{version}.tar.bz2
License:		CPL
BuildRoot:		%{_tmppath}/%{name}-buildroot
BuildArch:		noarch
BuildRequires:		epydoc
BuildRequires:          python-devel

%description
The Natural Langauge Toolkit is a Python package that simplifies the 
construction of programs that process natural language and defines 
standard interfaces between the different components of an NLP system. 



%prep
%setup -q -n %{origname}-%{version}
%setup -q -T -D -a 1 -n %{origname}-%{version}
%setup -q -T -D -a 2 -n %{origname}-%{version}

%build
%{__python} setup.py build
pushd doc
%make
popd

%install
%{__rm} -rf %{buildroot}

%{__python} setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
%{__rm} -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc corpora doc

