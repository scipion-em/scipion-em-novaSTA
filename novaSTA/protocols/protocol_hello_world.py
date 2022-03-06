# -*- coding: utf-8 -*-
# **************************************************************************
# *
# * Authors:     Juan Martin Pinilla (scipion@cnb.csic.es)
# *
# * your institution
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
# *  e-mail address 'you@yourinstitution.email'
# *
# **************************************************************************


"""
Describe your python module here:
This module will provide the traditional Hello world example
"""
from pyworkflow.protocol import Protocol, params, Integer
from pyworkflow.utils import Message


class novaSTAPrefixHelloWorld(Protocol):
    """
    This protocol will print hello world in the console
    IMPORTANT: Classes names should be unique, better prefix them
    """
    _label = 'NovaSTA'

    # -------------------------- DEFINE param functions ----------------------
    def _defineParams(self, form):
        """ Define the input parameters that will be used.
        Params:
            form: this is the form to be populated with sections and params.
        """
        # You need a params to belong to a section:
        form.addSection(label=Message.LABEL_INPUT)

        # Este primer parametro no va al fichero, es para el comando principal

        '''form.addParam('nCores', params.IntParam,
                      default=0,
                      allowsNull=False,
                      label='Number of cores',
                      help='Number of cores when running with CPU parallelization',
                      allowsPointers=False)
        '''

        form.addParam('extractSubtomos', params.IntParam,
                      default=1,
                      allowsNull=False,
                      label='Extract Subtomos',
                      help='Previous count of printed messages',
                      allowsPointers=False)

        form.addParam('createRef', params.IntParam,
                      default=0,
                      allowsNull=False,
                      label='Create Ref',
                      help='Previous count of printed messages',
                      allowsPointers=False)

        form.addParam('symmetry', params.IntParam,
                      default=1,
                      allowsNull=False,
                      label='Symmetry',
                      help='Previous count of printed messages',
                      allowsPointers=False)

        form.addParam('class', params.IntParam,
                      default=1,
                      allowsNull=False,
                      label='class',
                      help='Previous count of printed messages',
                      allowsPointers=False)

        form.addParam('threshold', params.FloatParam,
                      default=0.0,
                      allowsNull=False,
                      label='Threshold',
                      help='Previous count of printed messages',
                      allowsPointers=False)

        form.addParam('motl', params.StringParam,
                      default='./path/to/allmotl',
                      label='Motl',
                      help='What will be printed in the console.')

        form.addParam('folder', params.StringParam,
                      default='./path/to/processing/folder',
                      label='Folder',
                      help='What will be printed in the console.')

        form.addParam('ref', params.StringParam,
                      default='./path/to/ref',
                      label='Ref',
                      help='What will be printed in the console.')

        form.addParam('mask', params.StringParam,
                      default='../path/to/mask.em',
                      label='Mask',
                      help='What will be printed in the console.')

        form.addParam('ccMask', params.StringParam,
                      default='../path/to/ccmask.em',
                      label='ccMask',
                      help='What will be printed in the console.')

        form.addParam('wedgeList', params.StringParam,
                      default='../path/to/wedge_list.em',
                      label='Wedge List',
                      help='What will be printed in the console.')

        form.addParam('subtomograms', params.StringParam,
                      default='../path/to/subtomograms/subtomo',
                      label='Subtograms',
                      help='What will be printed in the console.')

        form.addParam('iter', params.IntParam,
                      default=2,
                      allowsNull=False,
                      label='Iter',
                      help='Previous count of printed messages',
                      allowsPointers=False)

        form.addParam('startIndex', params.IntParam,
                      default=0,
                      allowsNull=False,
                      label='Start Index',
                      help='Previous count of printed messages',
                      allowsPointers=False)

        form.addParam('phiIter', params.IntParam,
                      default=2,
                      allowsNull=False,
                      label='phiIter',
                      help='Previous count of printed messages',
                      allowsPointers=False)

        form.addParam('phiIncr', params.IntParam,
                      default=1,
                      allowsNull=False,
                      label='phiIncr',
                      help='Previous count of printed messages',
                      allowsPointers=False)

        form.addParam('angIter', params.IntParam,
                      default=2,
                      allowsNull=False,
                      label='angIter',
                      help='Previous count of printed messages',
                      allowsPointers=False)

        form.addParam('angIncr', params.IntParam,
                      default=2,
                      allowsNull=False,
                      label='angIncr',
                      help='Previous count of printed messages',
                      allowsPointers=False)

        form.addParam('lowPass', params.IntParam,
                      default=13,
                      allowsNull=False,
                      label='lowPass',
                      help='Previous count of printed messages',
                      allowsPointers=False)

        form.addParam('highPass', params.IntParam,
                      default=1,
                      allowsNull=False,
                      label='highPass',
                      help='Previous count of printed messages',
                      allowsPointers=False)

        form.addParam('subtomoSize', params.IntParam,
                      default=32,
                      allowsNull=False,
                      label='subtomoSize',
                      help='Previous count of printed messages',
                      allowsPointers=False)

        form.addParam('tomograms', params.StringParam,
                      default='./',
                      label='Tomograms',
                      help='What will be printed in the console.')

        form.addParam('tomoDigits', params.IntParam,
                      default=3,
                      allowsNull=False,
                      label='tomoDigits',
                      help='Previous count of printed messages',
                      allowsPointers=False)

        # GPU settings
        form.addHidden(params.USE_GPU, params.BooleanParam, default=True,
                       expertLevel=params.LEVEL_ADVANCED,
                       label="Use GPU (vs CPU)",
                       help="Set to true if you want to use GPU implementation ")
        form.addHidden(params.GPU_LIST, params.StringParam, default='0',
                       expertLevel=params.LEVEL_ADVANCED,
                       label="Choose GPU ID",
                       help="GPU may")

        form.addParallelSection(threads=1, mpi=1)

        # --------------------------- STEPS functions ------------------------------
    def _insertAllSteps(self):
        # Insert processing steps
        self._insertFunctionStep(self.generateParamsFile)
        #self._insertFunctionStep(self.novaSTAStep)
        self._insertFunctionStep('createOutputStep')

    def novaSTAStep(self):
        # say what the parameter says!!

        pass

    def generateParamsFile(self):
        filename = self._getExtraPath("parameter_file.txt")
        print(filename)
        f = open(filename, "w")
        gpuToUse = self.getGpuList()[0]
        f.write("useGPU %i \n" % gpuToUse)
        f.write("extractSubtomos %i \n" % self.extractSubtomos)
        f.write("createRef %i \n" % self.createRef)
        f.write("symmetry %i \n" % self.symmetry)
        f.write("class %i \n" % self.getParam('class'))
        f.write("threshold %i \n" % self.getParam('threshold'))
        f.write("motl %i \n" % self.getParam('motl'))
        f.write("folder %s" % self.getParam('folder'))
        f.write("ref %s" % self.getParam('ref'))
        f.write("mask %s" % self.getParam('mask'))
        f.write("ccMask %s" + str(self.getParam('ccMask')) + "\n")
        f.write("wedgeList %s" + str(self.getParam('wedgeList')) + "\n")
        f.write("subtomograms %s" + str(self.getParam('subtomograms')) + "\n")
        f.write("iter " + str(self.getParam('iter')) + "\n")
        f.write("starIndex " + str(self.getParam('starIndex')) + "\n")
        f.write("phiIter " + str(self.getParam('phiIter')) + "\n")
        f.write("phiIncr " + str(self.getParam('phiIncr')) + "\n")
        f.write("angIter " + str(self.getParam('angIter')) + "\n")
        f.write("angIncr " + str(self.getParam('angIncr')) + "\n")
        f.write("lowPass " + str(self.getParam('lowPass')) + "\n")
        f.write("highPass " + str(self.getParam('highPass')) + "\n")
        f.write("subtomoSize " + str(self.getParam('subtomoSize')) + "\n")
        f.write("tomograms " + str(self.getParam('tomograms')) + "\n")
        f.write("tomoDigits " + str(self.getParam('tomoDigits')) + "\n")

        f.close()


    def createOutputStep(self):
        # register how many times the message has been printed
        # Now count will be an accumulated value
        #timesPrinted = Integer(self.times.get() + self.previousCount.get())
        timesPrinted = 3
        self._defineOutputs(count=timesPrinted)

    # --------------------------- INFO functions -----------------------------------
    def _summary(self):
        """ Summarize what the protocol has done"""
        summary = []

        if self.isFinished():
            summary.append("This protocol has printed *%s* %i times." % (self.message, self.times))
        return summary

    def _methods(self):
        methods = []

        if self.isFinished():
            methods.append("%s has been printed in this run %i times." % (self.message, self.times))
            if self.previousCount.hasPointer():
                methods.append("Accumulated count from previous runs were %i."
                               " In total, %s messages has been printed."
                               % (self.previousCount, self.count))
        return methods
