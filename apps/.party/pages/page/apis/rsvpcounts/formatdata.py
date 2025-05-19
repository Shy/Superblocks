

output = {"attending": "0", "maybe": "0", None: "0", "not_attending": "0"}


for item in getCounts.output:
    output[item['rsvp']] = str(item['rsvp_status'])
    
if getPlusOne.output[0].plus != "0":
    output["attending"] += f'+{getPlusOne.output[0].plus}'

return output