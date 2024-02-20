import web_scraping
import send_email

if __name__ == '__main__':
    print('Hello World!')
    lista_concurso = web_scraping.do_the_scraping()
    print('aqui é no main')
    print(lista_concurso)
    send_email.do_send_email(lista_concurso)
    print('aqui já enviou o e-mail')


