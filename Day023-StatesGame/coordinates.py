import turtle

screen = turtle.Screen()
screen.title("India Coordinate Finder")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_names = [
    "Andhra Pradesh",
    "Arunachal Pradesh",
    "Assam",
    "Bihar",
    "Chhattisgarh",
    "Goa",
    "Gujarat",
    "Haryana",
    "Himachal Pradesh",
    "Jharkhand",
    "Karnataka",
    "Kerala",
    "Madhya Pradesh",
    "Maharashtra",
    "Manipur",
    "Meghalaya",
    "Mizoram",
    "Nagaland",
    "Odisha",
    "Punjab",
    "Rajasthan",
    "Sikkim",
    "Tamil Nadu",
    "Telangana",
    "Tripura",
    "Uttar Pradesh",
    "Uttarakhand",
    "West Bengal"
]
index = 0

def get_coordinates(x, y):
    global index
    if index < len(state_names):
        state = state_names[index]
        print(f"{state},{int(x)},{int(y)}")
        index += 1

screen.onscreenclick(get_coordinates)
turtle.mainloop()