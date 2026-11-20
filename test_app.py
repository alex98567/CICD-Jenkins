import app

def test_get_message_default():
    assert app.get_message() == "Hello, Jenkins!"

def test_get_message_custom():
    assert app.get_message("CI/CD") == "Hello, CI/CD!"

def test_main_output(capsys):
    app.main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Jenkins!"