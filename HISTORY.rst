=======
History
=======

0.1 (2024-01-20)
------------------

* Initial coding by Simon Moulds, packaged by Simon Mudd
* Initial release on pypi
* Then Simon Mudd had to delete the release because he was calling it NFRA instead of NRFA, mainly because nfrapy sounds a bit like frappuchino and that suggests a clever logo. Simon Moulds had to point out to the disappointed Muddpile that this was the wrong acronym. 
* Basic functionality: simply calls the NRFA API and gets time series data
* A command line script is included: nrfa_get_ts

0.2 (2024-02-01)
-----------------

* Update so that the time column is always parsed as a datetime (S Moulds)
* Added flag that allows the time to be used as an index, which is useful for some dataframe operations (D Golberg)
* Added an option to feed the timeseries function a list of strings that all fetching then concatenaiton of different timeseries (D Goldberg)