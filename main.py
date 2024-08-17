# Template: https://brittanychiang.com/

from fasthtml import common as fh

title = [fh.Title('Kareem Adebisi')]
favicon = [fh.Link(rel='icon', href='home_site_logo.png', type='image/x-icon')]
viewport = [fh.Meta(name='viewport', content='width=device-width, initial-scale=1.0')]
css = [fh.Link(rel='stylesheet', href='style.css', type='text/css')]
responsivecss = [fh.Link(rel='stylesheet', href='responsive.css', type='text/css')]
bootstrap_icons = [fh.Link(rel='stylesheet', href='https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css')]
all_headers = css+bootstrap_icons+responsivecss+favicon+viewport+title


app,rt = fh.fast_app()
h1 = fh.A(fh.H1('Kareem Adebisi',cls='name'),href='/')
h2 = fh.H2('Software Engineer, Artist, Tinkerer',cls='title')
sub_title = fh.P('I am a software engineer with a passion for solving interesting problems with innovative solutions.',cls='description')
nav = {'About Me':'#','Experience':'#','Projects':'#','Contact':'#'}

# Socials
'''
<a href="https://calendar.app.google/bppoS98yQGr9M4Z59" target="_blank" rel="noopener noreferrer">Make Appointment</a>
'''
linkedin = fh.A(fh.I(cls='bi bi-linkedin'),href='https://www.linkedin.com/in/kareem-adebisi-495441142/')
github = fh.A(fh.I(cls='bi bi-github'),href='https://github.com/kareemadebisi112')
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
react = fh.Div('React', cls='tag tool row')

about_me = fh.P('''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys 
                standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only 
                five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem 
                Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.''',cls='about-me')
# Company Text
rtx_description = fh.P('''Spearheaded comprehensive code reviews, ensuring quality and adherence to best practices.
                        Empowered junior developers through impactful mentorship, fostering their growth and 
                        enhancing team performance.Managed deployment schedule to ensure reliable software releases for client. Coordinated with senior management 
                       to prioritize project objectives and ensure alignment with 
                        client goals. ''', cls='experience-description')
intepros_description = fh.P('''Engineered an enterprise application to increase efficiency of client’s reporting methods. 
                                Built automations that enabled modernization of client’s manual processes. 
                                Established a culture of collaboration by serving as a resource and mentoring junior developers. 
                                Facilitated demos to guide the client through application features and development progress. 
                                Consulted with client during agile ceremonies to plan sprints to clarify and define priorities. 
                                Spearheaded the development of enterprise software to improve client case management process. ''', cls='experience-description')
pivial_description = fh.P('''Integrated Jira and Salesforce environments to improve task management continuity. 
                                Created flows to automate data storage and manipulation within enterprise production environment. 
                                Engineered automations to improve the efficiency of database management and record creation. 
                                Created and maintained development sandboxes for feature testing and deployments.''', cls='experience-description')
ascellon_description = fh.P(''' Implemented Salesforce and Outlook integration to support business development and lead generation. 
                                    Created and maintained Salesforce environment to scale and improve visibility of email campaigns. 
                                    Coordinated with IT Manager to reconfigure enterprise assets to enhance corporate resilience. 
                                    Built Salesforce applications to improve efficiency and support business objectives. 
                                    Implemented automated reports to provide insight to enterprise customers and enhance business success. 
                                    Instituted and maintained corporate git repository to improve system redundancy. 
                                    ''', cls='experience-description')

frm = fh.Form(
    # Tags with a `name` attr will have `name` auto-set to the same as `id` if not provided
    fh.Input(id='name', type='name', placeholder='Name'),
    fh.Input(id='email', type='email', placeholder='Email'),
    fh.Textarea(id='message', placeholder='Message'),
    fh.Button('Contact'),
    hx_post='/contact', hx_swap_oob='true', hx_target='#contact'
    )

db = fh.database('data/users.db')
users = db.t.users
if users not in db.t:
    users.create(dict(name=str, email=str, message=str))

User = users.dataclass()


# @dataclass
# class Contact:
#     name: str
#     email: str
#     message: str

