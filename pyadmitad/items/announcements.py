# coding: utf-8
from __future__ import unicode_literals

from pyadmitad.items.base import Item


__all__ = [
    'Announcements',
]


class Announcements(Item):
    """
    List of announcements

    """

    SCOPE = 'announcements'

    URL = Item.prepare_url('announcements')
    SINGLE_URL = Item.prepare_url('announcements/%(announcement_id)s')

    def get(self, **kwargs):
        """
        Args:
            limit (int)
            offset (int)

        """
        return self.transport.get().set_pagination(**kwargs).request(url=self.URL)

    def getOne(self, _id, **kwargs):
        """
        Args:
            _id (int)

        """
        request_data = {
            'url': self.SINGLE_URL,
            'announcement_id': Item.sanitize_id(_id)
        }

        return self.transport.get().request(**request_data)
