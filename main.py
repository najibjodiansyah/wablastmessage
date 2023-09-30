import pywhatkit

def prepare_message(nama):
    message =f"Assalamualaikum Wr.Wb.\n\n"\
        f"Bismillahirahmanirahim\n\n"\
        f"Kepada Yth. {nama} dan partner\n\n"\
        f"dengan tanpa mengurangi rasa hormat, perkenankan kami untuk mengundang dan memohon doa restu untuk acara kami.\n\n"\
        f"*Untuk info lengkap dari acara bisa kunjungi link dibawah ini:*\n"\
        f"https://nadya-najib-wedding.vercel.app/untuk/{nama}\n\n"\
        f"Merupakan suatu kehormatan dan kebahagiaan tersendiri apabila berkenan hadir dan memberikan doa restu kepada kami berdua.\n\n"\
        f"*Mohon maaf perihal undangan hanya di bagikan melalui pesan ini.*\n\n"\
        f"Atas perhatiannya kami ucapkan banyak terima kasih.\n\n"\
        f"Wassalamualaikum\n"\
        f"Salam hangat, *Nadya & Najib*"

    return message

def send_using_pywhatkit(data):
    namas = data.keys()
    for nama in namas:
        message = prepare_message(nama)
        phone_number = parsing_indonesia_number(map_data[nama])
        pywhatkit.sendwhatmsg_instantly(
            phone_no=phone_number, 
            message=message,
)
        
def parsing_indonesia_number(number):
    if number[0] == "0":
        number = number[1:]
        number = "+62" + number
    return number
        
map_data = {
        "nadya": "085161992903",
    }

send_using_pywhatkit(map_data)