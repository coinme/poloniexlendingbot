# coding=utf-8
import modules.Logger
import modules.Configuration
import modules.Poloniex


class Plugin(object):
    """
    @type cfg1: modules.Configuration
    @type api1: modules.Poloniex.Poloniex
    @type log1: modules.Logger.Logger
    """
    def __init__(self, cfg1, api1, log1, notify_config1):
        self.api = api1
        self.config = cfg1
        self.notify_config = notify_config1
        self.log = log1

    # override this to run plugin init code
    def on_bot_init(self):
        self.log.log(self.__class__.__name__ + ' plugin started.')

    # override this to run plugin loop code
    def on_bot_loop(self):
        pass

    # override this to run plugin stop code
    def on_bot_stop(self):
        pass
