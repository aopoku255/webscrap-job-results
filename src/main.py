from bs4 import BeautifulSoup

with open('src\\views\\index.html', 'r') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    course_html_tags = soup.find_all('div', class_='card')
    for courses in course_html_tags:
        course_name = courses.h5.text
        course_price = courses.a.text.split()[-1]

        print(f'course_name: {course_name}, pirce: {course_price}')
        