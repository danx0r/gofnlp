def put_on(subject, object):
    pass

def on_top_of(sub):
    pass

def what_is(sub, obj):
    pass

def that_is(sub, obj):
    pass

def the(sub):
    pass

def red(sub):
    pass

def blue(sub):
    pass

cube = None
table = None
color = None

#put the red cube on the table
put_on(the(red(cube)), the(table))

#put the blue cube on the red cube
put_on(the(blue(cube)), the(red(cube)))

#what color is the cube that is on top of the red cube?
what_is(
    color,
    that_is(
        the(cube),
        on_top_of(
            the(
                red(cube)
            )
        )
    )
)

"""
                                                     ?
  .--------------------------------------------------'
what-------is
       |------------------.
     color             that-is
                ,----------'-------.
              the               on-op-of
               '--cube              '-----.
                                         the
                                          '---.
                                             red
                                              '---.
                                                 cube

"""
