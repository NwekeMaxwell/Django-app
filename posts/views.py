from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# Create your views here. FBVs & CBVs

# dummy data to show posts to users
posts = [
    {
        "id" : 1,
        "title": 'Let\'s explore python',
        "content" : 'Python is intepreted,high level,general purpose programming language. Widely used in the field of web development, data science and machine learning.'
    },
    {
        "id" : 2,
        "title": 'Let\'s explore Javascript',
        "content" : 'Javascript is intepreted,high level,general purpose programming language. Widely used in the field of web development.'
    },
    {
        "id" : 3,
        "title": 'Django the best web framework',
        "content" : 'Django is used by almost every big tech company like facebook, google, youtube, instagram, etc.'
    },
]

def home(request):
    html = ""
    for post in posts:
        html += f'''
            <div>
                <a href="/posts/{post['id']}/">
                    <h1> {post['id']} - {post['title']}</h1>
                </a>
                <p> {post['content']}</p>
            </div>
        '''
    return render(request, 'home.html')
    # return HttpResponse(html)

def post(request, id):
    valid_id = False #lets use this boolean value to ensure we dont get an error page
    for post in posts:
        if post["id"] == id:
            valid_id = True
            post_dict = post
            break
    
    if valid_id:
        html = f'''
            <h1>{post_dict['title']}</h1>
            <p>{post_dict['content']} </p>
            <a href="/posts/home"> Back </a>
        '''
        return HttpResponse(html)
    else:
        return HttpResponseNotFound("Opps..Post not available!")

def redirectPostFn(request,id):
    url = reverse("post", args=[id])
    return HttpResponseRedirect(url)