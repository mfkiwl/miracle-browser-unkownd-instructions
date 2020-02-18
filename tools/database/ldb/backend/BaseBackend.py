
import sqlalchemy

from ..records import Device
from ..records import Board
from ..records import Core
from ..records import Target
from ..records import Experiment
from ..records import TraceSet
from ..records import StatisticTrace

class BaseBackend(object):
    """
    Class from which all other backends are derived. Provides the base
    interface which all backend classes must provide.
    """

    def __init__(self, path, autocommit=False):
        """
        Create a new connection to a database
        """
        self._engine        = sqlalchemy.create_engine(path)
        self._SessionMaker  = sqlalchemy.orm.sessionmaker(bind=self._engine)
        self._session       = self._SessionMaker()

        self._autocommit    = autocommit

    @property
    def autocommit(self):
        """
        Automatically commit everything to the database after every call
        to an insert/update/remove function
        """
        return self._autocommit

    @autocommit.setter
    def autocommit(self, value):
        self._autocommit = value


    def _handleAutocommit(self):
        """
        Called at the end of each insert/remove/update function to
        handle automatic comitting of pending operations.
        """
        if(self._autocommit):
            self.commit()


    def commit(self):
        """
        Commit pending operations to the database
        """
        self._session.commit()


    def createNew(path):
        """
        Creates a new database, as per the records schema.

        Returns True if everything was successful, else False
        """


    def insertDevice(self, device):
        """
        Insert a new device into the database, as described by the
        device parameter.

        :returns: None
        """
        self._session.add(device)
        self._handleAutocommit()
        return None


    def insertBoard(self, board):
        """
        Insert a new board into the database, as described by the
        board parameter.

        :returns: None
        """
        self._session.add(board)
        self._handleAutocommit()
        return None
    

    def insertCore(self, cpu ):
        """
        Insert a new Core into the database, as described by the
        cpu parameter.

        :returns: None
        """
        self._session.add(cpu)
        self._handleAutocommit()
        return None


    def insertTarget(self, target):
        """
        Insert a new target device into the database, as described by the
        target parameter.

        :returns: None
        """
        self._session.add(target)
        self._handleAutocommit()
        return None


    def insertExperiment(self, experiment):
        """
        Insert a new experiment into the database, as described by the
        experiment parameter.

        :returns: None
        """
        self._session.add(experiment)
        self._handleAutocommit()
        return None

    
    def insertTraceSet(self, traceSet):
        """
        Insert a new traceSet into the database, as described by the
        traceSet parameter.

        :returns: None
        """
        self._session.add(traceSet)
        self._handleAutocommit()
        return None


    def insertStatisticTrace(self, statisticTrace):
        """
        Insert a new statisticTrace into the database, as described by the
        statisticTrace parameter.

        :returns: None
        """
        assert(False)

        self._handleAutocommit()
        return None


    def getAllDevices(self):
        """
        Return an iterator which will iterate through all devices
        in the database.
        """
        return self._session.query(Device).order_by(Device.id)


    def getAllBoards(self):
        """
        Return an iterator which will iterate through all boards 
        in the database.
        """
        return self._session.query(Board).order_by(Board.id)


    def getAllCores(self):
        """
        Return an iterator which will iterate through all cores
        in the database.
        """
        return self._session.query(Core).order_by(Core.id)


    def getAllTargets(self):
        """
        Return an iterator which will iterate through all targets
        in the database.
        """
        return self._session.query(Target).order_by(Target.id)


    def getAllTraceSets(self):
        """
        Return an iterator which will iterate through all trace sets 
        in the database.
        """
        return self._session.query(TraceSet).order_by(TraceSet.id)


    def getAllExperiments(self):
        """
        Return an iterator which will iterate through all experiments
        in the database.
        """
        return self._session.query(Experiment).order_by(Experiment.id)


    def getDeviceById(self, deviceId):
        """
        Return an instance of the Device class from the database with
        the supplied deviceId.

        :returns: None or Device
        """
        return self._session.query(Device).filter_by(id=deviceId).first()


    def getBoardById(self, boardId):
        """
        Return an instance of the Board class from the database with
        the supplied boardId.

        :returns: None or Board
        """
        return self._session.query(Board).filter_by(id=boardId).first()


    def getCoreById(self, coreId):
        """
        Return an instance of the Core class from the database with
        the supplied coreId.

        :returns: None or Core
        """
        return self._session.query(Core).filter_by(id=coreId).first()


    def getTargetById(self, targetId):
        """
        Return an instance of the Target class from the database with
        the supplied targetId.

        :returns: None or Target 
        """
        return self._session.query(Target).filter_by(id=targetId).first()


    def getDeviceByName(self, deviceName):
        """
        Return an instance of the Device class from the database with
        the supplied deviceName.

        :returns: None or Device
        """
        return self._session.query(Device).filter_by(name=deviceName).first()


    def getBoardByName(self, boardName):
        """
        Return an instance of the Board class from the database with
        the supplied boardName.

        :returns: None or Board
        """
        return self._session.query(Board).filter_by(name=boardName).first()


    def getCoreByName(self, coreName):
        """
        Return an instance of the Core class from the database with
        the supplied coreName.

        :returns: None or Core
        """
        return self._session.query(Core).filter_by(name=coreName).first()


    def getTargetByName(self, targetName):
        """
        Return an instance of the Target class from the database with
        the supplied targetName.

        :returns: None or Target 
        """
        return self._session.query(Target).filter_by(name=targetName).first()
    

    def getExperimentById(self, experimentId):
        """
        Return an instance of the Experiment class from the database with
        the supplied experimentId.

        :returns: None or Experiment
        """
        return self._session.query(Experiment).filter_by(id=experimentId).first()

    
    def getExperimentByCatagoryAndName(self, catagory, name):
        """
        Return an instance of the Experiment class from the database
        which has the supplied catagory and name values.

        :returns: None or Experiment
        """
        return self._session.query(Experiment).filter_by(
            catagory = catagory,
            name     = name
        ).first()

    
    def getTraceSetById(self, traceSetId):
        """
        Return an instance of the TraceSet class from the database with
        the supplied traceSetId.

        :returns: None or TraceSet 
        """
        return self._session.query(TraceSet).filter_by(id=traceSetId).first()


    def getTraceSetsForTargetAndExperiment(self, targetId, experimentId):
        """
        Return an iterable of all trace sets associated with the supplied
        target and experiment.
        """
        return self._session.query(TraceSet).filter_by (
            experimentId = experimentId,
            targetId     = targetId
        )


    def getStatisticTraceById(self, statisticTraceId):
        """
        Return an instance of the StatisticTrace class from the database with
        the supplied statisticTraceId.

        :returns: None or StatisticTrace 
        """
        assert(False)

        return None


    def removeDevice(self, deviceId):
        """
        Remove the device from the database with the supplied Id,
        along with all experimental data from the database which
        points to that device.
        """
        assert(False)

        self._handleAutocommit()
        return None


    def removeBoard(self, boardId):
        """
        Remove the board from the database with the supplied Id,
        along with all experimental data from the database which
        points to that board.
        """
        assert(False)

        self._handleAutocommit()
        return None


    def removeCore(self, coreId):
        """
        Remove the Core from the database with the supplied Id,
        along with all experimental data from the database which
        points to that Core.
        """
        assert(False)

        self._handleAutocommit()
        return None


    def removeTarget(self, targetId):
        """
        Remove the target from the database with the supplied Id,
        along with all experimental data from the database which
        points to that target.
        """
        assert(False)

        self._handleAutocommit()
        return None

    
    def removeExperiment(self, experimentId):
        """
        Remove the experiment from the database with the supplied Id,
        along with all experimental data from the database which
        points to that experiment.
        """
        assert(False)

        self._handleAutocommit()
        return None
    
    
    def removeTraceSet(self, traceSetId):
        """
        Remove the traceSet from the database with the supplied Id,
        along with all statistic traces which are derived from it.
        """
        assert(False)

        self._handleAutocommit()
        return None

    
    def removeStatisticTrace(self, statisticTraceId):
        """
        Remove the statistic from the database with the supplied Id
        """
        assert(False)

        self._handleAutocommit()
        return None

