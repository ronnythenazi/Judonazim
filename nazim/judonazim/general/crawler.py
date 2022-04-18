import requests
from bs4 import BeautifulSoup as bs
from .general import is_url_startswith_article_path



def get_ask_search_request_link():
    return 'https://www.ask.com/web?q='

def get_preview_data_from_article(url):

    content = get_url_content(url)

    avatar = elem_fields(key='avatar', classname='tiny-avatar', val='src')
    thumb = elem_fields(key='thumb', classname='thumb', val='src')
    author = elem_fields(key='author', classname='author-crawl', val='txt')
    date_ = elem_fields(key='date', classname='date-crawl', val='txt')

    return get_custom_vals(content, avatar, thumb, author, date_)


def get_search_result_articles(search, start_from=0, max_per_page=10):
    result_lst = get_search_result_all(search)
    final_result = []

    for res in result_lst:
        url = get_url_from_search_result_item(res)
        if is_url_startswith_article_path(url) == False:
            continue

        title = get_title_from_search_result_item(res)
        descr = get_description_from_search_result_item(res)
        item = {'title' : title, 'url': url, 'descr':descr}

        perview_article_data = get_preview_data_from_article(url)
        for article_item in perview_article_data:
            key = article_item['key']
            val =article_item['val']
            item[key] = val


        final_result.append(item)

    return final_result[start_from:start_from + max_per_page]


def get_custom_vals(elem, *args):
    filter_lst = []
    for arg in args:
        fields = arg.get_fields()
        filter_lst.append(fields)
    res = get_elem_inner_filter(elem, filter_lst)
    return res



def get_title_from_search_result_item(xml):
    class_name = 'PartialSearchResults-item-title'
    title = get_text_from_classname(xml, class_name)
    return title

def get_description_from_search_result_item(xml):
    class_name = 'PartialSearchResults-item-abstract'
    description = get_text_from_classname(xml, class_name)
    return description

def get_url_from_search_result_item(xml):
    url = get_attribute_val_by_tagname(xml, 'a', 'href')
    return url

def get_text_from_classname(xml, calss_name):
    #title = xml.find(class_ = 'PartialSearchResults-item-title').text
    txt = xml.find(class_ = calss_name).text
    return txt

def get_attribute_val_by_tagname(xml, tag, attr):
    #url = xml.find('a').get('href')
    res = xml.find(tag).get(attr)
    return res

def get_attribute_val_by_classname(xml, calss_name, attr):
    #url = xml.find(class_ = 'thumb').get('src')
    res = xml.find(class_ = calss_name).get(attr)
    return res


def get_img_url_from_article(xml):
    calss_name = 'thumb'
    url = get_attribute_val_by_classname(xml, class_name, 'src')
    return url

def get_author_avatar_from_article(xml):
    calss_name = 'tiny-avatar'
    url = get_attribute_val_by_classname(xml, class_name, 'src')
    return url

def get_elem_inner_all(xml, tag_name, class_name):
    result_lst = xml.find_all(tag_name, {'class':class_name})
    return result_lst

class elem_fields():

    fields = []
    def __init__(self, key='', classname='', tag='', val=''):
        self.set_vars(key, classname, tag, val)
        self.set_fields()

    def set_vars(self, key, classname, tag, val):
        self.key = key
        self.classname = classname
        self.tag = tag
        self.val = val

    def set_fields(self):
        self.fields = { 'key':self.key, 'class': self.classname, 'tag':self.tag, 'val':self.val }

    def get_fields(self):
        return self.fields


def get_elem_inner_filter(elem, filter_dict_lst):
    #result_lst = get_elem_inner_all(xml, tag_name, class_name)
    filtered_result_lst = []
    for child_prop in filter_dict_lst:
        child_class = child_prop['class']
        child_tag = child_prop['tag']
        child_val =  child_prop['val']
        child_key_name = child_prop['key']

        if not child_class == '' and child_val=='txt':
            txt = get_text_from_classname(elem, child_class)
            item = {'key':child_key_name, 'val':txt}
            filtered_result_lst.append(item)
            continue

        attr_lst = ['src', 'href']
        if not child_class == '' and child_val in attr_lst:
            val = get_attribute_val_by_classname(elem, child_class, child_val)
            item = {'key':child_key_name, 'val':val}
            filtered_result_lst.append(item)
            continue

        if not child_tag == '' and child_val in attr_lst:
            val = get_attribute_val_by_tagname(elem, child_tag, child_val)
            item = {'key':child_key_name, 'val':val}
            filtered_result_lst.append(item)
            continue

        if child_val == 'inner':
            val = get_elem_inner_all(elem, child_tag, child_class)
            item = {'key':child_key_name, 'val':val}
            filtered_result_lst.append(item)
            continue
    return filtered_result_lst



def get_search_result_all(search):
    url = get_ask_search_request_link() + search
    content = get_url_content(url)
    result_lst =  get_elem_inner_all(content, 'div', 'PartialSearchResults-item')
    return result_lst

def get_url_content(url):
    res = requests.get(url)
    soup = bs(res.text, 'lxml')
    return soup
