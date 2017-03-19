class EditPost(BlogHandler):
    def get(self, post_id):
        #1. fetch the post by post_id
        key = db.Key.from_path('Post', int(post_id), parent=blog_key())
        post = db.get(key)
        post = Post.get_by_id(int(post_id), parent=blog_key())
        #2. Check if logged in user is the author of the post (if post.author == self.user.key())
        if post.author == self.user.blog_key():
            self.render(editpost.html, post = post)
        else:
        	error="You are not the author of this post."
        	self.render("post.html", subject=subject, content=content, error=error)
    def post(self, post_id):
        #1. get subject and content
        
        2. check if both were provided
        3. check if logged in user is still the author
        4. go ahead and edit the post

/voteup/([0-9])+ => /voteup/123123

class VoteUp(BlogHandler):
	def get(self, post_id):
		1. fetch the post by post_id
		2. check if the post exists
		3. to fetch the Like object by post_id
		4. if post.author == self.user.key() => return because author of the post
		4. for user in likeObj.liked_by:
				if user == self.user.key().id():
					return #because already liked the post
		5. likeObj.append(self.user.key().id())
		6. likeObj.like_count+=1
		7. likeObj.put()
		8. return


class Comment(BlogHandler):
    def get(self):
        if self.user:
            self.render("comment_page.html")
        else:
            self.redirect("/login")

    def post(self):
        if not self.user:
            self.redirect('/')

        subject = self.request.get('subject')
        content = self.request.get('content')

        if subject and content:
            c = Comment(parent = blog_key(), 
                subject = subject,
                content = content,
                author=self.user.key())
            c.put()
            likeObj = Like(post_id=c.key().id())
            likeObj.put()
            self.redirect('/blog/%s' % str(c.key().id()))
        else:
            error = "subject and content, please!"
            self.render("comment_page.html", subject=subject, content=content, error=error)


# use this link to implement COmments
    <a href="/blog/{{p.key().id()/newcomment">Comment</a>



USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)
