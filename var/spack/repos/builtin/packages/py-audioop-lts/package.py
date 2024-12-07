# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyAudioopLts(PythonPackage):
    """LTS Port of Python audioop"""

    homepage = "https://github.com/AbstractUmbra/audioop"
    pypi = "audioop_lts/audioop_lts-0.2.1.tar.gz"

    # Omitting license due to custom

    version("0.2.1", sha256="e81268da0baa880431b68b1308ab7257eb33f356e57a5f9b1f915dfb13dd1387")

    depends_on("c", type="build")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.13:", type=("build", "run"))

