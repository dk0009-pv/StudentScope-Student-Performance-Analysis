import itertools
import unittest
import pandas as pd
import numpy as np
from analysis_core import *

class DashboardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.df = load_data()
        cls.model, cls.metrics, cls.report, cls.cm = train_week3(cls.df)

    def test_three_filter_combinations(self):
        df = self.df
        cases = [({'school':['gp'],'address':['u'],'internet':['yes']}, (df.school=='gp') & (df.address=='u') & (df.internet=='yes')),
                 ({'school':['ms'],'address':['r'],'internet':['no']}, (df.school=='ms') & (df.address=='r') & (df.internet=='no')),
                 ({'school':['gp','ms'],'address':['r'],'internet':['yes']}, (df.address=='r') & (df.internet=='yes'))]
        counts=[]
        for selections, mask in cases:
            actual=filter_data(df,selections); expected=df.loc[mask]
            pd.testing.assert_frame_equal(actual,expected)
            pd.testing.assert_series_equal(grade_distribution(actual),grade_distribution(expected))
            self.assertEqual(grade_distribution(actual).sum(),len(actual))
            self.assertGreater(len(actual),0); counts.append(len(actual))
        self.assertEqual(len(set(counts)),3)

    def test_empty_and_all(self):
        self.assertTrue(filter_data(self.df,{'school':[]}).empty)
        pd.testing.assert_frame_equal(filter_data(self.df,{c:self.df[c].unique() for c in FILTERS}),self.df)
        self.assertEqual(grade_distribution(self.df.iloc[:0]).sum(),0)

    def test_week3_metrics(self):
        self.assertEqual((self.metrics['train'],self.metrics['test']),(519,130))
        self.assertAlmostEqual(self.metrics['accuracy'],109/130)
        self.assertAlmostEqual(self.metrics['baseline'],110/130)
        self.assertEqual(self.cm.values.sum(),130)
        old = pd.read_csv(ROOT/'outputs'/'classification_report.csv',index_col=0)
        np.testing.assert_allclose(self.report.loc[LABELS].values,old.loc[LABELS].values)

    def test_every_valid_prediction(self):
        combinations=list(itertools.product(range(1,5),range(4),range(1,5),sorted(self.df.internet.unique()),sorted(self.df.Mjob_group.unique())))
        X=pd.DataFrame(combinations,columns=FEATURES)
        predictions=self.model.predict(X); probabilities=self.model.predict_proba(X)
        self.assertEqual(len(predictions),512)
        self.assertTrue(set(predictions)<=set(LABELS))
        np.testing.assert_allclose(probabilities.sum(axis=1),1)
        for row in [combinations[0],combinations[-1],combinations[234]]:
            result, probs=predict_grade(self.model,*row)
            self.assertIn(result,LABELS); self.assertAlmostEqual(sum(probs.values()),1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
