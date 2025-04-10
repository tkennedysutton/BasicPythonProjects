#Task: Write a script that takes a list of numbers (e.g., pupil test scores or daily coffee quality ratings) and computes the, Sum, Average, Standard Deviation
import torch 
pupil_scores = torch.tensor([48,50,35,45,20,49,23,34,45,46,47,38,23,5],dtype=torch.float32)

def x(pupil_scores):
    return pupil_scores.sum()
xx = x(pupil_scores)
print("sum of pupil scores=\n",xx)


def y(pupil_scores):
    return pupil_scores.numel()
yy = y(pupil_scores)

def z(xx,yy):
    return xx / yy
zz = z(xx,yy)
print("AVERAGE of pupil scores=\n",zz)

def xy(pupil_scores):
    return pupil_scores.std()

sdev_scores = xy(pupil_scores)
print("standard deviation of scores=\n",sdev_scores)

