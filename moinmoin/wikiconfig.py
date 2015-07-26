# -*- coding: iso-8859-1 -*-
# MoinMoin - Configuration for the Freifunk Kassel Wiki

import sys
import os

from MoinMoin.config import multiconfig, url_prefix_static

class Config(multiconfig.DefaultConfig):

    # General MoinMoin Setup --------------------------------------------
    # This has to be filled with your own config settings

    # User interface ----------------------------------------------------
    navi_bar = [
        u'Info',
        u'News',
        u'Firmware',
        u'Karte',
        u'Kontakt',
    ]

    # Favicons everywhere
    html_head = '''
    <link rel="apple-touch-icon" sizes="57x57" href="/wikistatic/icons/apple-touch-icon-57x57.png">
    <link rel="apple-touch-icon" sizes="60x60" href="/wikistatic/icons/apple-touch-icon-60x60.png">
    <link rel="apple-touch-icon" sizes="72x72" href="/wikistatic/icons/apple-touch-icon-72x72.png">
    <link rel="apple-touch-icon" sizes="76x76" href="/wikistatic/icons/apple-touch-icon-76x76.png">
    <link rel="apple-touch-icon" sizes="114x114" href="/wikistatic/icons/apple-touch-icon-114x114.png">
    <link rel="apple-touch-icon" sizes="120x120" href="/wikistatic/icons/apple-touch-icon-120x120.png">
    <link rel="apple-touch-icon" sizes="144x144" href="/wikistatic/icons/apple-touch-icon-144x144.png">
    <link rel="apple-touch-icon" sizes="152x152" href="/wikistatic/icons/apple-touch-icon-152x152.png">
    <link rel="apple-touch-icon" sizes="180x180" href="/wikistatic/icons/apple-touch-icon-180x180.png">
    <link rel="icon" type="image/png" href="/wikistatic/icons/favicon-32x32.png" sizes="32x32">
    <link rel="icon" type="image/png" href="/wikistatic/icons/android-chrome-192x192.png" sizes="192x192">
    <link rel="icon" type="image/png" href="/wikistatic/icons/favicon-96x96.png" sizes="96x96">
    <link rel="icon" type="image/png" href="/wikistatic/icons/favicon-16x16.png" sizes="16x16">
    <link rel="manifest" href="/wikistatic/icons/manifest.json">
    <link rel="shortcut icon" href="/wikistatic/icons/favicon.ico">
    <meta name="apple-mobile-web-app-title" content="Freifunk Kassel">
    <meta name="application-name" content="Freifunk Kassel">
    <meta name="msapplication-TileColor" content="#ffc40d">
    <meta name="msapplication-TileImage" content="/wikistatic/icons/mstile-144x144.png">
    <meta name="msapplication-config" content="/wikistatic/icons/browserconfig.xml">
    <meta name="theme-color" content="#ffffff">
    <script type="text/javascript" src="/wikistatic/ffks/js/jquery-2.1.4.min.js"></script>'''

    # when it looks acceptable
    theme_default = u'ffks'
    theme_force = True
