Name:           {{PACKAGE_NAME}}
Version:        {{VERSION}}
Release:        {{RELEASE}}%{?dist}
Summary:        {{SUMMARY}}
License:        {{SPDX_LICENSE}}
URL:            {{HOMEPAGE_URL}}
Source0:        {{SOURCE_URL}}

BuildRequires:  {{BUILD_DEPENDENCIES}}
Requires:       {{RUNTIME_DEPENDENCIES}}

%description
{{DESCRIPTION}}

%prep
%autosetup -n %{name}-%{version}

%build
{{BUILD_COMMAND}}

%install
rm -rf %{buildroot}
{{INSTALL_COMMAND}}

%check
{{TEST_COMMAND}}

%files
%license LICENSE
%doc README.md
{{PACKAGE_FILE_LIST}}

%changelog
* {{RPM_CHANGELOG_DATE}} {{MAINTAINER_NAME}} <{{MAINTAINER_EMAIL}}> - {{VERSION}}-{{RELEASE}}
- {{CHANGELOG_ENTRY}}
