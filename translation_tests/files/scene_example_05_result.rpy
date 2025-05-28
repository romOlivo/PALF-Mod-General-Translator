label day010405:
call calendar(3) from _call_calendar
$ calDate = calDate.replace(day=5, month=4, year=2004)

ethan @sad "[day_scene_example_05_scene_text[0].to_scene_text(vars())]"
calem @closedbrow talking2mouth "[day_scene_example_05_scene_text[1].to_scene_text(vars())]"
red @wince talking2mouth "[day_scene_example_05_scene_text[2].to_scene_text(vars())]"
brendan @happy "[day_scene_example_05_scene_text[3].to_scene_text(vars())]"
roxanne @happy "[day_scene_example_05_scene_text[4].to_scene_text(vars())]"
wally @sadbrow surprised2mouth sweat "[day_scene_example_05_scene_text[5].to_scene_text(vars())]"
grusha @wince "[day_scene_example_05_scene_text[6].to_scene_text(vars())]"
flannery "[day_scene_example_05_scene_text[7].to_scene_text(vars())]"
whitney "[day_scene_example_05_scene_text[8].to_scene_text(vars())]"
serena @happy "[day_scene_example_05_scene_text[9].to_scene_text(vars())]"

scene dorm_A with Dissolve(2.0)
$ renpy.transition(dissolve)
show screen currentdate
