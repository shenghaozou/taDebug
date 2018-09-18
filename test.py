#!/usr/bin/python
import subprocess, json, re, sys, main

PASS = 'PASS'
PROBLEMS = 20
EPSILON = 0.01

def areResultExpected(actualResult, expectedResult):
    if abs(actualResult - expectedResult) > EPSILON:
        return "expected (%s) but found (%s)" % (actualResult, expectedResult)
    return None

def problem1(lines):
    expected = 0
    output = main.test()
    error = areResultExpected(output, expected)
    return error if error else PASS

def get_python_binary_name():
    try:
        subprocess.check_output(['python3', '--version'], stderr=subprocess.STDOUT)
        return 'python3'
    except:
        return 'python'

def get_python_version(python_binary):
    try:
        output = subprocess.check_output([python_binary, '--version'],
                                         stderr=subprocess.STDOUT)
        output = str(output, 'utf-8')
    except:
        return 'unknown'
    return output

def main():
    result = {'score': 0, 'tests': []}
    program = 'main.py'

    python_binary = get_python_binary_name()
    version = get_python_version(python_binary)
    print('Your Python version: '+version)

    if version.lower().find('python 3') < 0:
        print('WARNING! Your Python version may not work for this class.')
        print('Please check with us about this.')
        print()

    if len(sys.argv) == 2:
        program = sys.argv[1]
    try:
        cmd = [python_binary, program]
        print('Running your program with this command: ' + ' '.join(cmd) + '\n')
        output = subprocess.check_output(cmd)
    except:
        print('Your Python program crashed.  Please fix it to get any points.')

        # chuck output lines by problem
        problemNumber = None
        problems = dict() # key:problem number, val: list of lines
        for line in output.split('\n'):
            m = re.match(r'Problem (\d+)$', line)
            if m:
                problemNumber = int(m.group(1))
                problems[problemNumber] = []
            elif problemNumber:
                problems[problemNumber].append(line)

        # run checker on each section
        for problemNum in range(1, PROBLEMS + 1):
            fn = globals().get('problem%d' % problemNum, None) # our test
            # run test and record output
            try:
                testResult = fn()
            except Exception as e:
                testResult = "Got exception {} when running test {}".format(
                    str(e), problemNum)
            result['tests'].append({
                'test': problemNum,
                'result': testResult
            })
        # final score
        passing = [t for t in result['tests'] if t['result'] == PASS]
        result['score'] = len(passing) * 100 // len(result['tests'])

    # save/display results
    with open('result.json', 'w') as f:
        f.write(json.dumps(result, indent=2))
    print('RESULTS:')
    for test in result['tests']:
        print('  Problem %d: %s' % (test['test'], test['result']))
    print('Score: %d%%' % result['score'])

if __name__ == '__main__':
    main()
