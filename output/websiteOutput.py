import os.path


def _generate_leaderboard_html(leaderboard):
    # Create the HTML content for the leaderboard
    leaderboard_html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Leaderboard</title>
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container">
            <h1>Leaderboard</h1>
            <table class="table table-striped">
                <thead class="thead-dark">
                    <tr>
                        <th scope="col">Rank</th>
                        <th scope="col">Name</th>
                    </tr>
                </thead>
                <tbody>
    """

    # Iterate through the leaderboard data to create table rows
    for rank, name in leaderboard.items():
        leaderboard_html += f"""
                    <tr>
                        <td>{rank}</td>
                        <td>{name}</td>
                    </tr>
        """

    # Finish the HTML content
    leaderboard_html += """
                </tbody>
            </table>
        </div>

        <!-- Bootstrap JS and jQuery (optional, for Bootstrap components that require JS) -->
        <!-- Make sure to include jQuery before Bootstrap's JS -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    </body>
    </html>
    """

    return leaderboard_html

def write_leaderboard_website(leaderboard_data):
    html = _generate_leaderboard_html(leaderboard_data)
    output_path = os.path.join("output", "leaderboard.html")

    with open(output_path, "w") as output_file:
        output_file.write(html)