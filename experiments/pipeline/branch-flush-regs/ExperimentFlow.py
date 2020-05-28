
import os
import logging as log

EXPERIMENT_CATAGORY = "pipeline"
EXPERIMENT_NAME     = "branch-flush-regs"

def runCapture(args):
    """
    Top level function for running all trace capture processes for this
    experiment.
    """
    return args.runAndInsertTTest (
            EXPERIMENT_CATAGORY ,
            EXPERIMENT_NAME     ,
            {}
        )


def runAnalysis(aif):
    """
    Run any experiment specific analysis.

    aif - AnalysisInterface instance
    """

    aif.runDefaultAnalysis()

    for ttest in aif.getTTestsForTargetAndExperiment():
        aif.runHammingDistanceAnalysis(ttest.randomTraceSet, "di1","di2")