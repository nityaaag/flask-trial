from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Student Portal</title>
        <style>
            * {
                box-sizing: border-box;
                margin: 0;
                padding: 0;
            }

            body {
                font-family: Arial, sans-serif;
                background: #f4f3f8;
                color: #222;
            }

            .navbar {
                background: #17131f;
                color: white;
                padding: 20px 8%;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }

            .navbar h2 {
                color: #ffffff;
            }

            .navbar span {
                color: #c9b8e8;
                font-size: 14px;
            }

            .hero {
                background: linear-gradient(135deg, #6f4aa8, #9b7bc4);
                color: white;
                text-align: center;
                padding: 70px 20px;
            }

            .hero h1 {
                font-size: 42px;
                margin-bottom: 15px;
            }

            .hero p {
                font-size: 18px;
                opacity: 0.9;
            }

            .container {
                max-width: 1000px;
                margin: 45px auto;
                padding: 0 20px;
            }

            .section-title {
                text-align: center;
                margin-bottom: 30px;
            }

            .section-title h2 {
                font-size: 28px;
                color: #292331;
            }

            .section-title p {
                color: #777;
                margin-top: 8px;
            }

            .cards {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 22px;
            }

            .card {
                background: white;
                padding: 30px 25px;
                border-radius: 14px;
                text-align: center;
                box-shadow: 0 5px 18px rgba(0, 0, 0, 0.08);
                transition: 0.3s;
            }

            .card:hover {
                transform: translateY(-6px);
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.12);
            }

            .icon {
                font-size: 35px;
                margin-bottom: 15px;
            }

            .card h3 {
                margin-bottom: 10px;
                color: #292331;
            }

            .card p {
                color: #777;
                font-size: 14px;
                line-height: 1.6;
                margin-bottom: 20px;
            }

            .btn {
                display: inline-block;
                text-decoration: none;
                background: #6f4aa8;
                color: white;
                padding: 10px 22px;
                border-radius: 8px;
                font-size: 14px;
                transition: 0.3s;
            }

            .btn:hover {
                background: #543582;
            }

            footer {
                background: #17131f;
                color: #aaa;
                text-align: center;
                padding: 20px;
                margin-top: 50px;
                font-size: 14px;
            }

            @media (max-width: 700px) {
                .cards {
                    grid-template-columns: 1fr;
                }

                .hero h1 {
                    font-size: 32px;
                }

                .navbar {
                    padding: 18px 5%;
                }
            }
        </style>
    </head>

    <body>

        <nav class="navbar">
            <h2>Student Portal</h2>
            <span>Academic Information System</span>
        </nav>

        <section class="hero">
            <h1>Welcome to Student Portal</h1>
            <p>Access important academic information in one place.</p>
        </section>

        <main class="container">

            <div class="section-title">
                <h2>Explore Student Portal</h2>
                <p>Select an option to continue</p>
            </div>

            <div class="cards">

                <div class="card">
                    <div class="icon">👤</div>
                    <h3>About</h3>
                    <p>
                        Learn more about the Student Portal and its purpose.
                    </p>
                    <a href="/about" class="btn">View About</a>
                </div>

                <div class="card">
                    <div class="icon">📚</div>
                    <h3>Courses</h3>
                    <p>
                        Explore the courses available for students.
                    </p>
                    <a href="/courses" class="btn">View Courses</a>
                </div>

                <div class="card">
                    <div class="icon">📧</div>
                    <h3>Contact</h3>
                    <p>
                        Get in touch with the Student Portal support team.
                    </p>
                    <a href="/contact" class="btn">Contact Us</a>
                </div>

            </div>

        </main>

        <footer>
            © 2026 Student Portal | Flask Web Application
        </footer>

    </body>
    </html>
    """


@app.route("/about")
def about():
    return """
    <h1>About Student Portal</h1>
    <p>This portal provides useful academic information for students.</p>
    <br>
    <a href="/">← Back to Home</a>
    """


@app.route("/courses")
def courses():
    return """
    <h1>Available Courses</h1>
    <ul>
        <li>BCA</li>
        <li>BSc</li>
        <li>MCA</li>
        <li>MSc</li>
    </ul>
    <br>
    <a href="/">← Back to Home</a>
    """


@app.route("/contact")
def contact():
    return """
    <h1>Contact Us</h1>
    <p>Email: cs@example.com</p>
    <br>
    <a href="/">← Back to Home</a>
    """


if __name__ == "__main__":
    app.run(debug=True)