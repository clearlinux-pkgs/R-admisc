#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v19
# autospec commit: f35655a
#
Name     : R-admisc
Version  : 0.36
Release  : 25
URL      : https://cran.r-project.org/src/contrib/admisc_0.36.tar.gz
Source0  : https://cran.r-project.org/src/contrib/admisc_0.36.tar.gz
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
    routine and some more flexible alternatives to the base functions 'with()'
    and 'within()'.
    SOP simplification functions in this package use related minimization from
    package 'QCA', which is recommended to be installed despite not being listed
    in the Imports field, due to circular dependency issues.

%package lib
Summary: lib components for the R-admisc package.
Group: Libraries

%description lib
lib components for the R-admisc package.


%prep
%setup -q -n admisc
pushd ..
cp -a admisc buildavx2
popd
pushd ..
cp -a admisc buildavx512
popd
pushd ..
cp -a admisc buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726150482

%install
export SOURCE_DATE_EPOCH=1726150482
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/V3/usr/lib64/R/library/admisc/libs/admisc.so
/V4/usr/lib64/R/library/admisc/libs/admisc.so
/VA/usr/lib64/R/library/admisc/libs/admisc.so
/usr/lib64/R/library/admisc/libs/admisc.so
