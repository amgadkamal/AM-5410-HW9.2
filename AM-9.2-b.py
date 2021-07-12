# It was done for class using resources provided by the instructor.
import pygame, math
from pygame_button import Button
pygame.init() # prepare the pygame module for use
global done
global NumberOfclicks

# Create a new surface and window.
surface_size = 1024
main_surface = pygame.display.set_mode((surface_size,surface_size))
my_clock = pygame.time.Clock()

def draw_tree(order, theta, sz, posn, heading, color=(0,0,0), depth=0):
   trunk_ratio= 0.29       # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos(heading)
   delta_y = trunk * math.sin(heading)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   pygame.draw.line(main_surface, color, posn, newpos)

   if order > 0:   # Draw another layer of subtrees
      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      RED = (255, 0, 0)
      BLUE = (0, 0, 255)
      GREEN = (0, 255, 0)
      BLACK = (0, 0, 0)
      ORANGE = (255, 180, 0)
      YELLOW=(255,255,0)
      OLIVE=(128,128,0)
      GRAY=(128,128,128)

      def colors(i):#colors for the tree with each depth
          switcher = {
              1:GRAY,
              2:ORANGE,
              3: BLACK,
              4: GREEN,
              5: OLIVE,
              6: BLUE,
              7: RED,
              8: YELLOW,
              0:RED
          }
          return switcher.get(i, "Invalid color")

      color1 =colors(depth)
      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(order-1, theta, newsz, newpos, heading-theta, color1, depth+1)
      draw_tree(order-1, theta, newsz, newpos, heading+theta, color1, depth+1)


def gameloop(button,button2):
  theta= 0
  while not done:
        # Handle evente from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;
        button.check_event(ev)

        # Updates - change the angle
        theta += 0.01
        # Draw everything
        main_surface.fill((255, 255, 0))
        draw_tree(9, theta, surface_size*0.9, (surface_size//2, surface_size-50), -math.pi/2)
        button.update(main_surface)
        button2.update(main_surface)
        pygame.display.flip()
        my_clock.tick(120)

RED=(255,0,0)
BLUE=(0,0,255)
GREEN=(0,255,0)
BLACK=(0,0,0)
ORANGE=(255,180,0)

BUTTON_STYLE={
    "hover_color":BLUE,
    "clicked_color":GREEN,
    "clicked_font_color":BLACK,
    "hover_font_color":ORANGE}

done=False
def end():
    global done
    done=True
def paused():
    global NumberOfclicks
    if NumberOfclicks==1:
       global done
       done=False
    NumberOfclicks = NumberOfclicks + 1

def main():
    button = Button((0, 0, 200, 50), RED, end, text='Quit', **BUTTON_STYLE)#change name for the first button
    button2 = Button((0, 60, 200, 50), RED, paused, text='Play/Pause', **BUTTON_STYLE)#make new button
    gameloop(button,button2)
    pygame.quit()
if __name__ == '__main__':
    main()

