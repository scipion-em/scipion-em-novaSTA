# **************************************************************************
# *
# * Authors:     Juan Martin Pinilla (scipion@cnb.csic.es) [1]
# *
# * [1] Centro Nacional de Biotecnologia, CSIC, Spain
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'scipion@cnb.csic.es'
# *
# **************************************************************************

import pwem

from .constants import NOVASTA_HOME, NOVASTA_CUDA_LIB

__version__ = '3.0.5'
_logo = ""
_references = ["Turonova2017"]


class Plugin(pwem.Plugin):
    _homeVar = NOVASTA_HOME

    @classmethod
    def _defineVariables(cls):
        cls._defineEmVar(NOVASTA_HOME, 'novaSTA-master')
        cls._defineVar(NOVASTA_CUDA_LIB, pwem.Config.CUDA_LIB)

    @classmethod
    def getEnviron(cls):
        return None

    @classmethod
    def getDependencies(cls):
        neededPrograms = ['wget', 'unzip', 'fftw3', 'fftw3f', 'lib64', 'gcc']

        return neededPrograms

    @classmethod
    def defineBinaries(cls, env):
        version = 'master'
        NOVASTA_INSTALLED = 'novaSTA_%s_installed' % version
        warningMsg = "'WARNING: if program fails when executing reinstall in scipion3/software/em/novaSTA-master " \
                     "setting the path to the include files from fftw3 as well as following fftw3 libraries: fftw3 " \
                     "fftw3f. Typically both libraries should be in one folder and thus one library path should be " \
                     "sufficient. Example command:'" \
                     "'make includepath = \"path_to_fftw_include_files\" libpath = \"path_to_fftw_libraries\"'" \
                     "'NovaSTA also requires standard libraries with the standard path being " \
                     "/usr/lib64 - if the libraries are elsewhere open makefile and change the path accordingly'"

        # Display warning message
        installationCmd = 'echo %s && ' % warningMsg

        # Download git repo
        installationCmd += 'wget https://github.com/turonova/novaSTA/archive/refs/heads/master.zip && ' \
                           'unzip master.zip && '

        # Binaries compilation
        installationCmd += 'cd novaSTA-master && ' \
                           'make && ' \
                           'cd .. && '

        # Create installation finished flag file
        installationCmd += 'touch %s ' % NOVASTA_INSTALLED

        env.addPackage('novaSTA',
                       version=version,
                       tar='void.tgz',
                       neededProgs=cls.getDependencies(),
                       commands=[(installationCmd, NOVASTA_INSTALLED)],
                       default=True)

    @classmethod
    def runNovaSTA(cls, protocol, program, args, cwd=None):
        """ Run NovaSTA command from a given protocol. """
        fullProgram = '%s/%s/%s' % (cls.getVar(NOVASTA_HOME), "novaSTA-master", program)
        protocol.runJob(fullProgram, args, env=cls.getEnviron(), cwd=cwd)