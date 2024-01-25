%if 0%{?rhel} == 8
%define anaconda_core_version 33
%endif
%if 0%{?rhel} == 9
%define anaconda_core_version 34
%endif
%if 0%{?fedora}
%define anaconda_core_version %{fedora}
%endif

Name:           oscap-anaconda-addon
Version:        2.0.0
Release:        17%{?dist}
Summary:        Anaconda addon integrating OpenSCAP to the installation process

License:        GPLv2+
URL:            https://github.com/OpenSCAP/oscap-anaconda-addon

Source0:        https://github.com/OpenSCAP/oscap-anaconda-addon/releases/download/r%{version}/%{name}-%{version}.tar.gz
# TODO: Remove when the fixed upstream release contains dbus service data
Source1:        addon-dbus-data.zip

Patch1: 	lang.patch
Patch2: 	oscap-anaconda-addon-2.0.1-various_bugfixes-PR_166.patch
Patch3: 	oscap-anaconda-addon-2.0.1-fix_archive_handling-PR_170.patch
Patch4: 	oscap-anaconda-addon-2.0.1-fix_no_hardening-PR_176.patch
Patch5: 	oscap-anaconda-addon-2.0.1-fix_fingerprint-PR_177.patch
Patch6: 	oscap-anaconda-addon-2.0.1-rhel9_tailoring_fix-PR_180.patch
Patch7: 	oscap-anaconda-addon-1.2.2-dbus_show_integration-PR_182.patch
Patch8: 	oscap-anaconda-addon-2.1.0-unified_help-PR_192.patch
Patch9: 	oscap-anaconda-addon-2.0.1-absent_appstream-PR_185.patch
Patch10: 	oscap-anaconda-addon-2.0.1-fix_strings-PR_207.patch
Patch11: 	oscap-anaconda-addon-2.1.0-clicking_fix-PR_223.patch
Patch12: 	oscap-anaconda-addon-2.1.0-archive_handling-PR_224.patch
Patch13: 	oscap-anaconda-addon-2.1.0-content_paths-PR_227.patch
Patch14: 	oscap-anaconda-addon-null-http_only_uri-PR_233.patch
Patch15: 	oscap-anaconda-addon-2.0.1-tar-extraction-PR_250.patch
Patch16: 	oscap-anaconda-addon-2.0.1-package-groups-PR_248.patch

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  gettext
BuildRequires:  python3-devel
BuildRequires:  python3-pycurl
BuildRequires:  openscap openscap-utils openscap-python3
BuildRequires:  anaconda-core >= %{anaconda_core_version}
Requires:       anaconda-core >= %{anaconda_core_version}
Requires:       python3-pycurl
Requires:       python3-kickstart
Requires:       openscap openscap-utils openscap-python3
Requires:       scap-security-guide

%description
This is an addon that integrates OpenSCAP utilities with the Anaconda installer
and allows installation of systems following restrictions given by a SCAP
content.

%prep
%autosetup -p1
unzip %{_sourcedir}/addon-dbus-data.zip

%build

%check

