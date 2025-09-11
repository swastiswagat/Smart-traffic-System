import pygame
import sys
import re
import subprocess
pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Smart Traffic System Simulation")
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
GRAY = (100, 100, 100)
font = pygame.font.SysFont('Arial', 20)
large_font = pygame.font.SysFont('Arial', 30, bold=True)

current_green = "NORTH"
switch_time = 0
green_duration = 100
vehicle_counts = {"NORTH": 0, "SOUTH": 0, "EAST": 0, "WEST": 0}
ai_process = subprocess.Popen(['python', 'main.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, bufsize=1)

def parse_ai_output(line):
    """Parse the output from the AI script"""
    global vehicle_counts
    match = re.search(r"NORTH:(\d+), SOUTH:(\d+), EAST:(\d+), WEST:(\d+)", line)
    if match:
        vehicle_counts["NORTH"] = int(match.group(1))
        vehicle_counts["SOUTH"] = int(match.group(2))
        vehicle_counts["EAST"] = int(match.group(3))
        vehicle_counts["WEST"] = int(match.group(4))
        return True
    return False

def decide_traffic_light():
    """A simple algorithm to decide which light should be green."""
    global current_green, green_duration, switch_time
    total_vehicles = sum(vehicle_counts.values())
    if total_vehicles == 0:
        return
    if vehicle_counts[current_green] > 2:
        green_duration = 100 + (vehicle_counts[current_green] * 20)
        return
    next_green = max(vehicle_counts, key=vehicle_counts.get)
    if vehicle_counts[next_green] > 0:
        current_green = next_green
        green_duration = 50 + (vehicle_counts[next_green] * 30)
        switch_time = pygame.time.get_ticks()

running = True
while running:
    current_time = pygame.time.get_ticks()

    line = ai_process.stdout.readline()
    if line:
        print("AI Output:", line.strip())
        parse_ai_output(line)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            ai_process.terminate()

    decide_traffic_light()

    if current_time - switch_time > green_duration:
        switch_time = current_time
    screen.fill(BLACK)
    pygame.draw.rect(screen, GRAY, (0, 250, width, 100))
    pygame.draw.rect(screen, GRAY, (350, 0, 100, height))
    light_positions = {"NORTH": (400, 150), "SOUTH": (400, 450), "EAST": (650, 300), "WEST": (150, 300)}
    for direction, pos in light_positions.items():
        color = GREEN if direction == current_green else RED
        pygame.draw.circle(screen, color, pos, 25)
    y_offset = 50
    for direction, count in vehicle_counts.items():
        text_color = GREEN if direction == current_green else WHITE
        count_text = large_font.render(f'{direction}: {count} vehicles', True, text_color)
        screen.blit(count_text, (50, y_offset))
        y_offset += 50

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()