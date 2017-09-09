
import numpy as np



class Bicluster(object):

	def __init__(self, rows=[], cols=[], random_module=None):
		#kdrew: define as sets so we don't have duplicates, there should only be one row index and one column index for each actual row or column
		self.__rows = set(rows)
		self.__cols = set(cols)
		if random_module == None:
			try:
				import random 
			except ImportError:
				self.random_module = None
			else:
				self.random_module = random
		else:
			self.random_module = random_module

	def __str__(self,):
		return "Bicluster: \nrows: %s \ncolumns: %s" % (self.__rows, self.__cols)
 
 	def print_submatrix(self, data_matrix):
		submat = self.get_submatrix(data_matrix)
		print self.columns()
		rows = self.rows()
		for i, row in enumerate(submat):
			print "%s : %s " % (rows[i], np.round(np.array(row)[0],5).tolist() )

	def add_row(self, row_index):
		self.__rows.add(row_index)

	def remove_row(self, row_index):
		self.__rows.discard(row_index)
	
	def add_column(self, col_index):
		self.__cols.add(col_index)

	def remove_column(self, col_index):
		self.__cols.discard(col_index)

	def rows(self, ):
		tmp = list(self.__rows)
		tmp.sort()
		return tmp

	def columns(self, ):
		tmp = list(self.__cols)
		tmp.sort()
		return tmp

	#kdrew: returns submatrix defined by the bicluster
	#kdrew: without_indices creates the submatrix without the row specified by given indices
	def get_submatrix(self, matrix, without_rows=[], without_cols=[]):
		sorted_rows = list(self.__rows-set(without_rows))
		sorted_rows.sort()
		sorted_cols = list(self.__cols-set(without_cols))
		sorted_cols.sort()

		#print sorted_rows
		#print sorted_cols

		if len(sorted_rows) == 0:
			return np.matrix([]).reshape(0,1)
		if len(sorted_cols) == 0:
			return np.matrix([]).reshape(1,0)

		return matrix[np.ix_(sorted_rows, sorted_cols)]

	#kdrew: get single row with columns defined in bicluster
	def get_row(self, matrix, row, without_cols=[]):
		sorted_cols = list(self.__cols-set(without_cols))
		sorted_cols.sort()
		return matrix[np.ix_(list([row,]),sorted_cols)]

	#kdrew: get single column with rows defined in bicluster
	def get_column(self, matrix, column, without_rows=[]):
		sorted_rows = list(self.__rows-set(without_rows))
		sorted_rows.sort()
		return matrix[np.ix_(sorted_rows, list([column,]))]

	#kdrew: returns rows not in bicluster
	def get_outside_rows(self, matrix):
		all_rows = set(np.arange(matrix.shape[0]))
		#print "all_rows", all_rows
		return all_rows - self.__rows

	#kdrew: returns columns not in bicluster
	def get_outside_cols(self, matrix):
		all_cols = set(np.arange(matrix.shape[1]))
		return all_cols - self.__cols


	def get_random_outside_rows(self, matrix, seed=None, without_rows=[]):
		#import random as r
		if seed != None:
			self.random_module.seed(seed)
		outside_rows = self.get_outside_rows(matrix) - set(without_rows)
		random_sample_size = len(self.__rows)
		#print outside_rows
		#kdrew: when there are not enough outside_rows to sample from, just take all of them (not optimal but it is what we have)
		if len(self.__rows) > len(outside_rows):
			random_sample_size = len(outside_rows)
		#kdrew: return a list of random rows the size of the bicluster rows
		random_rows = self.random_module.sample( outside_rows, random_sample_size )
		#print random_rows
		random_rows.sort()
		return random_rows

	def get_random_outside_cols(self, matrix, seed=None, without_cols=[]):
		#import random as r
		if seed != None:
			self.random_module.seed(seed)
		outside_cols = self.get_outside_cols(matrix) - set(without_cols)
		random_sample_size = len(self.__cols)
		#print outside_cols
		#kdrew: when there are not enough outside_rows to sample from, just take all of them (not optimal but it is what we have)
		if len(self.__cols) > len(outside_cols):
			random_sample_size = len(outside_cols)
		#kdrew: return a list of random cols the size of the bicluster cols
		random_cols = self.random_module.sample( outside_cols, random_sample_size )
		#print random_cols
		random_cols.sort()
		return random_cols


	#kdrew: scale bicluster submatrix in full matrix
	def scale(self, matrix, scale_factor):

		sorted_rows = list(self.__rows)
		sorted_rows.sort()
		sorted_cols = list(self.__cols)
		sorted_cols.sort()

		if len(sorted_rows) == 0 or len(sorted_cols) == 0:
			return matrix
        
		matrix[np.ix_(sorted_rows, sorted_cols)] = matrix[np.ix_(sorted_rows, sorted_cols)] * scale_factor

		return matrix