%install
make install DESTDIR=%{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%{_datadir}/anaconda/addons/org_fedora_oscap
%{_datadir}/anaconda/dbus/confs/org.fedoraproject.Anaconda.Addons.OSCAP.conf
%{_datadir}/anaconda/dbus/services/org.fedoraproject.Anaconda.Addons.OSCAP.service

%doc COPYING ChangeLog README.md

%changelog
* Wed Jul 19 2023 Jan Černý <jcerny@redhat.com> - 2.0.0-17
- Update translations (rhbz#2189526)
- Fix tar file extraction (rhbz#2218875)
- Fix conflict of tftp package with "network servers" group (rhbz#2172264)

* Wed Feb 08 2023 Matej Tyc <matyc@redhat.com> - 2.0.0-16
- Update translations
  Resolves: rhbz#2139667
  Resolves: rhbz#2150877

* Mon Jan 23 2023 Matej Tyc <matyc@redhat.com> - 2.0.0-15
- Fix a reaction to invalid content URI
  Resolves: rhbz#2148508

* Fri Nov 25 2022 Matej Tyc <matyc@redhat.com> - 2.0.0-14
- Fix regression introduced when fixing content archive input
  Resolves: rhbz#2129008

* Fri Nov 11 2022 Matej Tyc <matyc@redhat.com> - 2.0.0-13
- Fix problems with handling multi-datastream archives
  Resolves: rhbz#2129846
- Fix a crash when compulsively clicking in the GUI
  Resolves: rhbz#2127502

* Fri Jun 10 2022 Matej Tyc <matyc@redhat.com> - 2.0.0-12
- Remove the firstboot remediation feature completely.
  We can't have it, while maintaining the standard UX.
  Resolves: rhbz#2065751

* Wed Jun 01 2022 Matej Tyc <matyc@redhat.com> - 2.0.0-11
- Remove the redundant dependency on oscap-utils
  Resolves: rhbz#2086822

* Wed May 18 2022 Matej Tyc <matyc@redhat.com> - 2.0.0-10
- Fix strings, so they are translatable, and update translations
  Resolves: rhbz#2081268

* Mon Mar 21 2022 Matej Tyc <matyc@redhat.com> - 2.0.0-9
- Introduce the firstboot remediation
  Resolves: rhbz#1999587
- Add better error handling of installation using unsupported installation sources
  Resolves: rhbz#2042334

* Mon Jan 24 2022 Matej Tyc <matyc@redhat.com> - 2.0.0-8
- Introduce unified help support
  Resolves: rhbz#2043512
- Update translations
  Resolves: rhbz#2017374

* Mon Dec 13 2021 Matej Tyc <matyc@redhat.com> - 2.0.0-7
- Don't show the OSCAP spoke if the OSCAP DBus module is disabled
  Resolves: rhbz#2018954

* Thu Nov 25 2021 Matej Tyc <matyc@redhat.com> - 2.0.0-6
- Fix handling of tailoring in RHEL9
  Resolves: rhbz#1996129

* Wed Nov 10 2021 Matej Tyc <matyc@redhat.com> - 2.0.0-5
- Fix handling of content archives
  Resolves: rhbz#1996129
- Fix handling of content fingerprint
  Resolves: rhbz#1993065
- Fix crash when a previously selected hardening has been cancelled
  Resolves: rhbz#2014108
- Pull latest translations

* Fri Aug 20 2021 Matej Tyc <matyc@redhat.com> - 2.0.0-4
- Update translations
  Resolves: rhbz#1962112

* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 2.0.0-3
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Tue Aug 03 2021 Matej Tyc <matyc@redhat.com> - 2.0.0-2
- Fix issues with locally installed content and labelling of discovered content.
- Resolves: rhbz#1989434

* Fri Jul 02 2021 Matej Tyc <matyc@redhat.com> - 2.0.0-1
- Rebase to the 2.0.0 upstream release.
- Remove the cpio dependency which is not needed any more.

* Wed Jun 23 2021 Jan Černý <jcerny@redhat.com> - 1.0-11
- Rebuild after test config change in test.yml

* Mon Jun 14 2021 Matej Tyc <matyc@redhat.com> - 1.0-10
- Unified the spec file with the Fedora one.
- Removed unwanted dependencies.
- nose is not needed for a long time.
- mock has been moved into the Python standard library, so it is also not needed.

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.0-9
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Matěj Týč <matyc@redhat.com> - 1.0-5
- Disabled execution of tests, as they are not meant to be executed in the build environment.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Matěj Týč <matyc@redhat.com> - 1.0-1
- Rebased to upstream version 1.0
- Python3 support, anaconda 28 support.

* Fri Feb 09 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.7-7
- Escape macros in %%changelog

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jan 07 2015 Vratislav Podzimek <vpodzime@redhat.com> - 0.7-1
- Adapt to changes in Anaconda
- Define name of the spoke window
- Set fetching flag to False when extraction error happens
- Remove code that was pushed to the anaconda's sources

* Fri Feb 28 2014 Vratislav Podzimek <vpodzime@redhat.com> - 0.6-2
- Rebuild with building issues fixed

* Fri Feb 28 2014 Vratislav Podzimek <vpodzime@redhat.com> - 0.6-1
- Getting status needs to run in the main thread
- Grab focus for the URL entry after switching notebook page
- Clear rule data when unselecting profile
- Update message as part of the initialization
- Add BuildRequires: gettext
- Include translations in the tarball and RPM

* Fri Feb 28 2014 Vratislav Podzimek <vpodzime@redhat.com> - 0.5-1
- Allow users to change content
- Show and hide control buttons properly
- Fix sensitivity of the URL entry and fetch button
- Add the button allowing users to use SSG content if available
- Fix listing python sources when creating potfile and regenerate it
- Omit the %%addon section from kickstart in dry-run mode
- Implement the dry-run mode in the GUI (trac#2)
- Add UI elements for content changing and dry-run mode
- Check content_defined instead of content_url in the GUI code
- First select the profile, then update the message store
- Remove unused import
- Ignore some more temporary/backup files
- If no content is specified and SSG is available, use it
- New special content type -- SCAP Security Guide
- Fix name of the property used when doing fingerprint check
- Get rid of an unused variable
- Fix data fetch locking to work properly with kickstart installations
- Use 'anonymous:' if no username and password is given for FTP
- Initial version of the translations template file
- First steps to dry-run mode
- Fix main notebook tabs
- Make translations work
- Manipulation with the i18n related files
- If no profile is given, default to default
- Ignore updates.img and its auxiliary directory
- Catch only fetching errors from the fetching thread
- Do not allow multiple simultaneous fetches/initializations
- Prevent user from changing the URL while we try to fetch from it
- Add support for the Default profile
- Support FTP as a content source (#1050980)
- React properly on archive extraction failure
- Refactor the code pre-processing the fetched content
- Unify exceptions from archive extraction
- Make pylint check mandatory to pass
- Support for hash based content integrity checking

* Tue Jan 14 2014 Vratislav Podzimek <vpodzime@redhat.com> - 0.4-1
- Beware of running Gtk actions from a non-main thread
- Fix path to the tailoring file when getting rules
- A git hook for running tests when pushing
- Inform user if no profile is selected
- Visually mark the selected profile
- Better UX with content URL entry and progress label
- React on invalid content properly (#1032846)
- Stop spinner when data fetching is finished
- Make the data fetching thread non-fatal (#1049989)
- Exit code 2 from the oscap tool is not an error for us (#1050913)
- Be ready to work with archives/RPMs containing data streams
- Add unit tests for the keep_type_map function
- Add support for namedtuples to keep_type_map
- Add target for running pylint check
- Add target for running just unittests
- On the way to tailoring
- Tests for kickstart XCCDF tailoring handling
- Kickstart support for XCCDF tailoring
- Check session validity also when using XCCDF benchmark

* Tue Dec 10 2013 Vratislav Podzimek <vpodzime@redhat.com> - 0.3-1
- Implement and use our own better function for joining paths
- The content entry should have focus if there is no content
- RPM is just a weird archive in the pre-installation phase
- Ignore RPM files as well
- Adapt tests to dir constants now ending with "/"
- CpioArchive cannot be created from a piped output
- Fix namespace definitions in the testing XCCDF file
- Prevent putting None into xccdf_session_is_sds
- Fix the __all__ variable in the common module
- Strip content dir prefix when setting xccdf/cpe paths
- Inform user we now support archive URLs as well
- Ignore various file types in the git repository
- Try to find content files in the fetched archive or RPM
- Run pylint -E as part of the test target
- Return list of extracted files/directories when extracting archive
- Do not try to search for empty file paths in archives
- Properly set the content type based on the URL's suffix
- Switch profiles on double-click
- Hook urlEntry's activate signal to fetchButton click
- Save the spoke's glade file with a new Glade
- The addon now requires the python-cpio package
- Use really_hide for the UI elements for datastream-id and xccdf-id
- Support for RPM content in the GUI spoke
- RPM content support for kickstart processing
- Add property for the raw post-installation content path
- Make content type case insensitive
- Rest of the code needed for RPM extraction
- Actually look for the file path in entry names
- Basic stuff needed for the RPM content support
- Run tests in paralel
- Specify files in a better way in spec

* Mon Oct 21 2013 Vratislav Podzimek <vpodzime@redhat.com> - 0.2-1
- Initial RPM for the oscap-anaconda-addon
