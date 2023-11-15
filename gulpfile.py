from invoke import task
import shutil

path = {
    'controller': 'src/controllers',
    'routes': 'src/routes'
}

@task
def default(ctx):
    build_typescript(ctx)

def build_typescript(ctx):
    print("Compiling TypeScript...")
    shutil.rmtree(path['controller'], ignore_errors=True)
    ctx.run("tsc")
    print("TypeScript compilation complete.")
