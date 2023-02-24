from bs4 import BeautifulSoup

def main():

    with open('website.html', 'r') as file:
        contents = file.read()

    soup = BeautifulSoup(contents, 'html.parser')

    # print(soup.title)
    # print(soup.title.string)

    # print(soup.prettify())

    all_anchor_tags = soup.find_all(name='a')
    # print(all_anchor_tags)

    # for tag in all_anchor_tags:
    #     print(tag.getText())
    #     print(tag.get('href'))

    heading = soup.find(name='h1', id="name")
    section_heading = soup.find(name='h3', class_="heading")
    # print(heading)
    # print(section_heading)
    # print(section_heading.get("class"))

    company_url = soup.select_one(selector="p a") #looks for an a tag inside a p tag - returns the first match - use 'select' to get them all
    name = soup.select_one(selector="#name")
    # print(company_url)
    # print(name)

    headings = soup.select(".heading")
    print(headings)

if __name__ == "__main__":
    main()