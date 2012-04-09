
from sc2reader.utils import AttributeDict
from sc2reader.graham_data import configuration
from sc2reader.graham_data import versionv12
from sc2reader.graham_data import versionv133
from sc2reader.graham_data import versionv13
from sc2reader.graham_data import versionv142
from sc2reader.graham_data import versionv14

v12 = configuration.Data(versionv12.version)
v133 = configuration.Data(versionv133.version)
v13 = configuration.Data(versionv13.version)
v14 = configuration.Data(versionv14.version)
v142 = configuration.Data(versionv142.version)
