#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-admisc
Version  : 0.29
Release  : 10
URL      : https://cran.r-project.org/src/contrib/admisc_0.29.tar.gz
Source0  : https://cran.r-project.org/src/contrib/admisc_0.29.tar.gz
Summary  : Adrian Dusa's Miscellaneous
Group    : Development/Tools
License  : GPL-3.0
Requires: R-admisc-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
Interprets and translates, factorizes and negates SOP - Sum of Products
    expressions, for both binary and multi-value crisp sets, and extracts
    information (set names, set values) from those expressions. Other functions
    perform various other checks if possibly numeric (even if all numbers reside
    in a character vector) and coerce to numeric, or check if the numbers are
    whole. It also offers, among many others, a highly versatile recoding
    routine and a more flexible alternative to the base function 'with()'.
    Some of the functions in this package use related functions from package
    'QCA'. Users are encouraged to install that package despite not being listed
    in the Imports field, due to circular dependency issues.

%package lib
Summary: lib components for the R-admisc package.
Group: Libraries

%description lib
lib components for the R-admisc package.


%prep
%setup -q -c -n admisc
cd %{_builddir}/admisc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1655748488

%install
export SOURCE_DATE_EPOCH=1655748488
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library admisc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library admisc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library admisc
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc admisc || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/admisc/ChangeLog
/usr/lib64/R/library/admisc/DESCRIPTION
/usr/lib64/R/library/admisc/INDEX
/usr/lib64/R/library/admisc/Meta/Rd.rds
/usr/lib64/R/library/admisc/Meta/features.rds
/usr/lib64/R/library/admisc/Meta/hsearch.rds
/usr/lib64/R/library/admisc/Meta/links.rds
/usr/lib64/R/library/admisc/Meta/nsInfo.rds
/usr/lib64/R/library/admisc/Meta/package.rds
/usr/lib64/R/library/admisc/NAMESPACE
/usr/lib64/R/library/admisc/R/admisc
/usr/lib64/R/library/admisc/R/admisc.rdb
/usr/lib64/R/library/admisc/R/admisc.rdx
/usr/lib64/R/library/admisc/help/AnIndex
/usr/lib64/R/library/admisc/help/admisc.rdb
/usr/lib64/R/library/admisc/help/admisc.rdx
/usr/lib64/R/library/admisc/help/aliases.rds
/usr/lib64/R/library/admisc/help/paths.rds
/usr/lib64/R/library/admisc/html/00Index.html
/usr/lib64/R/library/admisc/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/admisc/libs/admisc.so
/usr/lib64/R/library/admisc/libs/admisc.so.avx2
/usr/lib64/R/library/admisc/libs/admisc.so.avx512
