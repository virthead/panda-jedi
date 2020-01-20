
from pandacommon.pandamsgbkr import msg_processor
from pandacommon.pandalogger import logger_utils

from pandajedi.jediconfig import jedi_config


# logger
msg_processor.base_logger = logger_utils.setup_logger('JediMsgProcessor')


# Main message processing agent
class MsgProcAgent(msg_processor.MsgProcAgentBase):
    pass


# launch
def launcher():
    tmp_log = logger_utils.make_logger(msg_processor.base_logger, method_name='launcher')
    tmp_log.debug('start')
    try:
        config_file = jedi_config.msgprocessor.configFile
    except Exception as e:
        tmp_log.error('failed to read config json file; should not happen... {0}: {1}'.format(e.__class__.__name__, e))
        raise e
    else:
        agent = MsgProcAgent(config_file)
        agent.run()
