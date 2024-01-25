# Patch0 applies correctly but with mismatch and we dont't want backup file
%global _default_patch_flags --no-backup-if-mismatch

Name:                 oscap-anaconda-addon
Version:              1.2.1
Release:              12%{?dist}
Summary:              Anaconda addon integrating OpenSCAP to the installation process

License:              GPLv2+
URL:                  https://github.com/OpenSCAP/oscap-anaconda-addon

# This is a OpenELA maintained package which is specific to
# our distribution.
#
# The source is thus available only from within this SRPM
# or via direct git checkout:
# git clone https://github.com/OpenSCAP/oscap-anaconda-addon.git
Source0:              %{name}-%{version}.tar.gz

# Let the Patch1 be reserved for translations patches
Patch1:               lang.patch
Patch2:               oscap-anaconda-addon-1.2.2-content_ident-PR_167.patch
Patch3:               oscap-anaconda-addon-1.2.2-deep_archives-PR_168.patch
Patch4:               oscap-anaconda-addon-1.2.2-absent_appstream-PR_184.patch
Patch5:               oscap-anaconda-addon-1.3.0-better_archive_handling-PR_220.patch
Patch6:               oscap-anaconda-addon-1.3.0-clicking_nocrash-PR_221.patch
Patch7:               oscap-anaconda-addon-1.3.0-fix_content_paths-PR_225.patch
Patch8:               oscap-anaconda-addon-null-http_content_url-PR_232.patch

BuildArch:            noarch
BuildRequires:        make
BuildRequires:        gettext
BuildRequires:        python3-devel
BuildRequires:        python3-pycurl
BuildRequires:        openscap openscap-utils openscap-python3
BuildRequires:        anaconda-core >= 33
Requires:             anaconda-core >= 33
Requires:             python3-cpio
Requires:             python3-pycurl
Requires:             python3-kickstart
Requires:             openscap openscap-utils openscap-python3
Requires:             scap-security-guide

%description
This is an addon that integrates OpenSCAP utilities with the Anaconda installer
and allows installation of systems following restrictions given by a SCAP
content.

%prep
%setup -q -n %{name}-%{version}

# As patches may translates the strings that are updated by later patches,
# Patch1 needs to be aplied last.
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
# NOTE CONCERNING TRANSLATION PATCHES
# When preparing translation patches, don't consider that some languages are unsupported -
# we aim to include all applicable translation texts to the appropriate patch.
# This has consulted with ljanda@redhat.com, and we basically follow the existing practice of the Anaconda project we integrate into.

%build

#%check
#make test


%install
make install DESTDIR=%{buildroot}
%find_lang %{name}

%files -f %{name}.lang
%{_datadir}/anaconda/addons/org_fedora_oscap

%doc COPYING ChangeLog README.md

%changelog
* Wed Feb 08 2023 Matej Tyc <matyc@redhat.com> - 1.2.1-12
- Update translations
  Resolves: rhbz#2139743

* Mon Jan 23 2023 Matej Tyc <matyc@redhat.com> - 1.2.1-11
- Fix a reaction to invalid content URI
  Resolves: rhbz#2148509

* Wed Nov 23 2022 Matej Tyc <matyc@redhat.com> - 1.2.1-10
- Fix regression introduced when fixing content archive input
  Resolves: rhbz#2129008

* Thu Nov 10 2022 Matej Tyc <matyc@redhat.com> - 1.2.1-9
- Fix problems with handling multi-datastream archives
  Resolves: rhbz#2129008
- Fix a crash when compulsively clicking in the GUI
  Resolves: rhbz#2000998

* Wed Jul 20 2022 Matej Tyc <matyc@redhat.com> - 1.2.1-8
- Update translations
  Resolves: rhbz#2062707

* Fri Jun 10 2022 Matej Tyc <matyc@redhat.com> - 1.2.1-7
- Remove the firstboot remediation feature completely.
  We can't have it, while maintaining the standard UX.
  Resolves: rhbz#2063179

