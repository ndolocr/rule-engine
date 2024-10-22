from dslResolver.DSLResolver import DSLResolver

class DSLKeywordResolver:
    def __init__(self, resolver_list=None):
        if resolver_list is None:
            resolver_list = []
        # Using dictionary comprehension to create the map
        # self.dsl_keyword_resolver_map = {resolver.get_resolver_keyword(): resolver for resolver in resolver_list}
        # Initialize an empty dictionary
        self.dsl_keyword_resolver_map = {}
        for resolver in resolver_list:
            self.dsl_keyword_resolver_map[resolver.get_resolver_keyword()] = resolver

    
    def get_dsl_keyword_resolver_list(self):
        return self.dsl_keyword_resolver_map

    def get_resolver(self, keyword: str):
        # Returning None if the keyword is not found, mimicking Optional behavior in Python
        return self.dsl_keyword_resolver_map.get(keyword)