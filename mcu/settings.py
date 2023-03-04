import board


__all__ = ['VOLT_PINS', 'IN_RANGE_THRESHOLDS', 'TIMEOUT_THRESHOLD']

VOLT_PINS = (board.A0, board.A1, board.A2, board.A3, board.A4, board.A5)
#VOLT_PINS = (board.A0, board.A1, board.A2, board.A3, board.A4, board.D2) # if using a board with a 7th pin

IN_RANGE_THRESHOLDS = [(-1, 40e3)] * 6

TIMEOUT_THRESHOLD = 120 * 1e6 # 0.12 s
#TIMEOUT_THRESHOLD = 400 * 1e6 # 0.4 s # for braille
