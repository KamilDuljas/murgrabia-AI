from openai import OpenAI


def send_request(key):
    try:
        client = OpenAI(api_key=key)
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are obedient assistant."},
                {"role": "user", "content": "bedziesz pracowal dla swojego pana."},
            ],
        )
        print(messages[1]["content"])
        print(completion.choices[0].message)
    except Exception:
        print("Twoj klucz nie pasuje, precz!")
