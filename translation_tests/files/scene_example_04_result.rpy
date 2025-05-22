label day010405:
call calendar(3) from _call_calendar
$ calDate = calDate.replace(day=5, month=4, year=2004)

TempCharacter("[day_scene_example_04_scene_text[0]]") "[day_scene_example_04_scene_text[1]]"

scene dorm_A with Dissolve(2.0)
$ renpy.transition(dissolve)
show screen currentdate
