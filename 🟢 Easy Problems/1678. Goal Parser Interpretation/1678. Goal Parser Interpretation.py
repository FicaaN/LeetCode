class Solution:
    def interpret(self, command: str) -> str:
        goal_return = []
        i = 0
        
        while i < len(command):
            if command[i] == 'G':
                goal_return.append('G')
                i += 1
            elif command[i:i+2] == '()':
                goal_return.append('o')
                i += 2
            elif command[i:i+4] == '(al)':
                goal_return.append('al')
                i += 4
        
        return ''.join(goal_return)

    # One line solution
    # return command.replace('()','o').replace('(al)','al')