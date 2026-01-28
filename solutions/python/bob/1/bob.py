def response(hey_bob):
    message = hey_bob.strip()

    if not message:
        return 'Fine. Be that way!'

    is_shouting = message.isupper()
    is_question = message.endswith('?')

    if is_shouting and is_question:
        return "Calm down, I know what I'm doing!"
    elif is_question:
        return 'Sure.'
    elif is_shouting:
        return 'Whoa, chill out!'
    else:
        return 'Whatever.'