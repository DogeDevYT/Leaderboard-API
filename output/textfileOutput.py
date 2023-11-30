import os
def write_to_text_file(leaderboard_data):
    output_path = os.path.join("output", "leaderboard.txt")

    with open(output_path, "w") as output_file:
        for rank, name in leaderboard_data.items():
            output_file.write(f"{rank}:{name}\n")