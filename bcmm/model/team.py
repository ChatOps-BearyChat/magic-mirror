# -*- coding: utf-8 -*-

from __future__ import absolute_import

from bcmm.model.base import Model


class Team(Model):

    def __init__(self, **kwargs):
        self.pk = kwargs['id']

        self.update(_replace=True, **kwargs)

        super(Team, self).__init__()

    def update(self, **kwargs):
        _replace = kwargs.get('_replace', False)
        fields = ('name', 'subdomain', 'description', 'logo_url', 'plan',)
        for field in fields:
            v = kwargs.get(field)
            if v or _replace:
                setattr(self, field, v)
