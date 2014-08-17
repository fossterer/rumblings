NOTE: The following information is true with any regular project too (not necessarily licensed as open source)

Doing a 'git clone git://git.gnome.org/gnome-screenshot' inside my new '~/Projects/gnome/' directory, I find a few familiar files:

(The idea - I need to build the cloned code to have a working implementation which I can use to test my changes)

+----------------+------------------------------------------------------------+
| FILE           |                A few Contents & Description                |
+----------------+------------------------------------------------------------+
|                |                                                            |
|autogen.sh      |     - REQUIRED_AUTOCONF_VERSION=2.59                       |
|                |     - REQUIRED_AUTOMAKE_VERSION=1.11                       |
|                |     - REQUIRED_INTLTOOL_VERSION=0.40.0                     |
|                |     - REQUIRED_PKG_CONFIG_VERSION=0.22                     |
|                |                                                            |
|                |     (You might have found the tools mentioned above        |
|                |        sometime ago in the GNU toolchain, right?)          |
+----------------+------------------------------------------------------------+
|configure.ac    |    After executing the above file successully, this gets   |
|                |    renamed to **configure**, an executable script!         |
|                |                                                            |
|                |       This would become the second one to execute          |
+----------------+------------------------------------------------------------+
|Makefile        |   After doing a successul 'configure', you can issue a     |
|                |   **make** which reads the contents of this file to finish |
|                |   the build process and provide yout the final executable  |
|                |   of this project.                                         |
+----------------+------------------------------------------------------------+
