# -*- coding: iso-8859-1 -*-
"""
    MoinMoin - Freifunk Kassel theme

    @copyright: 2003-2005 Nir Soffer, Thomas Waldmann
    @license: GNU GPL, see COPYING for details.
"""

from MoinMoin.theme import ThemeBase

class Theme(ThemeBase):

    name = "ffks"

    def header(self, d, **kw):
        """ Assemble wiki header

        @param d: parameter dictionary
        @rtype: unicode
        @return: page header html
        """
        html = [
            # Pre header custom html
            self.emit_custom_html(self.cfg.page_header1),

    		# Wrapper
            u'<div class="wrapper">',

            # Header
            u'<div class="header-wrap">',
            self.logo(),


            u'<header class="site-header">',

    		# v Social
            u'<div class="social">',
            u'<ul class="social-media-list">',

    		# Mail
            u'<li>',
    		u'<a href="mailto:hallo@freifunk-kassel.de">',
    		u'<i class="fa fa-envelope"></i>',
    		u'hallo@freifunk-kassel.de',
    		u'</a>',
            u'</li>',

    		# GitHub
            u'<li>',
    		u'<a target="_blank" href="https://github.com/freifunkks">',
    		u'<i class="fa fa-github"></i>',
    		u'freifunkks',
    		u'</a>',
            u'</li>',

    		# Twitter 
            u'<li>',
    		u'<a target="_blank" href="https://twitter.com/freifunkks">',
    		u'<i class="fa fa-twitter"></i>',
    		u'freifunkks',
    		u'</a>',
            u'</li>',

    		# RSS
            u'<li>',
    		u'<a target="_blank" href="https://twitter.com/freifunkks">',
    		u'<i class="fa fa-rss"></i>',
    		u'Neuigkeiten',
    		u'</a>',
            u'</li>',

            u'</ul>',
            u'</div>',
    		# ^ Social


            self.navibar(d),
            #u'<hr id="pageline">',
            #u'<div id="pageline"><hr style="display:none;"></div>',
            u'</header>',

            u'</div>',

    		# do we need a search?
            #self.searchform(d),

    		# not used?!
            #self.interwiki(d),
            #self.trail(d),


            # Post header custom html (not recommended)
            self.emit_custom_html(self.cfg.page_header2),

            self.msg(d),
            self.editbar(d),
            self.title(d),

            # Start of page
            self.startPage(),
        ]
        return u'\n'.join(html)

    def editorheader(self, d, **kw):
        """ Assemble wiki header for editor

        @param d: parameter dictionary
        @rtype: unicode
        @return: page header html
        """
        html = [
            # Pre header custom html
            self.emit_custom_html(self.cfg.page_header1),

            # Header
            u'<div id="header">',
            self.title(d),
            self.msg(d),
            u'</div>',

            # Post header custom html (not recommended)
            self.emit_custom_html(self.cfg.page_header2),

            # Start of page
            self.startPage(),
        ]
        return u'\n'.join(html)

    def footer(self, d, **keywords):
        """ Assemble wiki footer

        @param d: parameter dictionary
        @keyword ...:...
        @rtype: unicode
        @return: page footer html
        """
        page = d['page']
        html = [
            # End of page
            self.pageinfo(page),
            self.endPage(),

            # Pre footer custom html (not recommended!)
            self.emit_custom_html(self.cfg.page_footer1),

            # Footer
            u'<div id="footer">',

    		# Two times needed?
            #self.editbar(d),

    		# Sorry, but you'll be mentioned somewhere else
            #self.credits(d),
            #self.showversion(d, **keywords),

            self.username(d),
            u'<ul id="footerpages">',
            u'<li><a rel="nofollow" href="/wiki/&Auml;nderungen">&Auml;nderungen</a></li>',
            u'<li><a rel="nofollow" href="/wiki/Hilfe">Hilfe</a></li>',
            u'<li><a rel="nofollow" href="/wiki/Impressum">Impressum</a></li>',
            u'</ul>',
            u'</div>',


            # Post footer custom html
            self.emit_custom_html(self.cfg.page_footer2),

    		# Wrapper
            u'</div>',
            ]
        return u'\n'.join(html)


def execute(request):
    """
    Generate and return a theme object

    @param request: the request object
    @rtype: MoinTheme
    @return: Theme object
    """
    return Theme(request)

