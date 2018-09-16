import os

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    line_iter = (line.strip() for line in open(filename))
    print(line_iter)
    return [line for line in line_iter if line and not line.startswith("#")]


if __name__ == "__main__":
    for line in parse_requirements('requirements.txt'):
        os.system('pip install {}'.format(line)) 
