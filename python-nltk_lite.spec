%bcond_with     doc
%define origname nltk_lite

Name:           python-%{origname}
Version:        0.7.5
Release:        %mkrel 4
Epoch:          0
Summary:        Natural Language Toolkit for Python
License:        CPL
Group:          Development/Python
URL:            http://nltk.sourceforge.net/
Source0:        http://ovh.dl.sourceforge.net/nltk/nltk_lite-%{version}.tar.gz
Source1:        http://ovh.dl.sourceforge.net/nltk/nltk_lite-corpora-%{version}.zip
Source2:        http://ovh.dl.sourceforge.net/nltk/nltk_lite-doc-%{version}.zip
Source3:        http://ovh.dl.sourceforge.net/nltk/nltk_lite-examples-%{version}.zip
Requires:       python-yaml
%if %with doc
BuildRequires:  epydoc
%endif
%py_requires -d
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The Natural Langauge Toolkit is a Python package that simplifies the 
construction of programs that process natural language and defines 
standard interfaces between the different components of an NLP system. 

%prep
%setup -q -n %{origname}-%{version}
%setup -q -T -D -a 1 -n %{origname}-%{version}
%setup -q -T -D -a 2 -n %{origname}-%{version}
%setup -q -T -D -a 3 -n %{origname}-%{version}
%{__chmod} -Rf a+rX,u+w,g-w,o-w .
%{_bindir}/find . -name '.DS_Store' -o -name '.api.done' -o -name '.png' | %{_bindir}/xargs %{__rm} -r

%build
%{__python} setup.py build
%if %with doc
pushd doc
%{__make}
popd
%endif

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O2 --root=%{buildroot} --record=INSTALLED_FILES
%{__mkdir_p} %{buildroot}%{_datadir}/nltk_lite
%{__cp} -a corpora doc examples %{buildroot}%{_datadir}/nltk_lite
%{_bindir}/find %{buildroot} -type f -name '*.txt' | %{_bindir}/xargs %{__perl} -pi -e 's|\r$||g'

%{__chmod} 755 %{buildroot}%{_datadir}/nltk_lite/doc/examples.py \
               %{buildroot}%{_datadir}/nltk_lite/doc/pages.py \
               %{buildroot}%{py_puresitedir}/nltk_lite/corpora/toolbox.py \
               %{buildroot}%{py_puresitedir}/nltk_lite/misc/nemo.py \
               %{buildroot}%{py_puresitedir}/nltk_lite/contrib/toolbox/settings.py \
               %{buildroot}%{py_puresitedir}/nltk_lite/contrib/toolbox/language.py \
               %{buildroot}%{py_puresitedir}/nltk_lite/test/doctest_driver.py \
               %{buildroot}%{py_puresitedir}/nltk_lite/contrib/toolbox/data.py \
               %{buildroot}%{py_puresitedir}/nltk_lite/stem/porter.py \
               %{buildroot}%{_datadir}/nltk_lite/doc/tree2image.py

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc *.txt
%defattr(-,root,root,0755)
%{py_puresitedir}/nltk_lite*
%exclude %{py_puresitedir}/yaml
%{_datadir}/nltk_lite
