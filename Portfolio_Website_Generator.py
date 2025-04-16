def get_user_input(prompt):
    try:
        value = input(prompt)
        if not value.strip():
            raise ValueError("Input cannot be empty.")
        return value
    except Exception as e:
        print(f"Error: {e}")
        return get_user_input(prompt)

def generate_portfolio_html(name, bio, skills, email, github, linkedin):
    html_template = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>{name}'s Portfolio</title>
        <style>
            body {{
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to right, #2b5876, #4e4376);
                color: #ffffff;
            }}
            .container {{
                max-width: 900px;
                margin: 50px auto;
                padding: 20px;
                background: rgba(0,0,0,0.2);
                border-radius: 15px;
                box-shadow: 0 8px 20px rgba(0, 0, 0, 0.4);
            }}
            h1 {{
                text-align: center;
                font-size: 3em;
            }}
            .bio {{
                font-size: 1.2em;
                margin-bottom: 20px;
                text-align: center;
            }}
            .section {{
                margin-bottom: 30px;
            }}
            .skills ul {{
                list-style: none;
                padding: 0;
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
            }}
            .skills li {{
                background: #ffffff20;
                margin: 10px;
                padding: 10px 15px;
                border-radius: 20px;
            }}
            .contact a {{
                color: #ffc107;
                text-decoration: none;
                display: block;
                margin: 10px 0;
                text-align: center;
                font-size: 1.1em;
            }}
            footer {{
                text-align: center;
                margin-top: 40px;
                font-size: 0.9em;
                color: #ccc;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{name}</h1>
            <p class="bio">{bio}</p>
            <div class="section skills">
                <center><h2>Skills</h2></center>
                <ul>
                    {''.join(f'<li>{skill.strip()}</li>' for skill in skills.split(','))}
                </ul>
            </div>
            <div class="section contact">
                <center><h2>Contact</h2></center>
                <a href="mailto:{email}">📧 {email}</a>
                <a href="{github}" target="_blank">🐱 GitHub</a>
                <a href="{linkedin}" target="_blank">💼 LinkedIn</a>
            </div>
        </div>
        <footer>
            <p>Generated with ❤️ using Python</p>
        </footer>
    </body>
    </html>
    """
    return html_template

def main():
    print("🎨 Welcome to the Portfolio Website Generator 🎨")

    try:
        name = get_user_input("Enter your full name: ")
        bio = get_user_input("Enter a short bio about yourself: ")
        skills = get_user_input("Enter your skills (comma-separated): ")
        email = get_user_input("Enter your email address: ")
        github = get_user_input("Enter your GitHub URL: ")
        linkedin = get_user_input("Enter your LinkedIn URL: ")

        html_content = generate_portfolio_html(name, bio, skills, email, github, linkedin)

        filename = "portfolio.html"
        with open(filename, "w", encoding="utf-8") as file:
            file.write(html_content)
        print(f"\n✅ Portfolio generated successfully! Open '{filename}' to view it.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()