@rt('/')
def get(): return fh.Html(*all_headers, 
                    fh.Body(  

                        fh.Div(
                            # Header + Left Column
                            fh.Div(
                                fh.Div(h1, h2, sub_title, cls='row'),

                                fh.Div(fh.Nav(fh.Ul(
                                    fh.Li(fh.A('About Me',href='/#about',cls='nav')),
                                    fh.Li(fh.A('Projects',href='/#projects',cls='nav')),
                                    fh.Li(fh.A('Experience',href='/#experience',cls='nav')),
                                    fh.Li(fh.A('Contact',href='/#contact',cls='nav')),))
                                    ,cls='row'),
                                
                                # Socials
                                fh.Div(
                                    fh.Div(
                                        fh.Div(linkedin ,cls='row social'),
                                        fh.Div(github ,cls='row social'),
                                        fh.Div(twitter ,cls='row social')
                                        ,cls='column social-container'
                                    )
                                    ,cls='row socials'
                                ),

                                cls='stack name-section'
                            ),


                            # Main Content
                            fh.Div(
                                fh.Div(

                                    # About Section
                                    fh.Div(
                                        fh.H2('About Me'),
                                        about_me,
                                    cls='row', id='about'),


                                    # Projects Section
                                    fh.Div(
                                        fh.H2('Projects'),
                                        fh.Div(
                                            fh.A(fh.Div(
                                                fh.H3("The Daily Plank - The Daily Ed, Edd, n' Eddy Guessing Game"),
                                                fh.H4('2024'),
                                                fh.P('This is a description of the project',cls='project-description'),
                                                fh.Div(html,python,django,htmx, cls='column tag-container'),
                                                cls='project'
                                            ),href='https://www.daily-plank.com/'),
                                            fh.Div(
                                                fh.H3('Massive Prompts - Use AI to Get Ahead at Work'),
                                                fh.H4('2024'),
                                                fh.P('This is a description of the project',cls='project-description'),
                                                fh.Div(html,python,js,django, cls='column tag-container'),                                                
                                                cls='project'
                                            ),
                                            fh.Div(
                                                fh.H3('Grant Propel - Find Grants for Your Business'),
                                                fh.H4('Coming Soon'),
                                                fh.P('This is a description of the project',cls='project-description'),
                                                fh.Div(html,python,django,htmx, cls='column tag-container'),                                                
                                                cls='project coming-soon'
                                            ),                                        cls='row project-container'),
                                    cls='row', id='projects'),

                                    # Experience Section
                                    fh.Div(
                                        fh.H2('Experience'),
                                        fh.Div(
                                            fh.Div(
                                                fh.H3("Senior Software Engineer - RTX"),
                                                fh.H4('Jun 2023 - Present'),
                                                rtx_description,                                          
                                                fh.Div(html,js,salesforce, cls='column tag-container'),
                                                cls='project'
                                            ),
                                            fh.Div(
                                                fh.H3('Software Engineer - Intepros Federal'),
                                                fh.H4('Dec 2021 - Jun 2023'),
                                                intepros_description,                                            
                                                fh.Div(html,python,js,sql,django, cls='column tag-container'),
                                                cls='project'
                                            ),
                                            fh.Div(
                                                fh.H3('Salesforce Engineer - Pivital'),
                                                fh.H4('Dec 2021 Contract'),
                                                pivial_description,                                            
                                                fh.Div(js,sql,react,salesforce, cls='column tag-container'),
                                                cls='project'
                                            ),
                                            fh.Div(
                                                fh.H3('Software Engineer - Ascellon Corporation'),
                                                fh.H4('Jun 2014 - Jun 2021'),
                                                ascellon_description,                                            
                                                fh.Div(cpp,html,js,salesforce, cls='column tag-container'),
                                                cls='project'
                                            ),
                                        cls='row project-container')                                    
                                    ,cls='row', id='experience'),

                                    # Contact Section
                                    fh.Div(
                                        fh.H2('Contact Me'),
                                        fh.Div(
                                            fh.A('Email Me',href='mailto:kareem.s.adebisi@gmail.com',cls='contact-button'),
                                        ),
                                    cls='row', id='contact'),
                                cls='stack main-stack'),
                            cls='column main-section'),
                        cls='column main-container'),
                    )
)


fh.serve()