__author__ = 'Tavern'
# coding:utf-8


class HTMLBuilder(object):
    @classmethod
    def Table(cls, lists=[]):
        table = "<table>"
        for tr in lists:
            table += '<tr>'
            if isinstance(tr, list):
                for td in tr:
                    table += '<td>%s</td>' % td
            table += '</tr>'
        table += "</table>"
        return table
