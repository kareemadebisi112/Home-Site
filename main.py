from fasthtml import common as fh

css = [fh.Link(rel='stylesheet', href='style.css', type='text/css')]
bootstrap_icons = [fh.Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css')]
all_headers = css+bootstrap_icons


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
html = fh.Div('HTML', cls='tag row')
css = fh.Div('CSS', cls='tag row')
python = fh.Div('Python', cls='tag row')
htmx = fh.Div('HTMX', cls='tag new row')

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

                                cls='stack'
                            ),


                            # Main Content
                            fh.Div(
                                fh.Div(
                                    fh.Div(
                                        fh.H2('About Me'),
                                        fh.P('Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.',cls='about-me')
                                    ,cls='row'),
                                    fh.Div(
                                        fh.H2('Projects'),
                                        fh.Div(
                                            fh.Div(
                                                fh.H3('Project 1'),
                                                fh.Div(html,css,python,htmx, cls='column'),
                                                fh.P('This is a description of the project',cls='project-description'),
                                                cls='project'
                                            ),
                                            fh.Div(
                                                fh.H3('Project 2'),
                                                fh.P('This is a description of the project',cls='project-description'),
                                                cls='project'
                                            ),
                                            cls='row'),
                                        cls='row'),
                                ),

                            ),
                            cls='column'
                        )
                    )
)

fh.serve()