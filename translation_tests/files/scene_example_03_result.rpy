label day010405:
call calendar(3) from _call_calendar
$ calDate = calDate.replace(day=5, month=4, year=2004)

red @thinking "[day_scene_example_03_scene_text[0].to_scene_text(vars())]"
$ BecomeNamed("Hilbert")
hilbert @thinking "[day_scene_example_03_scene_text[1].to_scene_text(vars())]"
red frownmouth "[day_scene_example_03_scene_text[2].to_scene_text(vars())]"

scene dorm_A with Dissolve(2.0)
$ renpy.transition(dissolve)
show screen currentdate
