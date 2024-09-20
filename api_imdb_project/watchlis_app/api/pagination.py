from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class MoviewlistPagination(PageNumberPagination):
    page_size=10 # it divides into whole into 10
    page_query_param='P' #"http://localhost:8000/watch/list2/?P=2"
    page_size_query_param='size'# if the client want thier wish to give ex: ?size=15
    max_page_size=13# it takes only 13 per each page

    #/list2/?P=last by defualt gives last page
    # last_page_strings='end' #/list2/?P=end


class MoviewlistLOPagination(LimitOffsetPagination):
    default_limit=5
    max_limit=10
    limit_query_param='limit'
    offset_query_param='start'

class MoviewlistCursorPagination(CursorPagination):# this will shows only next and previous
    #by deafult this displays latest ones first like desc to asc
    page_size=5
    cursor_query_param='record' #by default it shows cursor so instead of that will display record
    ordering='-created'  # without - gives asc-desc
