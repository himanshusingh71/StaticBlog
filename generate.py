import os
import urllib.parse

# Define the template for the main index.html file
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="favicon.ico" />
    <title>Himanshu's Blog</title>
    <script src="https://cdn.tailwindcss.com"></script>
        <script>
        document.addEventListener("DOMContentLoaded", () => {
            const cursorCircle = document.querySelector(".cursor-circle");

            document.addEventListener("mousemove", (e) => {
                cursorCircle.style.transform = `translate(${e.clientX}px, ${e.clientY}px)`;
            });
        });
    </script>
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
            color: #1a1c24 !important; /* Slightly Darker Gray */
        }

        a:hover {
            color: blue !important; /* Even Darker Gray on Hover */
            text-decoration: underline;
        }

.cursor-circle {
    position: fixed;
    top: 0;
    left: 0;
    width: 50px; /* Circle size */
    height: 50px;
    border: 2px solid rgba(255, 255, 255, 0.8); /* Circle color */
    border-radius: 50%;
    pointer-events: none;
    transform: translate(-50%, -50%);
    animation: rotateAround 2s linear infinite;
}

@keyframes rotateAround {
    0% {
        transform: translate(-50%, -50%) rotate(0deg) translateX(20px) rotate(0deg);
    }
    100% {
        transform: translate(-50%, -50%) rotate(360deg) translateX(20px) rotate(-360deg);
    }
}

</style>



</head>
<body class="flex flex-col items-center min-h-screen">
    <div class="cursor-circle"></div>


    <!-- Header -->
    <header class="sm:w-4/5 md:w-4/5 lg:w-full text-center py-6 sm:text-4xl md:text-6xl lg:text-6xl font-bold ascii-text underline" >
        Himanshu's Blog
    </header>
    
    <!-- Main Content -->
    <main class="flex flex-col items-center my-8 mx-3" >
        <div class="text-3xl ascii-text">
        {blog_links}
        </div>
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
</html>
"""

def generate_blog_list():
    blog_links = ""
    for folder in sorted(os.listdir()):
        folder_path = os.path.join(os.getcwd(), folder)
        if os.path.isdir(folder_path) and os.path.exists(os.path.join(folder_path, "index.html")):
            encoded_folder = urllib.parse.quote(folder)
            blog_links += f'<div class="my-8">&#128214;    <a href="{encoded_folder}/" class="text-blue-500">{folder}</a></div>\n'
    
    return blog_links

# Generate and save the main index.html file
if __name__ == "__main__":
    blog_links = generate_blog_list()
    with open("index.html", "w") as f:
        f.write(HTML_TEMPLATE.replace("{blog_links}", blog_links))
    
    print("index.html has been generated successfully!")