* Mon Mar 21 2022 Matej Tyc <matyc@redhat.com> - 1.2.1-6
- Introduce the firstboot remediation
  Resolves: rhbz#1834716
- Add better error handling of installation using unsupported installation sources
  Resolves: rhbz#2007981

* Fri Jan 21 2022 Matej Tyc <matyc@redhat.com> - 1.2.1-5
- Updated translations
  Resolves: rhbz#2017356

* Fri Aug 20 2021 Matej Tyc <matyc@redhat.com> - 1.2.1-4
- Updated translations
  Resolves: rhbz#1962007

* Mon Aug 09 2021 Matej Tyc <matyc@redhat.com> - 1.2.1-3
- Fix handling of archives with directories in GUI installs
- Resolves: rhbz#1691305

* Tue Aug 03 2021 Matej Tyc <matyc@redhat.com> - 1.2.1-2
- Refactor content identification
- Resolves: rhbz#1989441

* Fri Jul 30 2021 Matej Tyc <matyc@redhat.com> - 1.2.1-1
- Rebase to the new upstream version.
- Resolves: rhbz#1691305

* Fri Jul 16 2021 Matej Tyc <matyc@redhat.com> - 1.2.0-2
- Updated translations
- Resolves: rhbz#1938623

* Fri Jun 25 2021 Matej Tyc <matyc@redhat.com> - 1.2.0-1
- Rebase to the new upstream version.
- Resolves: rhbz#1691305

* Mon Feb 15 2021 Matej Tyc <matyc@redhat.com> - 1.1.1-7
- Updated translations.

* Wed Nov 11 11:46:56 CET 2020 Matej Tyc <matyc@redhat.com> - 1.1.1-6
- Improved handling of conflicts between packages removed vs software wanted to be installed - rhbz#1892310

* Tue Aug 18 2020 Matěj Týč <matyc@redhat.com> - 1.1.1-5
- Fixed issues with encountering filenames with weird encoding during scans - rhbz#1867960

* Thu Jul 09 2020 Matěj Týč <matyc@redhat.com> - 1.1.1-4
- Fixed spoke window text: RHBZ#1855041

* Fri Jun 26 2020 Matěj Týč <matyc@redhat.com> - 1.1.1-3
- Updated translations: RHBZ#1820557

* Mon Jun 22 2020 Matěj Týč <matyc@redhat.com> - 1.1.1-2
- Fixed issues addressing combination of profiles and GUI-based software selections: RHBZ#1843932, RHBZ#1787156
- Improved handling of languages, capitalization: RHBZ#1696278
- Updated translations: RHBZ#1820557

* Tue Jun 02 2020 Matěj Týč <matyc@redhat.com> - 1.1.1-1
- Rebase to upstream 1.1.1
- This OAA is compatible with the RHEL 8.3 Anaconda: RHBZ#1696278
- The UX has been improved: RHBZ#1781790

* Mon Sep 02 2019 Watson Sato <wsato@redhat.com> - 1.0-10
- Do not use capital letters for spoke title: RHBZ#1744185
- Updated translations

* Wed Feb 13 2019 Matěj Týč <matyc@redhat.com> - 1.0-9
- Updated translations: RHBZ#1645924

* Fri Feb 08 2019 Watson Yuuma Sato <wsato@redhat.com> - 1.0-8
- Fixed translation of spoke title: RHBZ#1673044

* Fri Jan 18 2019 Matěj Týč <matyc@redhat.com> - 1.0-7
- Fixed bootloader-related Anaconda API usage: RHBZ#1664036
- Fixed root password-related Anaconda API usage: RHBZ#1665551
- Fixed checksum-related Python2->3 issue: RHBZ#1665147

* Thu Jan 17 2019 Matěj Týč <matyc@redhat.com> - 1.0-6
- Updated translations: RHBZ#1645924

