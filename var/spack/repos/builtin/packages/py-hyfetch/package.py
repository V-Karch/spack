# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyHyfetch(PythonPackage):
    """neofetch with flags <3"""

    homepage = "https://github.com/hykilpikonna/HyFetch"
    pypi = "HyFetch/HyFetch-1.99.0.tar.gz"

    license("MIT", checked_by="V-Karch")

    version("1.99.0", sha256="ddeb422fd797c710f0ad37d584fac466df89e39feddeef765492b2c0b529616e")

    # PKG-INFO
    depends_on("py-setuptools", type="build")
    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-typing-extensions", type=("build", "run"))
    depends_on("py-psutil", type=("build", "run"), when="platform=windows")
    depends_on("py-colorama@0.4.6:", type=("build", "run"), when="platform=windows")
