import bottle


class LBPlugin:
    @staticmethod
    def setup():
        # Application
        return bottle.Bottle()

    @staticmethod
    def auth(app, path, func, method):
        # Method
        match method:
            case "callback":
                def handler():
                    return func(bottle.request)
                app.route(f"/{path}/callback", "GET", handler)
            case "login":
                def handler():
                    result = func(bottle.request, bottle.request.query.get("callback"))
                    return {"url": result or False}
                app.route(f"/{path}/login", "GET", handler)
            case "metadata":
                def handler():
                    bottle.response.content_type = "text/xml"
                    return func()
                app.route(f"/{path}/metadata", "GET", handler)
            case _:
                # log error
                return {"error": "Invalid auth plugin method name"}

    @staticmethod
    def identity(app, path, func, method):
        # Method
        match method:
            case "group.get":
                def handler(group):
                    return {"group": func(group) or False}
                app.route(f"/{path}/group/<group>", "GET", handler)
            case "user.get":
                def handler(username):
                    return {"user": func(username) or False}
                app.route(f"/{path}/user/<username>", "GET", handler)
            case "user.groups":
                def handler(username):
                    return {"groups": func(username) or False}
                app.route(f"/{path}/groups/<username>", "GET", handler)
            case "user.search":
                def handler(query):
                    return {"search": func(query) or False}
                app.route(f"/{path}/search/<query>", "GET", handler)
            case _:
                # log error
                return {"error": "Invalid identity plugin method name"}
