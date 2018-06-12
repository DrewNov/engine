import sys,pygame,time,math

pygame.init()

screen = pygame.display.set_mode((800,600))

c = 200

cube1 = [[-c/2,-c/2,-c/2],[c/2,-c/2,-c/2],[c/2,c/2,-c/2],[-c/2,c/2,-c/2],[-c/2,-c/2,+c/2],[c/2,-c/2,+c/2],[c/2,c/2,+c/2],[-c/2,c/2,+c/2]]
cube2 = [[0,0,400],[c/2,0,400],[c/2,c/2,400],[0,c/2,400],[0,0,400+c/2],[c/2,0,400+c/2],[c/2,c/2,400+c/2],[0,c/2,400+c/2]]

cam_z_1 = 500

k = 0.00125

phi = 1/600


def draw_cube(cube,cam_z):
        for i in range(0,8):
                if i == 3 or i == 7:
                        pygame.draw.line(screen,(255,0,0),(300 + cube[i][0]/(k*(cube[i][2]+cam_z)),300 + cube[i][1]/(k*(cube[i][2]+cam_z))),(300 + cube[i-3][0]/(k*(cube[i-3][2]+cam_z)),300 + cube[i-3][1]/(k*(cube[i-3][2]+cam_z))))

                else:
                        pygame.draw.line(screen,(0,255,0),(300 + cube[i][0]/(k*(cube[i][2]+cam_z)),300 + cube[i][1]/(k*(cube[i][2]+cam_z))),(300 + cube[i+1][0]/(k*(cube[i+1][2]+cam_z)),300 + cube[i+1][1]/(k*(cube[i+1][2]+cam_z))))

                        if i <= 3:
                                pygame.draw.line(screen,(0,0,255),(300 + cube[i][0]/(k*(cube[i][2]+cam_z)),300 + cube[i][1]/(k*(cube[i][2]+cam_z))),(300 + cube[i+4][0]/(k*(cube[i+4][2]+cam_z)),300 + cube[i+4][1]/(k*(cube[i+4][2]+cam_z))))

                #Because of 1st if statement we need to do additional drawing
                pygame.draw.line(screen,(255,255,255),(300 + cube[3][0]/(k*(cube[3][2]+cam_z)),300 + cube[3][1]/(k*(cube[3][2]+cam_z))),(300 + cube[7][0]/(k*(cube[7][2]+cam_z)),300 + cube[7][1]/(k*(cube[7][2]+cam_z))))

        pygame.display.update()


def cube_coord_change(cube,cam_z):
        pressed = pygame.key.get_pressed()            
        if pressed[pygame.K_d]:
                for i in cube:
                        i[0] = i[0]*math.cos(phi)+i[2]*math.sin(phi)
                        i[2] = i[2]*math.cos(phi)-i[0]*math.sin(phi)
        elif pressed[pygame.K_a]:
                for i in cube:
                        i[0] = i[0]*math.cos(-phi)+i[2]*math.sin(-phi)
                        i[2] = i[2]*math.cos(-phi)-i[0]*math.sin(-phi)
        elif pressed[pygame.K_w]:
                for i in cube:
                        i[1] = i[1]*math.cos(phi)+i[2]*math.sin(phi)
                        i[2] = i[2]*math.cos(phi)-i[1]*math.sin(phi)
        elif pressed[pygame.K_s]:
                for i in cube:
                        i[1] = i[1]*math.cos(-phi)+i[2]*math.sin(-phi)
                        i[2] = i[2]*math.cos(-phi)-i[1]*math.sin(-phi)
        elif pressed[pygame.K_LEFT]:
                for i in cube:
                        i[0] += 1
        elif pressed[pygame.K_RIGHT]:
                for i in cube:
                        i[0] -= 1
        elif pressed[pygame.K_UP]:
                for i in cube:
                        cam_z -= 0.1
        elif pressed[pygame.K_DOWN]:
                for i in cube:
                        cam_z += 0.1 

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pass
        
        return cam_z


def move_cube(cube,cam_z):
        while True:
                draw_cube(cube,cam_z)
                
                cam_z = cube_coord_change(cube,cam_z)

                screen.fill((0,0,0)) 


move_cube(cube1,cam_z_1)

