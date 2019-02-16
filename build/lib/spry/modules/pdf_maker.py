from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

def create_pdf(username, totals):
    """Test out functionality."""
    html = HTML(string='<body width="600px"><div class="top"><br /><br /><h4>SPRY Report</h4><p>Data about <b>{}</b></p></div>\
        <div><img class="insta" src="./{}.jpg"/></div\
        <div>Total accounts found: {}</div></body>'.format(username, username, totals))
    css = CSS(string='''
    .top { text-align: center; border-bottom: 2px dashed deepskyblue; padding: 5px; }
    p { font-family: mono; font-size: 12px; }
    h2,h3,h4 { font-family: "Andale Mono"; font-size: 14px; }
    ul,li { font-family: "Andale Mono"; font-size: 11px; letter-spacing: 0.08em; }
    ul { list-style: none; }
    ul { width: 500px; margin-bottom: 20px; border-top: 1px solid #ccc; }
    li { border-bottom: 1px solid #ccc; float: left; display: inline;}
    #double li { width:50%;}
    #triple li { width:33.333%; }
    #six li { width:16.666%; }
    #quad li { width:25%; }
    ''')
    html.write_pdf(
        '{}-report.pdf'.format(username), stylesheets=[css])