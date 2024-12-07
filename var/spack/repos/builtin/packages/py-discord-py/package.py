# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyDiscordPy(PythonPackage):
    """A Python wrapper for the Discord API"""

    homepage = "https://github.com/Rapptz/discord.py"
    pypi = "discord_py/discord_py-2.4.0.tar.gz"

    license("MIT", checked_by="V-Karch")

    version("2.4.0", sha256="d07cb2a223a185873a1d0ee78b9faa9597e45b3f6186df21a95cec1e9bcdc9a5")
    
    variant("voice", default=True, description="With voice capabilities")

    depends_on("py-setuptools", type="build")
    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-aiohttp@3.7.4:3", type=("build", "run"))
    depends_on("py-audioop-lts", type=("build", "run"))
    
    depends_on("py-black", type=("build", "run"))    

    depends_on("py-pynacl@1.3.0:1.5", type=("build", "run"), when="+voice")   
