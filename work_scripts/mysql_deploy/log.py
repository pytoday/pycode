#!/usr/bin/env python3
# coding=utf-8
# title          : log.py
# description    : rewrite logging
# author         : JackieTsui
# organization   : pytoday.org
# date           : 2018/7/2 5:00
# email          : jackietsui72@gmail.com
# notes          :
# ==================================================

# Import the module needed to run the script
import logging


class Log:
    def __init__(self, log_name=None, app_name=None):
        # get logging instance
        self.app_name = app_name
        if self.app_name:
            self.logger = logging.getLogger(app_name)
        else:
            self.logger = logging.getLogger(__name__)
        self.Formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
        # set log name
        self.log_name = log_name
        if not self.logger.handlers:
            if self.log_name:
                self.file_handler = logging.FileHandler(self.log_name)
            else:
                self.file_handler = logging.FileHandler("/tmp/"+__name__+".log")
            self.file_handler.setFormatter(self.Formatter)  # log path
            self.logger.setLevel(logging.INFO)  # set default log level
            self.logger.addHandler(self.file_handler)  # log to file

    # rewrite method
    def info(self, message=None):
        self.logger.info(message)
        self.logger.removeHandler(self.logger.handlers)

    def debug(self, message=None):
        self.logger.debug(message)
        self.logger.removeHandler(self.logger.handlers)

    def warning(self, message=None):
        self.logger.warning(message)
        self.logger.removeHandler(self.logger.handlers)

    def error(self, message=None):
        self.logger.error(message)
        self.logger.removeHandler(self.logger.handlers)

    def critical(self, message=None):
        self.logger.critical(message)
        self.logger.removeHandler(self.logger.handlers)

    def fatal(self, message=None):
        self.logger.fatal(message)
        self.logger.removeHandler(self.logger.handlers)
