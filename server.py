def get_info():
    musicians = [
        "Miles Davis",
        "Louis Armstrong",
        "John Coltrane",
        "Charles Mingus",
        "Thelonious Monk"
    ]
    newline = "\n"

    # funny formatting so the HTML looks right
    return f"""<ol>
{newline.join(f"    <li>{musician}</li>" for musician in musicians)}
</ol>"""

def set_info(first_name, last_name):
    return f"""<div>
    <p>{first_name} {last_name}</p>
</div>"""

# allow use of code as a module (standard practice)
if __name__ == '__main__':
    print("First function call:")
    print(get_info())
    print("\nSecond function call:")
    print(set_info('Miles', 'Davis'))