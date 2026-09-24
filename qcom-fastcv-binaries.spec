%global debug_package %{nil}

Name:           qcom-fastcv-binaries
Version:        1.8.9
Release:        2%{?dist}
Summary:        Qualcomm FastCV - DSP binaries and optimized CV library
License:        LicenseRef-Qualcomm-nologin-binaries
URL:            https://www.qualcomm.com/developer/software/qualcomm-fastcv-sdk
Source0:        https://qartifactory-edge.qualcomm.com/artifactory/qsc_releases/software/chip/component/computervision-fastcv.qclinux.0.1/260805/prebuilt_trixie/qcom-fastcv-binaries_1.8.9_arm64.tar.gz

ExclusiveArch:  aarch64

%description
Qualcomm FastCV offers an optimized computer vision (CV) library
which frequently used vision processing functions and is designed
to take advantage of Hexagon DSPs.

This package contains binaries for Hexagon DSPs.

%package -n libfastcvopt1
Summary:        Qualcomm FastCV - shared libraries
Requires:       glib2
Requires:       fastrpc

%description -n libfastcvopt1
Qualcomm FastCV offers an optimized computer vision (CV) library
which frequently used vision processing functions and is designed
to take advantage of Hexagon DSPs.

This package contains shared libraries for the host system.

%package -n libfastcvopt-devel
Summary:        Qualcomm FastCV - development files
Requires:       libfastcvopt1 = %{version}-%{release}

%description -n libfastcvopt-devel
Qualcomm FastCV offers an optimized computer vision (CV) library
which frequently used vision processing functions and is designed
to take advantage of Hexagon DSPs.

This package contains the development files.

%package utils
Summary:        Qualcomm FastCV - utilities
Requires:       libfastcvopt1 = %{version}-%{release}

%description utils
Qualcomm FastCV offers an optimized computer vision (CV) library
which frequently used vision processing functions and is designed
to take advantage of Hexagon DSPs.

This package contains a test utility.

%prep
%autosetup -p1 -n qcom-fastcv-binaries-%{version}

%build
# Prebuilt binaries — no compilation step required.

%install
# DSP binaries (qcom-fastcv-binaries)
install -d %{buildroot}%{_libdir}/dsp
cp -a qcom-fastcv-binaries1/arm64/usr/lib/dsp/. %{buildroot}%{_libdir}/dsp/

# Shared libraries (libfastcvopt1)
install -d %{buildroot}%{_libdir}
install -m 0755 qcom-fastcv-binaries1/arm64/usr/lib/aarch64-linux-gnu/libfastcvopt.so.1.8.0 %{buildroot}%{_libdir}/libfastcvopt.so.1.8.0
ln -s libfastcvopt.so.1.8.0 %{buildroot}%{_libdir}/libfastcvopt.so.1
install -m 0755 qcom-fastcv-binaries1/arm64/usr/lib/aarch64-linux-gnu/libfastcvdsp_stub.so.1.8.0 %{buildroot}%{_libdir}/libfastcvdsp_stub.so.1.8.0
ln -s libfastcvdsp_stub.so.1.8.0 %{buildroot}%{_libdir}/libfastcvdsp_stub.so.1

# Development headers and unversioned .so symlinks (libfastcvopt-devel)
install -d %{buildroot}%{_includedir}/fastcv
cp -a qcom-fastcv-binaries-dev/arm64/usr/include/fastcv/. %{buildroot}%{_includedir}/fastcv/
ln -s libfastcvopt.so.1.8.0 %{buildroot}%{_libdir}/libfastcvopt.so
ln -s libfastcvdsp_stub.so.1.8.0 %{buildroot}%{_libdir}/libfastcvdsp_stub.so
install -d %{buildroot}%{_libdir}/pkgconfig
cp -a qcom-fastcv-binaries-dev/arm64/usr/lib/aarch64-linux-gnu/pkgconfig/. %{buildroot}%{_libdir}/pkgconfig/

# Utility binary (qcom-fastcv-utils)
install -d %{buildroot}%{_bindir}
install -m 0755 qcom-fastcv-binaries1/arm64/usr/bin/fastcv_simple_test64 %{buildroot}%{_bindir}/fastcv_simple_test64

find %{buildroot} -name '*.la' -delete

%files
%license LICENSE.qcom-2
%{_libdir}/dsp/

%files -n libfastcvopt1
%license LICENSE.qcom-2
%{_libdir}/libfastcvopt.so.1
%{_libdir}/libfastcvopt.so.1.8.0
%{_libdir}/libfastcvdsp_stub.so.1
%{_libdir}/libfastcvdsp_stub.so.1.8.0

%files -n libfastcvopt-devel
%license LICENSE.qcom-2
%{_includedir}/fastcv/
%{_libdir}/libfastcvopt.so
%{_libdir}/libfastcvdsp_stub.so
%{_libdir}/pkgconfig/

%files utils
%license LICENSE.qcom-2
%{_bindir}/fastcv_simple_test64

%changelog
* Thu Sep 24 2026 Pulkit Singh Tak <ptak@qti.qualcomm.com> - 1.8.9-2
- Add rules to install License file .

* Wed Aug 13 2026 Pulkit Singh Tak <ptak@qti.qualcomm.com> - 1.8.9-1
- Initial RPM packaging of qcom-fastcv-binaries prebuilt libraries version 1.8.9
