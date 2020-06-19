#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Main story.
"""
## path setting
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


def main(): # pragma: no cover
    w = World.create_world('君の声は真相に消ゆ')
    w.config.set_outline('声を探す')
    return w.run(
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

