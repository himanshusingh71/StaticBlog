import re
import os

# HTML template with placeholder for blog content
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-80HNCTMDHQ"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-80HNCTMDHQ');
</script>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="../favicon.ico" />
    <title>Himanshu's Blog</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&display=swap');
    .ascii-text {
        font-family: 'Fira Code', monospace;
        font-size: 2rem;
    }


        /* Soft Gray Theme */
        body {
            background-color: #a6a39c; /* Light Gray */
            color: black; /* Dark Gray */
            font-family: 'Fira Code', monospace;
        }

        a {
            color: #0074D9; /* Slightly Darker Gray */
            text-decoration: none;
        }

        a:hover {
            color: #111111; /* Even Darker Gray on Hover */
            text-decoration: underline;
        }



</style>
</head>
<body class="flex flex-col items-center min-h-screen">
    <!-- Header -->
    <header class="w-full text-center py-6 sm:text-4xl md:text-6xl lg:text-6xl font-bold ascii-text underline">
       <a href="../"> Himanshu's Blog </a>
    </header>
    
    <!-- Main Content -->
    <main class="sm:w-4/5 md:w-4/5 lg:w-1/2  text-2xl flex flex-col my-8 mx-3 a ascii-text">
       {blog_content}
    </main>
    
    <!-- Footer -->
<footer class="w-full flex justify-center items-center py-6 mt-auto">
    <a href="https://www.linkedin.com/in/himanshu-bisht-93a199194/" class="underline">
        <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">
            <path d="M22.23 0H1.77C.79 0 0 .77 0 1.72v20.56C0 23.23.79 24 1.77 24h20.46c.98 0 1.77-.77 1.77-1.72V1.72C24 .77 23.21 0 22.23 0zM7.08 20.49H3.56V9h3.52v11.49zM5.32 7.72a2.04 2.04 0 01-2.05-2.05c0-1.12.92-2.04 2.05-2.04s2.05.92 2.05 2.04c0 1.13-.92 2.05-2.05 2.05zM20.48 20.49h-3.52v-5.6c0-1.33-.03-3.04-1.86-3.04-1.86 0-2.14 1.46-2.14 2.96v5.68h-3.52V9h3.38v1.57h.05c.47-.9 1.62-1.86 3.34-1.86 3.58 0 4.24 2.35 4.24 5.4v6.38z"/>
        </svg>
    </a>
</footer>
</body>
</html>"""


def parse_markdown(md_text):
    """Convert a simple Markdown file to HTML with Tailwind CSS classes."""

    # Convert Large Headings
    md_text = re.sub(r'^# (.+)', r'<h1 class="text-3xl font-bold">\1</h1>', md_text, flags=re.MULTILINE)

    # Convert Subheadings
    md_text = re.sub(r'^## (.+)', r'<h2 class="text-2xl font-semibold">\1</h2>', md_text, flags=re.MULTILINE)

        # Convert Subheadings
    md_text = re.sub(r'^### (.+)', r'<h2 class="text-xl font-semibold">\1</h2>', md_text, flags=re.MULTILINE)

    # Convert Bold Text (**bold**) (Preserves inline formatting)
    md_text = re.sub(r"\*\*(.*?)\*\*|__(.*?)__", r'<strong>\1\2</strong>', md_text)


    # Convert Italic Text (*italic*) (Preserves inline formatting)
    md_text = re.sub(r'\*(.*?)\*', r'<em class="italic">\1</em>', md_text)

    md_text = re.sub(r"::center::(.*?)::center::", r'<div class="text-center">\1</div>', md_text, flags=re.DOTALL)

    md_text = md_text.replace("\n\n", "<br>\n")


    # Split paragraphs correctly (prevents breaking inline elements)
    paragraphs = md_text.split("\n\n")  # Split by empty lines to identify paragraphs
    paragraphs = [f"<p class='mb-4'>{p.replace('\n', ' ')}</p>" for p in paragraphs]  # Wrap each in <p> and replace inline newlines with spaces
    
    return "\n".join(paragraphs)


# Read Markdown file and convert it to HTML
def convert_markdown_to_html(md_file):
    if not os.path.exists(md_file):
        print(f"Error: {md_file} not found!")
        return ""

    with open(md_file, "r", encoding="utf-8") as f:
        md_content = f.read()

    return parse_markdown(md_content)


# Generate the final HTML file
def generate_blog(md_file, output_file="index.html"):
    blog_content = convert_markdown_to_html(md_file)
    
    # Inject blog content into the HTML template
    final_html = HTML_TEMPLATE.replace("{blog_content}", blog_content)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    print(f"Blog page generated: {output_file}")

if __name__ == "__main__":
    generate_blog("markdown.md")
