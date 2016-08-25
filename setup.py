from setuptools import setup, find_packages

setup(name='gnip_tweet_evaluation',
        packages=find_packages(),
        scripts=[
            'tweet_evaluator.py',
            'user_id_evaluator.py',
            'tweet_engagements.py',
            ],
        version='0.1',
        license='MIT',
        author='Jeff Kolb',
        author_email='jeffakolb@gmail.com',
        description="Tools for evaluation of Tweets, and interface to Twitter's Insights APIs", 
        url='https://github.com/jeffakolb/Gnip-Tweet-Evaluation',
        install_requires=['sngrams','pyyaml','requests','requests_oauthlib','pyfarmhash']  ,
        extras_require={'plotting':['matplotlib']}
        )