class BiclusterDF(Bicluster):

	def __init__(self, rows=[], cols=[], random_module=None, data_frame=None):
		self.data_frame = data_frame
		self.df_rows = rows
		self.df_cols = cols

		rows_i = set([list(self.data_frame.index).index(x) for x in self.df_rows])
		cols_i = set([list(self.data_frame.columns).index(x) for x in self.df_cols])

		super(BiclusterDF, self).__init__(rows=rows_i, cols=cols_i, random_module=random_module)

 	def print_submatrix(self, data_frame=None):
		if data_frame is None:
			data_frame = self.data_frame
		subdf = data_frame.ix[self.rows(), self.columns()]
		print subdf

	#kdrew: returns submatrix defined by the bicluster
	#kdrew: without_indices creates the submatrix without the row specified by given indices
	#kdrew: returns np matrix
	def get_submatrix(self, data_frame=None, without_indices=[], without_cols=[]):
		if data_frame is None:
			data_frame = self.data_frame

		without_row_ids = set([list(data_frame.index).index(x) for x in without_indices])
		without_cols_ids = set([list(data_frame.columns).index(x) for x in without_cols])

		sorted_rows = list(set(self.rows())-set(without_row_ids))
		sorted_rows.sort()
		sorted_cols = list(set(self.columns())-set(without_cols_ids))
		sorted_cols.sort()

		#print sorted_rows
		#print sorted_cols

		if len(sorted_rows) == 0:
			return np.matrix([]).reshape(0,1)
		if len(sorted_cols) == 0:
			return np.matrix([]).reshape(1,0)

		try:
			matrix = data_frame.as_matrix()
		except AttributeError: 
			if isinstance(data_frame,(np.ndarray)):
				matrix = data_frame
			else:
				raise

		return matrix[np.ix_(sorted_rows, sorted_cols)]

	#kdrew: get single row with columns defined in bicluster
	def get_row(self, data_frame, row, without_cols=[]):
		cols = set(self.columns) - set(without_cols)
		matrix = data_frame.ix[[row], cols].as_matrix()
		return matrix

	#kdrew: get single column with rows defined in bicluster
	def get_column(self, data_frame, column, without_rows=[]):
		rows = set(self.rows()) - set(without_rows)
		matrix = data_frame.ix[rows, [column]].as_matrix()
		return matrix


	#kdrew: returns rows not in bicluster
	def get_outside_rows(self, data_frame):
		all_rows = set(data_frame.index)
		#print "all_rows", all_rows
		return all_rows - set(self.rows())

	#kdrew: returns columns not in bicluster
	def get_outside_cols(self, data_frame):
		all_cols = set(data_frame.columns)
		return all_cols - set(self.columns())


	def get_random_outside_rows(self, data_frame, seed=None, without_rows=[]):
		#import random as r
		if seed != None:
			self.random_module.seed(seed)
		outside_rows = self.get_outside_rows(data_frame) - set(without_rows)
		random_sample_size = len(self.rows())
		#print outside_rows
		#kdrew: when there are not enough outside_rows to sample from, just take all of them (not optimal but it is what we have)
		if len(self.rows()) > len(outside_rows):
			random_sample_size = len(outside_rows)
		#kdrew: return a list of random rows the size of the bicluster rows
		random_rows = self.random_module.sample( outside_rows, random_sample_size )
		#print random_rows
		random_rows.sort()
		return random_rows

	def get_random_outside_cols(self, data_frame, seed=None, without_cols=[]):
		#import random as r
		if seed != None:
			self.random_module.seed(seed)
		outside_cols = self.get_outside_cols(data_frame) - set(without_cols)
		random_sample_size = len(self.columns())
		#print outside_cols
		#kdrew: when there are not enough outside_rows to sample from, just take all of them (not optimal but it is what we have)
		if len(self.columns()) > len(outside_cols):
			random_sample_size = len(outside_cols)
		#kdrew: return a list of random cols the size of the bicluster cols
		random_cols = self.random_module.sample( outside_cols, random_sample_size )
		#print random_cols
		random_cols.sort()
		return random_cols


	#kdrew: scale bicluster submatrix in full matrix
	def scale(self, data_frame, scale_factor):

		if len(self.rows()) == 0 or len(self.columns()) == 0:
			return data_frame.as_matrix()
        
		data_frame.ix[self.rows(), self.columns()] = data_frame.ix[self.rows(), self.columns()] * scale_factor

		#kdrew: might want to return just the data_frame here (?)
		return data_frame.as_matrix()