* Mon Dec 17 2018 Matěj Týč <matyc@redhat.com> - 1.0-5
- Applied the HelpFile -> help_id patch

* Fri Dec 14 2018 Matěj Týč <matyc@redhat.com> - 1.0-4
- Updated translations: RHBZ#1608331, RHBZ#1645924

* Wed Oct 10 2018 Matěj Týč <matyc@redhat.com> - 1.0-3
- Updated to the latest Anaconda API: RHBZ#1637635
- Added updated translations: RHBZ#1608331

* Mon Oct 01 2018 Matěj Týč <matyc@redhat.com> - 1.0-2
- Added the missing pycurl dependency.

* Tue Jul 03 2018 Matěj Týč <matyc@redhat.com> - 1.0-1
- Rebased to upstream version 1.0
- Python3 support, anaconda 28 support.

* Tue Dec 12 2017 Watson Yuuma Sato <wsato@redhat.com> - 0.8-3
- Return empty string when there is no tailoring file
  Resolves: rhbz#1520276

* Mon Dec 11 2017 Watson Sato <wsato@redhat.com> - 0.8-2
- Add japanese translation
- Update other translations
  Resolves: rhbz#1481190
- Fix selection of RHEL datastream
  Resolves: rhbz#1520358

* Mon Nov 27 2017 Watson Sato <wsato@redhat.com> - 0.8-1
- Rebase to the upstream version 0.8
  Related: rhbz#1472419

* Tue May 30 2017 Watson Sato <wsato@redhat.com> - 0.7-15
- Add japanese translation
- Update other translations
  Resolves: rhbz#1383181

* Thu Apr 20 2017 Raphael Sanchez Prudencio <rsprudencio@redhat.com> - 0.7-14
- Fixed gtk warning messages when anaconda is starting.
  Resolves: rhbz#1437106

* Tue Mar 28 2017 Martin Preisler <mpreisle@redhat.com> - 0.7-13
- Avoid long delay before a GeoIP related timeout in case internet is not available
  Resolves: rhbz#1379479

* Tue Sep 13 2016 Vratislav Podzimek <vpodzime@redhat.com> - 0.7-12
- Properly handle tailoring files for datastreams
  Resolves: rhbz#1364929

* Thu Aug 25 2016 Vratislav Podzimek <vpodzime@redhat.com> - 0.7-11
- Don't require blank stderr when running the oscap tool
  Resolves: rhbz#1360765
- Beware of the invalid profiles
  Resolves: rhbz#1365130
- Properly set the seen property for root passwords
  Resolves: rhbz#1357603

* Thu Jun 30 2016 Vratislav Podzimek <vpodzime@redhat.com> - 0.7-10
- Clear spoke's info before setting an error
  Resolves: rhbz#1349446

* Wed Jun  1 2016 Vratislav Podzimek <vpodzime@redhat.com> - 0.7-9
- Use the System hub category provided by Anaconda
  Resolves: rhbz#1269211
- Wait for Anaconda to settle before evaluation
  Resolves: rhbz#1265552
- Make the changes overview scrollable and smaller
  Related: rhbz#1263582
- Make the list of profiles scrollable
  Resolves: rhbz#1263582
- Do not try to create a single file multiple times
  Related: rhbz#1263315
- Avoid crashes on extraction errors
  Resolves: rhbz#1263315
- Disable GPG checks when installing content to the system
  Resolves: rhbz#1263216
- Allow fixing root password in graphical installations
  Resolves: rhbz#1265116
- Enforce the minimal root password length
  Resolves: rhbz#1238281
- Just report misconfiguration instead of crashing in text mode
  Resolves: rhbz#1263207
- Do not verify SSL if inst.noverifyssl was given
  Resolves: rhbz#1263257
- Also catch data_fetch.DataFetchError when trying to get content
  Resolves: rhbz#1263239
- Use new method signature with payload class
  Related: rhbz#1288636

