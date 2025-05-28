label day010405:
call calendar(3) from _call_calendar
$ calDate = calDate.replace(day=5, month=4, year=2004)

    "[day_scene_example_06_scene_text[0].to_scene_text(vars())]":
        red @happy "[day_scene_example_06_scene_text[1].to_scene_text(vars())]"
        serena @happy "[day_scene_example_06_scene_text[2].to_scene_text(vars())]"

    "[day_scene_example_06_scene_text[3].to_scene_text(vars())]":
        red @happy "[day_scene_example_06_scene_text[4].to_scene_text(vars())]"
        serena @happy "[day_scene_example_06_scene_text[5].to_scene_text(vars())]"

scene dorm_A with Dissolve(2.0)
$ renpy.transition(dissolve)
show screen currentdate
