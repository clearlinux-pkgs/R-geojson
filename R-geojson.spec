#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-geojson
Version  : 0.3.4
Release  : 30
URL      : https://cran.r-project.org/src/contrib/geojson_0.3.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/geojson_0.3.4.tar.gz
Summary  : Classes for 'GeoJSON'
Group    : Development/Tools
License  : MIT
Requires: R-jqr
Requires: R-jsonlite
Requires: R-lazyeval
Requires: R-magrittr
Requires: R-protolite
Requires: R-sp
BuildRequires : R-jqr
BuildRequires : R-jsonlite
BuildRequires : R-lazyeval
BuildRequires : R-magrittr
BuildRequires : R-protolite
BuildRequires : R-sp
BuildRequires : buildreq-R

%description
Includes S3 classes for 'GeoJSON' classes with brief summary output,
    and a few methods such as extracting and adding bounding boxes,
    properties, and coordinate reference systems; working with 
    newline delimited 'GeoJSON'; linting through the 'geojsonlint' 
    package; and serializing to/from 'Geobuf' binary 'GeoJSON' 
    format.

%prep
%setup -q -c -n geojson
cd %{_builddir}/geojson

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592950342

%install
export SOURCE_DATE_EPOCH=1592950342
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library geojson
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library geojson
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library geojson
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/geojson/DESCRIPTION
/usr/lib64/R/library/geojson/INDEX
/usr/lib64/R/library/geojson/LICENSE
/usr/lib64/R/library/geojson/Meta/Rd.rds
/usr/lib64/R/library/geojson/Meta/data.rds
/usr/lib64/R/library/geojson/Meta/features.rds
/usr/lib64/R/library/geojson/Meta/hsearch.rds
/usr/lib64/R/library/geojson/Meta/links.rds
/usr/lib64/R/library/geojson/Meta/nsInfo.rds
/usr/lib64/R/library/geojson/Meta/package.rds
/usr/lib64/R/library/geojson/Meta/vignette.rds
/usr/lib64/R/library/geojson/NAMESPACE
/usr/lib64/R/library/geojson/NEWS.md
/usr/lib64/R/library/geojson/R/geojson
/usr/lib64/R/library/geojson/R/geojson.rdb
/usr/lib64/R/library/geojson/R/geojson.rdx
/usr/lib64/R/library/geojson/data/Rdata.rdb
/usr/lib64/R/library/geojson/data/Rdata.rds
/usr/lib64/R/library/geojson/data/Rdata.rdx
/usr/lib64/R/library/geojson/doc/geojson-operations.R
/usr/lib64/R/library/geojson/doc/geojson-operations.Rmd
/usr/lib64/R/library/geojson/doc/geojson-operations.html
/usr/lib64/R/library/geojson/doc/geojson.R
/usr/lib64/R/library/geojson/doc/geojson.Rmd
/usr/lib64/R/library/geojson/doc/geojson.html
/usr/lib64/R/library/geojson/doc/index.html
/usr/lib64/R/library/geojson/examples/featurecollection1.geojson
/usr/lib64/R/library/geojson/examples/featurecollection2.geojson
/usr/lib64/R/library/geojson/examples/featurecollection3.geojson
/usr/lib64/R/library/geojson/examples/geometrycollection1.geojson
/usr/lib64/R/library/geojson/examples/linestring_one.geojson
/usr/lib64/R/library/geojson/examples/multilinestring_one.geojson
/usr/lib64/R/library/geojson/examples/ndgeojson1.json
/usr/lib64/R/library/geojson/examples/ndgeojson2.json
/usr/lib64/R/library/geojson/examples/ndgeojson3.json
/usr/lib64/R/library/geojson/examples/test.pb
/usr/lib64/R/library/geojson/examples/zillow_or.geojson
/usr/lib64/R/library/geojson/help/AnIndex
/usr/lib64/R/library/geojson/help/aliases.rds
/usr/lib64/R/library/geojson/help/geojson.rdb
/usr/lib64/R/library/geojson/help/geojson.rdx
/usr/lib64/R/library/geojson/help/paths.rds
/usr/lib64/R/library/geojson/html/00Index.html
/usr/lib64/R/library/geojson/html/R.css
/usr/lib64/R/library/geojson/img/one.png
/usr/lib64/R/library/geojson/img/two.png
/usr/lib64/R/library/geojson/tests/test-all.R
/usr/lib64/R/library/geojson/tests/testthat/feature.rds
/usr/lib64/R/library/geojson/tests/testthat/helper-geojson.R
/usr/lib64/R/library/geojson/tests/testthat/linestring.rds
/usr/lib64/R/library/geojson/tests/testthat/linestring_one.rds
/usr/lib64/R/library/geojson/tests/testthat/multilinestring.rds
/usr/lib64/R/library/geojson/tests/testthat/multipoint.rds
/usr/lib64/R/library/geojson/tests/testthat/multipolygon.rds
/usr/lib64/R/library/geojson/tests/testthat/point.rds
/usr/lib64/R/library/geojson/tests/testthat/polygon.rds
/usr/lib64/R/library/geojson/tests/testthat/test-as.geojson.R
/usr/lib64/R/library/geojson/tests/testthat/test-bbox.R
/usr/lib64/R/library/geojson/tests/testthat/test-crs.R
/usr/lib64/R/library/geojson/tests/testthat/test-feature.R
/usr/lib64/R/library/geojson/tests/testthat/test-featurecollection.R
/usr/lib64/R/library/geojson/tests/testthat/test-geo_bbox.R
/usr/lib64/R/library/geojson/tests/testthat/test-geo_pretty.R
/usr/lib64/R/library/geojson/tests/testthat/test-geo_type.R
/usr/lib64/R/library/geojson/tests/testthat/test-geo_write.R
/usr/lib64/R/library/geojson/tests/testthat/test-geobuf.R
/usr/lib64/R/library/geojson/tests/testthat/test-geometrycollection.R
/usr/lib64/R/library/geojson/tests/testthat/test-is.methods.R
/usr/lib64/R/library/geojson/tests/testthat/test-linestring.R
/usr/lib64/R/library/geojson/tests/testthat/test-multilinestring.R
/usr/lib64/R/library/geojson/tests/testthat/test-multipoint.R
/usr/lib64/R/library/geojson/tests/testthat/test-multipolygon.R
/usr/lib64/R/library/geojson/tests/testthat/test-ndgeo.R
/usr/lib64/R/library/geojson/tests/testthat/test-point.R
/usr/lib64/R/library/geojson/tests/testthat/test-polygon.R
/usr/lib64/R/library/geojson/tests/testthat/test-properties.R
/usr/lib64/R/library/geojson/tests/testthat/test-stream_in_geojson.R
/usr/lib64/R/library/geojson/tests/testthat/test-tibbles.R
/usr/lib64/R/library/geojson/tests/testthat/test-to_geojson.R
/usr/lib64/R/library/geojson/tests/testthat/test.rds
