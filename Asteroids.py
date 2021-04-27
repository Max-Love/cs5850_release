from Engine import *
import time

frameCap = 60

e = Engine(frameCap, 1080, 720, 1080, 720, '', './Resources/Images/bgnd.bmp', 1.0) #./BGM.wav
e.startUp()




to1 = e.createTextGameObject(0, [], 340, 320, 400, 80, './Resources/Fonts/DejaVuSansMono.ttf', 25)
to1.setText("START GAME")

while True:
    e.beginLoop()
    i = e.getInput()
    if i == "QUIT":
        break
    if i != "none":
        break
    e.updateWorld(1)
    e.renderWorld()
    
e.deleteGameObject(to1)




playerSprite = SpriteComponent('./Resources/Images/asteroids.png', 410, 405, 30, 28, 1, 1)
gravComp = GravityComponent()
#collComp = CollisionComponent()
soundComp = SoundComponent()
#transComp = TransformationComponent([ObjectType.TILE])
transComp = ProperTransformComponent([ObjectType.TILE])
enemySprite = SpriteComponent('./Resources/Images/asteroids.png', 370, 474, 30, 30, 1, 1)

soundComp.addCollisionSound(ObjectType.WALL, './Resources/Sounds/short-sound.wav')

player = e.createDynamicGameObject(1, ObjectType.PLAYER, 15.0, [playerSprite, transComp, soundComp], 450.0, 200.0, 30.0, 28.0, 0.0, 0.0, 0.0, 0.0) #collComp
timeText = e.createTextGameObject(2, [], 0, 0, 80, 100, './Resources/Fonts/DejaVuSansMono.ttf', 20)
enemy1 = e.createDynamicGameObject(3, ObjectType.ENEMY, 0.0, [enemySprite, gravComp, transComp], 50.0, 350.0, 50.0, 50.0, 0.0, 1.0, 0.0, 0.0)
enemy2 = e.createDynamicGameObject(4, ObjectType.ENEMY, 0.0, [enemySprite, gravComp, transComp], 650.0, 350.0, 50.0, 50.0, 0.0, 0.0, 0.0, 0.0)
enemy3 = e.createDynamicGameObject(5, ObjectType.ENEMY, 0.0, [enemySprite, gravComp, transComp], 700.0, 600.0, 50.0, 50.0, -1.0, -0.1, 0.0, 0.0)
enemy4 = e.createDynamicGameObject(6, ObjectType.ENEMY, 0.0, [enemySprite, gravComp, transComp], 100.0, 650.0, 50.0, 50.0, 0.5, 1.0, 0.0, 0.0)
enemy5 = e.createDynamicGameObject(7, ObjectType.ENEMY, 0.0, [enemySprite, gravComp, transComp], -100.0, 650.0, 50.0, 50.0, 1.0, 0.0, 0.0, 0.0)
enemy6 = e.createDynamicGameObject(12, ObjectType.ENEMY, 0.0, [enemySprite, gravComp, transComp], 200.0, 950.0, 50.0, 50.0, 0.0, 0.0, 0.0, 0.0)
enemy7 = e.createDynamicGameObject(13, ObjectType.ENEMY, 0.0, [enemySprite, gravComp, transComp], -100.0, -250.0, 50.0, 50.0, 0.0, 1.0, 0.0, 0.0)

loopcount = 0
seconds = 0;
won = True

timeText.setText(str(seconds));

while True:
    e.beginLoop()
    loopcount = loopcount + 1

    if loopcount == frameCap:
        seconds = seconds+1
        timeText.setText(str(seconds));
        loopcount = 0

    if seconds == 30:
        break

    if len(player.getCollisions()) != 0:
        won = False
        break

    i = e.getInput()
    if i == "QUIT":
        break
    if i != "none":
        print(i)
        sp = i.split("_")
        if sp[0] == "DOWN":
            if sp[1] == "LEFT":
                player.setVelocity(-4, 0)
            if sp[1] == "RIGHT":
                player.setVelocity(4, 0)
            if sp[1] == "UP":
                player.setVelocity(0, -4)
            if sp[1] == "DOWN":
                player.setVelocity(0, 4)
        else:
            player.setVelocity(0, 0)
    e.updateWorld(1)
    e.renderWorld()
    
e.deleteGameObject(player)
e.deleteGameObject(enemy1)
e.deleteGameObject(enemy2)
e.deleteGameObject(enemy3)
e.deleteGameObject(enemy4)
e.deleteGameObject(enemy5)
e.deleteGameObject(enemy6)
e.deleteGameObject(enemy7)
e.deleteGameObject(timeText)



to1 = e.createTextGameObject(10, [], 340, 320, 400, 80, './Resources/Fonts/DejaVuSansMono.ttf', 25)
if won:
    to1.setText("YOU WON!")
else:
    to1.setText("YOU LOST!")

while True:
    e.beginLoop()
    i = e.getInput()
    if i != "none":
        break
    e.updateWorld(1)
    e.renderWorld()
    
e.deleteGameObject(to1)

e.shutDown()
