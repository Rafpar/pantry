import subprocess


def git_context_processor(request):

    process = subprocess.Popen(["git", "describe", "--tags", "--abbrev=0"], stdout=subprocess.PIPE)
    tag = process.communicate()[0].strip().decode("utf-8")
    return {'version': tag}
