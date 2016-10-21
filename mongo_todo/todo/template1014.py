import web

urls=(

'/','Test'

)

render = web.template.render('templates')

class Test:

	def GET(self):
		return render.showRender('hello world')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()