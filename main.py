# Template: https://brittanychiang.com/

from fasthtml import common as fh

css = [fh.Link(rel='stylesheet', href='style.css', type='text/css')]
responsivecss = [fh.Link(rel='stylesheet', href='responsive.css', type='text/css')]
bootstrap_icons = [fh.Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css')]
all_headers = css+bootstrap_icons+responsivecss


app,rt = fh.fast_app()
h1 = fh.H1('Kareem Adebisi',cls='name')
h2 = fh.H2('Software Engineer, Founder, Artist',cls='title')
sub_title = fh.P('I am a software engineer with a passion for solving interesting problems with innovative solutions.',cls='description')
nav = {'About Me':'#','Experience':'#','Projects':'#','Contact':'#'}

# Socials
linkedin = fh.A(fh.I(cls='bi bi-linkedin'),href='')
github = fh.A(fh.I(cls='bi bi-github'),href='')
twitter = fh.A(fh.I(cls='bi bi-twitter'),href='')

# Languages and Technologies
# TODO: Turn into components that will allow for 'New' tags to be added
html = fh.Div('HTML + CSS', cls='tag row')
js = fh.Div('JavaScript', cls='tag row')
python = fh.Div('Python', cls='tag row')
sql = fh.Div('SQL', cls='tag row')
htmx = fh.Div('HTMX', cls='tag tool row')
django = fh.Div('Django', cls='tag tool row')
cpp = fh.Div('C++', cls='tag row')
csharp = fh.Div('C#', cls='tag row')
unity = fh.Div('Unity', cls='tag tool row')
salesforce = fh.Div('Salesforce', cls='tag tool row')

frm = fh.Form(
    # Tags with a `name` attr will have `name` auto-set to the same as `id` if not provided
    fh.Input(id='name', type='name', placeholder='Name'),
    fh.Input(id='email', type='email', placeholder='Email'),
    fh.Textarea(id='message', placeholder='Message'),
    fh.Button('Contact'),
    action='/contact', method='post'
    )

db = fh.database('data/users.db')
users = db.t.users
if users not in db.t:
    users.create(dict(name=str, email=str, message=str))

User = users.dataclass()

@rt('/')
def get(): return fh.Html(*all_headers, 
                    fh.Body(  

                        fh.Div(
                            # Header + Left Column
                            fh.Div(
                                fh.Div(h1, h2, sub_title, cls='row'),

                                fh.Div(fh.Nav(fh.Ul(
                                    fh.Li(fh.A('About Me',href='#')),
                                    fh.Li(fh.A('Experience',href='#')),
                                    fh.Li(fh.A('Projects',href='#')),
                                    fh.Li(fh.A('Contact',href='#'))))
                                    ,cls='row'),
                                
                                # Socials
                                fh.Div(
                                    fh.Div(
                                        fh.Div(linkedin ,cls='row'),
                                        fh.Div(github ,cls='row'),
                                        fh.Div(twitter ,cls='row')
                                        ,cls='column'
                                    )
                                    ,cls='row'
                                ),

                                cls='stack name-section'
                            ),


                            # Main Content
                            fh.Div(
                                fh.Div(

                                    # About Section
                                    fh.Div(
                                        fh.H2('About Me'),
                                        fh.P('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',cls='about-me')
                                    ,cls='row'),

                                    # Projects Section
                                    fh.Div(
                                        fh.H2('Projects'),
                                        fh.Div(
                                            fh.Div(
                                                fh.H3("The Daily Plank - The Daily Ed, Edd, n' Eddy Guessing Game"),
                                                fh.Div(html,python,js,django,htmx, cls='column'),
                                                fh.P('This is a description of the project',cls='project-description'),
                                                cls='project'
                                            ),
                                            fh.Div(
                                                fh.H3('Massive Prompts - Use AI to Get Ahead at Work'),
                                                fh.Div(html,python,js,django, cls='column'),
                                                fh.P('This is a description of the project',cls='project-description'),
                                                cls='project'
                                            ),
                                        cls='row'),
                                    cls='row'),

                                    # Experience Section
                                    fh.Div(
                                        fh.H2('Experience'),
                                        fh.Div(
                                            fh.Div(
                                                fh.H3("RTX - Senior Software Engineer"),
                                                fh.Div(html,js,salesforce, cls='column'),
                                                fh.P('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',cls='experience-description'),
                                                cls='project'
                                            ),
                                            fh.Div(
                                                fh.H3('Intepros Federal - Software Engineer'),
                                                fh.Div(html,python,js,sql,django, cls='column'),
                                                fh.P('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',cls='experience-description'),
                                                cls='project'
                                            ),
                                        cls='row')                                    
                                    ,cls='row'),

                                    # Contact Section
                                    fh.Div(
                                        fh.H2('Contact Me'),
                                        fh.Div(
                                            frm,
                                        ),
                                    )
                                ),
                            ),
                            cls='column main-section'
                        )
                    )
)

@rt("/contact")
def post(request):
    return fh.RedirectResponse('/', status_code=201)

fh.serve()