# portfolio_site
How is this project structure different than a Flask (or Node) application? What role are the urls.py and views.py files responsible for?
This project structure is different from a Flask or Node application is that is uses different folders that accesses different routes through urls, views and model files while Flask or Node is set up with a singular source of truth.

Why do we use two seperate urls.py files? How do they interact?
We use two separate urls.py files so that if we have a seperate set of rules we can establish different routes so that if I were trying to convey a message I could use a view to redirect to a different file that might contain a different display. The use of the include can redirect to a different url set up of views in a different file.

When is it desirable to split our code over multiple apps? Why would we want to do so?
It is desirable to split our code over multiple apps because it helps apply different features that might not be able to have the same rules as another app. It is easier to debug our code and helps with keeping our information secure, scalable and generally easier to use than Flask or Node.

.
