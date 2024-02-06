# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-pylev
Epoch: 100
Version: 1.4.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Python Levenshtein implementation that's not freaking GPL'd
License: BSD-3-Clause
URL: https://github.com/toastdriven/pylev/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Based off the Wikipedia code samples at
http://en.wikipedia.org/wiki/Levenshtein_distance.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pylev
Summary: Python Levenshtein implementation that's not freaking GPL'd
Requires: python3
Provides: python3-pylev = %{epoch}:%{version}-%{release}
Provides: python3dist(pylev) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pylev = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pylev) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pylev = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pylev) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pylev
Based off the Wikipedia code samples at
http://en.wikipedia.org/wiki/Levenshtein_distance.

%files -n python%{python3_version_nodots}-pylev
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-pylev
Summary: Python Levenshtein implementation that's not freaking GPL'd
Requires: python3
Provides: python3-pylev = %{epoch}:%{version}-%{release}
Provides: python3dist(pylev) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pylev = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pylev) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pylev = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pylev) = %{epoch}:%{version}-%{release}

%description -n python3-pylev
Based off the Wikipedia code samples at
http://en.wikipedia.org/wiki/Levenshtein_distance.

%files -n python3-pylev
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
