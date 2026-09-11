#!/usr/bin/python3
# -*- encoding: utf8 -*-
#

class FilterModule(object):
    ''' Give back filters to Ansible '''

    def filters(self):
        return {
            'filtre_test': self.msg
        }

    def msg(self,data,str):
        return data + ' ' + str
