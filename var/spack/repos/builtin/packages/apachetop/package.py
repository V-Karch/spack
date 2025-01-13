# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Apachetop(AutotoolsPackage):
    """ApacheTop watches a logfile generated by Apache (in standard common or
    combined logformat, and generates human-parsable output in realtime.)
    See the INSTALL file for ./configure options (there's a few newly added
    since v0.11)"""

    homepage = "https://github.com/tessus/apachetop"
    url = "https://github.com/tessus/apachetop/archive/0.19.7.tar.gz"

    version("0.23.2", sha256="4bce0120cb7b160256329f5d9253dc196b8690b33bdf410acc9c746bfa6d739d")
    version("0.19.7", sha256="88abf58ee5d7882e4cc3fa2462865ebbf0e8f872fdcec5186abe16e7bff3d4a5")
    version("0.18.4", sha256="1cbbfd1bf12275fb21e0cb6068b9050b2fee8c276887054a015bf103a1ae9cc6")
    version("0.17.4", sha256="892ed3b83b45eb38811e74d068089b1e8c34707787f240ce133d8c93198d7ff0")
    version("0.15.6", sha256="7343caeb1adab795439b7be9cf47ce6049751ae948537d5f27251c075264801a")

    depends_on("cxx", type="build")  # generated

    depends_on("autoconf", type="build")
    depends_on("automake", type="build")
    depends_on("libtool", type="build")
    depends_on("m4", type="build")
    depends_on("readline")
