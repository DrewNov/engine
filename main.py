import sys,pygame,math

resolution = (800,600)
a,b,c = 100,400,300
cam_z_init = 500
k = 0.00125
phi = 1/600
cp = math.cos(phi)
sp = math.sin(phi)

BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

cube1 = [[-a,-a,-a],[a,-a,-a],[a,a,-a],[-a,a,-a],[-a,-a,a],[a,-a,a],[a,a,a],[-a,a,a]]
cube2 = [[0,0,b],[a,0,b],[a,a,b],[0,a,b],[0,0,a+b],[a,0,a+b],[a,a,b+a],[0,a,a+b]]

pygame.init()
screen = pygame.display.set_mode(resolution)


def draw_cube(cube,cam_z):
        for i in range(8):
                if i == 3 or i == 7:
                        pygame.draw.line(screen, RED,
                            (c + cube[i][0]/(k*(cube[i][2]+cam_z)), c + cube[i][1]/(k*(cube[i][2]+cam_z))),
                            (c + cube[i-3][0]/(k*(cube[i-3][2]+cam_z)), c + cube[i-3][1]/(k*(cube[i-3][2]+cam_z))))
                else:
                        pygame.draw.line(screen, GREEN,
                            (c + cube[i][0]/(k*(cube[i][2]+cam_z)), c + cube[i][1]/(k*(cube[i][2]+cam_z))),
                            (c + cube[i+1][0]/(k*(cube[i+1][2]+cam_z)), c + cube[i+1][1]/(k*(cube[i+1][2]+cam_z))))

                        if i <= 3:
                                pygame.draw.line(screen, BLUE,
                                    (c + cube[i][0]/(k*(cube[i][2]+cam_z)), c + cube[i][1]/(k*(cube[i][2]+cam_z))),
                                    (c + cube[i+4][0]/(k*(cube[i+4][2]+cam_z)), c + cube[i+4][1]/(k*(cube[i+4][2]+cam_z))))

        #Because of 1st 'if statement' we need to do additional drawing
        pygame.draw.line(screen, WHITE,
            (c + cube[3][0]/(k*(cube[3][2]+cam_z)), c + cube[3][1]/(k*(cube[3][2]+cam_z))),
            (c + cube[7][0]/(k*(cube[7][2]+cam_z)), c + cube[7][1]/(k*(cube[7][2]+cam_z))))

        pygame.display.update()


def cube_coord_change(cube,cam_z):
        pressed = pygame.key.get_pressed()   

        if pressed[pygame.K_a]:
                for v in cube:
                        v[0] = v[0]*cp + v[2]*sp
                        v[2] = v[2]*cp - v[0]*sp
        elif pressed[pygame.K_d]:
                for v in cube:
                        v[0] = v[0]*cp - v[2]*sp
                        v[2] = v[2]*cp + v[0]*sp
        elif pressed[pygame.K_w]:
                for v in cube:
                        v[1] = v[1]*cp + v[2]*sp
                        v[2] = v[2]*cp - v[1]*sp
        elif pressed[pygame.K_s]:
                for v in cube:
                        v[1] = v[1]*cp - v[2]*sp
                        v[2] = v[2]*cp + v[1]*sp

        elif pressed[pygame.K_LEFT]:
                for v in cube:
                        v[0] -= 1
        elif pressed[pygame.K_RIGHT]:
                for v in cube:
                        v[0] += 1

        elif pressed[pygame.K_UP]:
                        cam_z -= 1
        elif pressed[pygame.K_DOWN]:
                        cam_z += 1

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
        
        return cam_z


def move_cube(cube,cam_z):
        while True:
                draw_cube(cube,cam_z)
                cam_z = cube_coord_change(cube,cam_z)
                screen.fill(BLACK)


move_cube(cube1,cam_z_init)
