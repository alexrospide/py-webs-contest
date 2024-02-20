import web_scraping
import send_email

if __name__ == '__main__':
    print('...Starting!')
    lista_concurso = web_scraping.do_the_scraping()
    print('Preparing E-mail...')
    send_email.do_send_email(lista_concurso)
    print('E-mail send!')