* Wed Sep 16 2015 Vratislav Podzimek <vpodzime@redhat.com> - 0.7-8
- Do not remove the root password behind user's back
  Resolves: rhbz#1263254

* Mon Sep 7 2015 Vratislav Podzimek <vpodzime@redhat.com> - 0.7-7
- Completely skip the execute() part if no profile is selected
  Resolves: rhbz#1254973

* Mon Aug 24 2015 Vratislav Podzimek <vpodzime@redhat.com> - 0.7-6
- Specify the name of the help content file
  Resolves: rhbz#1254884
- Skip files unrecognized by the 'oscap info' command
  Resolves: rhbz#1255075
- Only allow DS and XCCDF ID selection if it makes sense
  Resolves: rhbz#1254876

* Tue Aug 4 2015 Vratislav Podzimek <vpodzime@redhat.com> - 0.7-5
- Make sure DS and XCCDF ID lists are correctly refreshed
  Resolves: rhbz#1240946
- Make sure the DS and XCCDF ID combo boxes are visible for DS content
  Resolves: rhbz#1249951
- Try to load the OSCAP session early for DS content
  Resolves: rhbz#1247654
- Test preinst_content_path before raw_preinst_content_path
  Resolves: rhbz#1249937
- Clear any error if switching to the dry-run mode
  Related: rhbz#1247677
- Do not continue with and invalid profile ID
  Resolves: rhbz#1247677
- Cover all potential places with a non-main thread changing Gtk stuff
  Resolves: rhbz#1240967

* Thu Jul 23 2015 Vratislav Podzimek <vpodzime@redhat.com> - 0.7-4
- Better handle and report erroneous states
  Resolves: rhbz#1241064
- Make sure (some more) GUI actions run in the main thread
  Resolves: rhbz#1240967
- Beware of RPM->cpio entries' paths having absolute paths
  Related: rhbz#1241064
- Only output the kickstart section with content and profile set
  Resolves: rhbz#1241395
- Just report integrity check failure instead of traceback
  Resolves: rhbz#1240710
- Properly react on download/loading issues in text+kickstart mode
  Related: rhbz#1240710
- Fetch and process the content even if GUI doesn't take care of it
  Resolves: rhbz#1240625

* Tue Jul 7 2015 Vratislav Podzimek <vpodzime@redhat.com> - 0.7-3
- Do not output redundant/invalid fields for the SSG content (vpodzime)
  Resolves: rhbz#1240285
- Better handle unsupported URL types (vpodzime)
  Resolves: rhbz#1232631
- React better on network issues (vpodzime)
  Resolves: rhbz#1236657
- Improve the description of the default profile (vpodzime)
  Resolves: rhbz#1238080
- Use the openscap-scanner package instead of openscap-utils (vpodzime)
  Resolves: rhbz#1240249
- Better handle the case with no profile selected (vpodzime)
  Resolves: rhbz#1235750
- Add newline and one blank line after the %%addon section (vpodzime)
  Resolves: rhbz#1238267
- Word-wrap profile descriptions (vpodzime)
  Resolves: rhbz#1236644

* Wed Jun 17 2015 Vratislav Podzimek <vpodzime@redhat.com> - 0.7-2
- Add gettext to BuildRequires (vpodzime)
  Related: rhbz#1204640

* Tue Jun 16 2015 Vratislav Podzimek <vpodzime@redhat.com> - 0.7-1
- Rebase to the upstream version 0.7
  Related: rhbz#1204640

* Tue Apr 28 2015 Vratislav Podzimek <vpodzime@redhat.com> - 0.6-1
- Rebase to the upstream version 0.6
  Resolves: rhbz#1204640

* Mon Aug 04 2014 Vratislav Podzimek <vpodzime@redhat.com> - 0.4-3
- Don't distribute backup files
  Resolves: rhbz#1065906
* Wed Jan 15 2014 Vratislav Podizmek <vpodzime@redhat.com> - 0.4-2
- Skip running tests on RHEL builds
  Related: rhbz#1035662
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
