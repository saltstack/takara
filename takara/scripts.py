#!/usr/bin/env python3
import pop.hub

def start():
    hub = pop.hub.Hub()
    hub.pop.sub.add(dyne_name='takara')
    hub.takara.init.cli()
