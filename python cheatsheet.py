# #################### PYAUTOGUI controls#################





# pyautogui.press(keys)

# for keyboard inputs

# pyautogui.keyDown(key_name)
# pyautogui.keyUp(key_name)

# for timing





# pyautogui.moveTo(x,y,duration=num_seconds)

# for mouse movement (approx 0.2-0.4s)




# move mouse then click ========> 
# pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')


################################## Image recognition with  PYTHON-IMAGESEARCH ###############
# pos = imagesearch("github.png")
# if pos[0] != -1:
#     print("position : ", pos[0], pos[1])
#     pyautogui.moveTo(pos[0], pos[1])
# else:
#     print("image not found")





# If we right click and target ==> harvest_icon.png <=== appears then do things 

# pyautogui.click(button="right")
#     time.sleep(r(0.4, 0.2)) # the r function simply returns 0.4 + 0.2 * random.random()
#     presence = imagesearch("harvest_icon.png")
#     if (presence[0] == -1):
#       # do things


# Defining Imagesearch area to be resolution agnostic

# pos = imagesearcharea("github.png", 0, 0, 800, 600)
# if pos[0] != -1:
#     print("position : ", pos[0], pos[1])
#     pyautogui.moveTo(pos[0], pos[1])
# else:
#     print("image not found")



# Add event listener for when an image pops

# pos = imagesearch_loop("github.png", 0.5)
# print("image found ", pos[0], pos[1])


# add event listener for a region


# 


#  Run imagesearch grabber several times for optimization

# time1 = time.clock()
# im = region_grabber((0, 0, 800, 600))
# for i in range(10):
#     imagesearcharea("github.png", 0, 0, 800, 600, 0.8, im)
#     imagesearcharea("panda.png", 0, 0, 800, 600, 0.8, im)
# print(str(time.clock() - time1) + " seconds (optimized)")
