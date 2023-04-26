


root_dataset = "/content/EVA3D/datasets/DeepFashion/images/"

testing_images= ["MEN-Jackets_Vests-id_00005346-01_4_full.png",
                 "WOMEN-Dresses-id_00006993-03_7_additional.png",
                 "WOMEN-Tees_Tanks-id_00007918-05_4_full.png"]


from IPython.display import Image

for im in testing_images:
    Image('evaluations/512x256_deepfashion/iter_0420000/random_angles/images_paper_fig/0000000.png')