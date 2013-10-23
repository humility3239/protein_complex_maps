#!/usr/bin/python

# Unit tests for new clustering analysis functionality

import unittest
import protein_complex_maps.read_data as rd
import numpy as np


class ReadDataTest(unittest.TestCase):

	def setUp(self,):

		sample_filename = "./test_data.txt"
		sample_file = open(sample_filename, 'rb')
		self.data_matrix, self.name_list = rd.read_datafile(sample_file)

		print self.data_matrix

		sample_filename2 = "./test_data2.txt"
		sample_file2 = open(sample_filename2, 'rb')
		self.data_matrix2, self.name_list2 = rd.read_datafile(sample_file2)

		print self.data_matrix2

	def testRead(self,):
		
		assert(self.data_matrix[np.ix_([0],[0])] == 0.0)
		assert(self.data_matrix[np.ix_([2],[0])] == 10.0)
		assert(self.data_matrix[np.ix_([2],[1])] == 100.0)
		assert(self.data_matrix[np.ix_([11],[2])] == 20.0)
		
		assert(self.data_matrix2[np.ix_([0],[0])] == 4.0)
		assert(self.data_matrix2[np.ix_([2],[0])] == 0.0)
		assert(self.data_matrix2[np.ix_([2],[1])] == 0.0)
		assert(self.data_matrix2[np.ix_([2],[3])] == 121.0)
		assert(self.data_matrix2[np.ix_([10],[3])] == 5.0)
		#np.testing.assert_almost_equal( score, -1.73220495821 )
		#np.testing.assert_almost_equal( score, 0.000343732988528)

	def testConcat(self,):
		print "testConcat"
		c_dmat, c_nlist = rd.concat_data_matrix(self.data_matrix, self.name_list, self.data_matrix2, self.name_list2)

		print c_dmat
		print c_nlist

		index1 = c_nlist.index('ENSG00000072110')
		assert(c_dmat[np.ix_([index1],[0])] == 25.0)
		assert(c_dmat[np.ix_([index1],[7])] == 30.0)

		index2 = c_nlist.index('ENSG00000100519')
		assert(c_dmat[np.ix_([index2],[3])] == 105.0)
		assert(c_dmat[np.ix_([index2],[7])] == 0.0)

if __name__ == "__main__":
	unittest.main()


