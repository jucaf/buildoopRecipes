# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
%define lib_tomcat_server %{_usr}/lib/tomcatserver

%if  %{?suse_version:1}0
  %define doc_tomcat_server %{_docdir}/tomcatserver
%else
  %define doc_tomcat_server %{_docdir}/tomcatserver-%{version}
%endif
%define tomcat_server_version 6.0.36
%define tomcat_server_base_version 6.0.36
%define tomcat_server_release openbus_1.1.0

Name: tomcat-server
Version: %{tomcat_server_version}
Release: %{tomcat_server_release}
Summary: Apache Tomcat
URL: http://tomcat.apache.org/
Vendor: The Redoop Team
Group: Development/Libraries
BuildArch: noarch
Buildroot: %(mktemp -ud %{_tmppath}/tomcatserver-%{version}-%{release}-XXXXXX)
License: ASL 2.0 
Source0: apache-tomcat-%{tomcat_server_base_version}-src.tar.gz
Source1: rpm-build-stage
Source2: install_tomcat-server.sh

%description 
Apache Tomcat is an open source software implementation of the
Java Servlet and JavaServer Pages technologies.

%prep
%setup -n apache-tomcat-%{tomcat_server_base_version}-src

%build
bash %{SOURCE1}

%install
%__rm -rf $RPM_BUILD_ROOT
bash %{SOURCE2} \
          --build-dir=build \
	  --doc-dir=%{doc_tomcat_server} \
          --prefix=$RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%attr(0755,root,root) %{lib_tomcat_server}
%doc %{doc_tomcat_server}

%changelog

