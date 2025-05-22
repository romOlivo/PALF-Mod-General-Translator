label day010405:
call calendar(3) from _call_calendar
$ calDate = calDate.replace(day=5, month=4, year=2004)

    "Option 1":
        red @happy "Say option 1"
        serena @happy "Some great response"

    "Option 2":
        red @happy "Say option 2"
        serena @happy "Some awfully response"

scene dorm_A with Dissolve(2.0)
$ renpy.transition(dissolve)
show screen currentdate