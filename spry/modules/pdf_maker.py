from weasyprint import HTML, CSS
import os

def create_pdf(username, totals, found_accounts):
    """Generate PDF report with found accounts."""
    # Build accounts list HTML
    accounts_html = ""
    if found_accounts:
        accounts_html = "<div class='accounts-section'><h4>Found Accounts:</h4><ul id='triple'>"
        for account_url in found_accounts:
            # Extract domain name for display
            domain = account_url.split('/')[2] if '/' in account_url else account_url
            accounts_html += f"<li><a href='{account_url}'>{domain}</a></li>"
        accounts_html += "</ul></div>"
    else:
        accounts_html = "<div class='accounts-section'><p>No accounts found.</p></div>"
    
    # Check if Instagram image exists
    instagram_img_html = ""
    instagram_img_path = f"./{username}.jpg"
    if os.path.exists(instagram_img_path):
        instagram_img_html = f"<div class='image-section'><img class='insta' src='{instagram_img_path}' alt='Instagram Profile'/></div>"
    
    html_content = f'''<body width="600px">
        <div class="top">
            <br /><br />
            <h4>SPRY Report</h4>
            <p>Data about <b>{username}</b></p>
        </div>
        {instagram_img_html}
        <div class="summary">
            <p><b>Total accounts found: {totals}</b></p>
        </div>
        {accounts_html}
    </body>'''
    
    css = CSS(string='''
    body { padding: 20px; }
    .top { text-align: center; border-bottom: 2px dashed deepskyblue; padding: 5px; margin-bottom: 20px; }
    .summary { text-align: center; margin: 20px 0; padding: 10px; }
    .summary p { font-size: 14px; margin: 10px 0; }
    p { font-family: mono; font-size: 12px; }
    h2,h3,h4 { font-family: "Andale Mono"; font-size: 14px; margin: 10px 0; }
    ul,li { font-family: "Andale Mono"; font-size: 11px; letter-spacing: 0.08em; }
    ul { list-style: none; padding: 0; margin: 0; width: 100%; }
    ul#triple { display: flex; flex-wrap: wrap; width: 500px; margin-bottom: 20px; border-top: 1px solid #ccc; }
    ul#triple li { width: 33.333%; padding: 5px; box-sizing: border-box; border-bottom: 1px solid #ccc; float: left; display: inline; }
    ul#triple li a { color: #0066cc; text-decoration: none; }
    ul#triple li a:hover { text-decoration: underline; }
    .image-section { text-align: center; margin: 20px 0; padding: 10px; }
    .insta { width: 150px; height: 150px; object-fit: cover; border-radius: 50%; display: block; margin: 0 auto; }
    .accounts-section { margin: 20px 0; }
    .accounts-section h4 { font-family: "Andale Mono"; font-size: 14px; margin-bottom: 10px; }
    ''')
    
    html = HTML(string=html_content)
    html.write_pdf(
        f'{username}-report.pdf', stylesheets=[css])