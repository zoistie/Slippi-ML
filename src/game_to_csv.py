import os
import pandas as pd
from peppi_py import read_slippi

def game_to_dataframe(game):
    rows = []
    if game.start.match == None:
        return pd.DataFrame(rows)
    lastframe = game.frames.id[-1].as_py()
    if lastframe < 1800:
        return pd.DataFrame(rows)
    if game.start.players[0].netplay.name == 'MinmayFan7':
        player = 0
        opponent = 1
    else:
        player = 1
        opponent = 0
    for frame in game.frames.id:
        frame_index = frame.as_py()
        row = {
            'match_id': game.start.match.id,
            'stage': game.start.stage,
            'player': game.start.players[player].netplay.name,
            'opponent': game.start.players[opponent].netplay.name,
            'player_char': game.start.players[player].character,
            'opponent_char': game.start.players[opponent].character,
            'frame_id': frame_index,
            'player_random_seed': game.frames.ports[player].leader.pre.random_seed[frame_index],
            'player_state': game.frames.ports[player].leader.pre.state[frame_index],
            'player_position_x': game.frames.ports[player].leader.pre.position.x[frame_index],
            'player_position_y': game.frames.ports[player].leader.pre.position.y[frame_index],
            'player_direction': game.frames.ports[player].leader.pre.direction[frame_index],
            'player_joystick_x': game.frames.ports[player].leader.pre.joystick.x[frame_index],
            'player_joystick_y': game.frames.ports[player].leader.pre.joystick.y[frame_index],
            'player_cstick_x': game.frames.ports[player].leader.pre.cstick.x[frame_index],
            'player_cstick_y': game.frames.ports[player].leader.pre.cstick.y[frame_index],
            'player_trigger_l': game.frames.ports[player].leader.pre.triggers_physical.l[frame_index],
            'player_trigger_r': game.frames.ports[player].leader.pre.triggers_physical.r[frame_index],
            'player_buttons': game.frames.ports[player].leader.pre.buttons[frame_index],
            'player_buttons_physical': game.frames.ports[player].leader.pre.buttons_physical[frame_index],
            'player_raw_analog_x': game.frames.ports[player].leader.pre.raw_analog_x[frame_index],
            'player_raw_analog_y': game.frames.ports[player].leader.pre.raw_analog_y[frame_index],
            'player_percent': game.frames.ports[player].leader.pre.percent[frame_index],
            'player_character': game.frames.ports[player].leader.post.character[frame_index],
            'player_shield': game.frames.ports[player].leader.post.shield[frame_index],
            'player_stocks': game.frames.ports[player].leader.post.stocks[frame_index],
            'player_animation_index': game.frames.ports[player].leader.post.animation_index[frame_index],
            'opponent_random_seed': game.frames.ports[opponent].leader.pre.random_seed[frame_index],
            'opponent_state': game.frames.ports[opponent].leader.pre.state[frame_index],
            'opponent_position_x': game.frames.ports[opponent].leader.pre.position.x[frame_index],
            'opponent_position_y': game.frames.ports[opponent].leader.pre.position.y[frame_index],
            'opponent_direction': game.frames.ports[opponent].leader.pre.direction[frame_index],
            'opponent_joystick_x': game.frames.ports[opponent].leader.pre.joystick.x[frame_index],
            'opponent_joystick_y': game.frames.ports[opponent].leader.pre.joystick.y[frame_index],
            'opponent_cstick_x': game.frames.ports[opponent].leader.pre.cstick.x[frame_index],
            'opponent_cstick_y': game.frames.ports[opponent].leader.pre.cstick.y[frame_index],
            'opponent_trigger_l': game.frames.ports[opponent].leader.pre.triggers_physical.l[frame_index],
            'opponent_trigger_r': game.frames.ports[opponent].leader.pre.triggers_physical.r[frame_index],
            'opponent_buttons': game.frames.ports[opponent].leader.pre.buttons[frame_index],
            'opponent_buttons_physical': game.frames.ports[opponent].leader.pre.buttons_physical[frame_index],
            'opponent_raw_analog_x': game.frames.ports[opponent].leader.pre.raw_analog_x[frame_index],
            'opponent_raw_analog_y': game.frames.ports[opponent].leader.pre.raw_analog_y[frame_index],
            'opponent_percent': game.frames.ports[opponent].leader.pre.percent[frame_index],
            'opponent_character': game.frames.ports[opponent].leader.post.character[frame_index],
            'opponent_shield': game.frames.ports[opponent].leader.post.shield[frame_index],
            'opponent_stocks': game.frames.ports[opponent].leader.post.stocks[frame_index],
            'opponent_animation_index': game.frames.ports[opponent].leader.post.animation_index[frame_index],
        }
        rows.append(row)
    return pd.DataFrame(rows)

# Main script to process all .slp files in a directory
data_dir = 'src/data'
output_csv = 'game_data.csv'
all_data = []

import random

for file_name in os.listdir(data_dir):
    if file_name.endswith('.slp'):
        file_path = os.path.join(data_dir, file_name).replace("\\", "/")
        print(file_path)  # Ensure forward slashes
        if random.randint(1, 6) == 1:  # Randomly include 1 in 6 files
            try:
                game = read_slippi(file_path)
                if game is not None:  # Skip if game is NoneType
                    df = game_to_dataframe(game)
                    all_data.append(df)
                else:
                    print(f"Skipping file: {file_name} (Invalid game object)")
            except Exception as e:
                print(f"Error processing file {file_name}: {e}")
        else:
            print(f"Skipping file: {file_name} (Not selected randomly)")


# Combine all dataframes and save to CSV
final_df = pd.concat(all_data, ignore_index=True)
final_df.to_csv(output_csv, index=False)

print(f"CSV file created: {output_csv}")