label day010405:
call calendar(3) from _call_calendar
$ calDate = calDate.replace(day=5, month=4, year=2004)

ethan @sad "[day_scene_example_05_scene_text[0]]"
calem @closedbrow talking2mouth "[day_scene_example_05_scene_text[1]]"
red @wince talking2mouth "[day_scene_example_05_scene_text[2]]"
brendan @happy "[day_scene_example_05_scene_text[3]]"
roxanne @happy "[day_scene_example_05_scene_text[4]]"
wally @sadbrow surprised2mouth sweat "[day_scene_example_05_scene_text[5]]"
grusha @wince "[day_scene_example_05_scene_text[6]]"
flannery "[day_scene_example_05_scene_text[7]]"
whitney "[day_scene_example_05_scene_text[8]]"
serena @happy "[day_scene_example_05_scene_text[9]]"

scene dorm_A with Dissolve(2.0)
$ renpy.transition(dissolve)
show screen currentdate
