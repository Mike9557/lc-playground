class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        unique_list = {}
        domain = 'http://' + startUrl.split('/')[2]
        def dfs(url):
            nonlocal unique_list
            nonlocal domain
            if url in unique_list:
                return
            unique_list[url] = []
            for u in htmlParser.getUrls(url):
                if domain == u[:len(domain)]:
                    unique_list[url].append(u)
                    dfs(u)
        dfs(startUrl)
        result = []
        for url in unique_list:
            result += [url] + unique_list[url]
        return list(set(result))