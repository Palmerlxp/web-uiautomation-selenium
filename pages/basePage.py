#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
@author: zhaogao
@license: (C) Copyright 2013-2018.
@contact: gaozhao89@qq.com
@software: web-uiautomation-selenium
@file: basePage
@time: 06/06/2018 11:24 AM
'''
from utils.loggingFactory import Log
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from utils import pathFactory

import datetime, os, time

log = Log().getLog('Base')
current_path = os.getcwd()


class Base(object):
    def __init__(self, driver):
        self.driver = driver

    def go(self, url):
        log.info('go to url %s' % (self, url))
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def execute(self, command, params=None):
        self.driver.execute(command, params)

    def current_url(self):
        return self.driver.current_url

    def page_source(self):
        return self.driver.page_source

    def close(self):
        log.info('close current window')
        self.driver.close()

    def quit(self):
        log.info('quit current session')
        self.driver.quit()

    def max(self):
        log.info('set maximize of current window')
        self.driver.maximize_window()

    def back(self):
        log.info('go back')
        self.driver.back()

    def forward(self):
        log.info('forward')
        self.driver.forward()

    def refresh(self):
        log.info('refresh')
        self.driver.refresh()

    def get_cookies(self):
        return self.driver.get_cookies()

    def get_cookie(self, name):
        return self.driver.get_cookie(name)

    def delete_cookie(self, name):
        self.driver.delete_cookie(name)

    def delete_cookie3(self):
        self.driver.delete_all_cookies()

    def add_cookie(self, cookie):
        self.driver.add_cookie(cookie)

    def set_loc_wait(self, sec):
        self.driver.implicitly_wait(sec)

    def set_script_wait(self, sec):
        self.driver.set_script_timeout(sec)

    def set_page_wait(self, sec):
        self.driver.set_page_load_timeout(sec)

    def set_window_size(self, width, height):
        self.driver.set_window_size(width, height)

    def get_window_size(self):
        return self.driver.get_window_size()

    def set_window_position(self, x, y):
        self.driver.set_window_position(x, y)

    def get_window_position(self):
        return self.driver.get_window_position()

    def get_window_rect(self):
        return self.driver.get_window_rect()

    def set_window_rect(self, x=None, y=None, width=None, height=None):
        self.driver.set_window_rect(x, y, width, height)

    def find(self, loc):
        try:
            return self.driver.find_element(*loc)
        except NoSuchElementException:
            self.log.info('no element %s was found in page' % (self, loc))

    def finds(self, loc):
        try:
            return self.driver.find_elements(*loc)
        except NoSuchElementException:
            log.info('no element %s was found in page' % (self, loc))

    def driver_wait(self, loc, sec):
        try:
            WebDriverWait(self.driver, sec).until(lambda driver: driver.find_element(*loc).is_displayed())
        except NoSuchElementException:
            self.log.info('no element %s was found in page' % (self, loc))

    def take_screen_shot(self, name):
        date_format = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        pf = pathFactory
        screenshots_path = pf.get_abs_path(
            pf.path_join(pf.get_workspace_root_path(), 'screenshots'))
        screenshots_name = date_format.join(name, '.png')
        pf.make_dir(screenshots_path)
        self.driver.get_screenshot_as_file(pf.path_join(screenshots_path, screenshots_name))

    def is_exist(self, loc):
        try:
            self.driver.find_element(*loc).is_displayed()
            return True
        except NoSuchElementException:
            log.info('no element %s was found in page' % (self, loc))
            return False

    def click(self, loc, find_first=True):
        try:
            if find_first:
                self.is_exist(loc)
            self.find(loc).click()
        except NoSuchElementException:
            log.info('no element %s was found in page' % (self, loc))

    def input(self, loc, text, find_first=True, clear_content=True):
        try:
            if find_first:
                self.is_exist(loc)
            if clear_content:
                self.find(loc).clear()
            self.find(loc).send_keys(text)
        except NoSuchElementException:
            log.info('no element %s was found in page' % (self, loc))

    @staticmethod
    def sleep(sec=3):
        log.info('sleep for %s seconds' % sec)
        time.sleep(sec)