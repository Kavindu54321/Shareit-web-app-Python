# Shareit-web-app-Python


# Installation :arrow_down:

### You will need to download python this project

- [python](https://www.python.org/downloads/)

#### Make sure you have the latest version of python on your computer.

```
python --version
```

## <br />

# Getting Started :python app:

### Clone the repo


```
git clone https://github.com/<YOUR GITHUB USERNAME>/Shareit-web-app-Python.git

cd Shareit-web-app-Python
```

### Install packages from the root directory

```bash
python install

```

Then, run the development server:

```bash
python app.py

```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) with your browser to see the result.

---

# Usage :joystick:

Goto [emailjs.com](https://www.emailjs.com/) and create a new account for the mail sending. In free trial you will get 200 mail per month. After setup `emailjs` account, Please create a new `.env` file from `.env.example` file.

Eg:

```env
NEXT_PUBLIC_EMAILJS_SERVICE_ID =
NEXT_PUBLIC_EMAILJS_TEMPLATE_ID =
NEXT_PUBLIC_EMAILJS_PUBLIC_KEY =
NEXT_PUBLIC_GTM = # For site analytics
NEXT_PUBLIC_APP_URL = "http://127.0.0.1:5000"
NEXT_PUBLIC_RECAPTCHA_SECRET_KEY = # For captcha verification on contact form
NEXT_PUBLIC_RECAPTCHA_SITE_KEY =
```

