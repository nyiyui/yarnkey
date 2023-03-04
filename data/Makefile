all: fe-p1 fe-all

fe-p1: freq-p1.csv err-p1.csv

fe-all: freq-all.csv err-all.csv

clean:
	# don't delete the raw data!
	rm -f log-p1.slog.txt freq-p1.csv err-p1.csv log-all.slog.txt err-all.csv freq-all.csv

.PHONY: all fe-p1 fe-all clean

# raw data from the server
yarnkey-log.slog.txt:
	scp yarnkey-server:/proj/yarnkey/yarnkey-log.txt $@

log-p1.slog.txt: yarnkey-log.slog.txt valid-times-p1 per-time.py
	./per-time.py valid-times-p1 < $< > $@

freq-p1.csv: log-p1.slog.txt raw_to_freq.py freq_to_csv.py
	cat $< | ./raw_to_freq.py | ./freq_to_csv.py > $@

err-p1.csv: log-p1.slog.txt err.py
	./err.py < $< > $@

# raw data for p1 and p2
log-all.slog.txt: yarnkey-log.slog.txt valid-times-p2 per-time.py sel_sess.py deduplicate.py
	cat yarnkey-log.slog.txt | ./per-time.py valid-times-p2 | ./deduplicate.py > $@
	cat yarnkey-log.slog.txt | ./sel_sess.py 'krt.*' | ./deduplicate.py >> $@

err-all.csv: log-all.slog.txt err.py
	./err.py < $< > $@

freq-all.csv: log-all.slog.txt freq_to_csv.py raw_to_freq.py
	cat $< | ./raw_to_freq.py | ./freq_to_csv.py > $@
