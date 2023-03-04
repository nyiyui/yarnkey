all: ltr_count.csv norm_count.csv

norm_data.txt:
	( \
		./sel_sess.py '2022-04-10.*' < ./kyokukey_data.txt; \
		./sel_sess.py '2022-04-16.*' < ./kyokukey_data.txt; \
	) \
		> norm_data.txt

norm_count.csv: norm_data.txt
	./norm.py < norm_data.txt > norm_count.csv

norm_count2.csv: kyokukey_data.txt
	./norm.py < kyokukey_data.txt > norm_count2.csv

ltr_data.txt:
	cat ./kyokukey_data.txt > ltr_data.txt
#	cat ./kyokukey_data.txt \
#		| ./sel_uuid.py '(39dce704-8bf7-4b8c-811e-3fe6e7b85d47|ae5e3107-46b7-4e64-8f01-96520ac8a0a2)' exclude \
#		| ./sel_sess.py 'ltr.*' \
#		> ltr_data.txt

ltr_count.csv: ltr_data.txt
	./perltr.py < ltr_data.txt > ltr_count.csv

clean:
	rm -f ltr_data.txt ltr_count.csv
	rm -f norm_data.txt norm_count.csv

.PHONY: clean
