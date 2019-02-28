pages = [
    {
    "filename": "content/index.html",
    "output": "docs/index.html",
    "title": "About Me",
    },
    {
    "filename": "content/projects.html",
    "output": "docs/projects.html",
    "title": "My Projects",
    },
    {
    "filename": "content/blog.html",
    "output": "docs/blog.html",
    "title": "My blog",
    },
]
    
def main():
#    page_title = page ['title']
    for page in pages:
        top = open('templates/top.html').read()
        middle = open(page['filename']).read()      
        bottom = open('templates/bottom.html').read()
        combined = top + middle + bottom
        open(page["output"],"w+").write(combined)
# do the same thing here that I learned in middle    
    
print("Built!")
    
    
if __name__== "__main__":
    main()

print("again")



#print('Building Home page')
#top_html = open('templates/top.html').read()
#middle_html = open('content/home.html').read()
#bottom_html = open('templates/bottom.html').read()
#combined_html = top_html + middle_html + bottom_html
#open('docs/index.html',"w+").write(combined_html)

#print('Building Blog page')
#top_html = open('templates/top.html').read()
#middle_html = open('content/blog.html').read()
#bottom_html=open('templates/bottom.html').read()
#combined_html = top_html +middle_html + bottom_html
#open('docs/blog.html',"w+").write(combined_html)

#print('Building projects page')
#top_html = open('templates/top.html').read()
#middle_html = open('content/projects.html').read()
#bottom_html=open('templates/bottom.html').read()
#combined_html = top_html +middle_html + bottom_html
#open('docs/projects.html',"w+").write(combined_html)
