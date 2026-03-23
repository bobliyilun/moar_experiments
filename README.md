# moar_experiments
Some questions:
moar seems to always rely on some sense of ground truth
does the adversarial scenario include truth tampering?

I could think of several things to try at this moment:
prompt injection at the pipeline level
prompt injection in the input dataset

Aside from the truth tampering mentioned above.

Is tampering off limits?

Furthermore, since each evaluation function is paired with a dataset and we are relatively short on time, 
I would need a very simple dataset if possible to break it 


https://huggingface.co/datasets/theatticusproject/cuad/tree/main/CUAD_v1
https://huggingface.co/datasets/theatticusproject/cuad/blob/main/CUAD_v1/master_clauses.csv