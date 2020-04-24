from midasmednet.landmarks import LandmarkTrainer
from sacred import Experiment
from sacred.observers import MongoObserver
import midasmednet.dataset

ex = Experiment('landmark_detection')
ex.observers.append(MongoObserver(db_name='mednet'))
ex.add_config('/home/raheppt1/projects/mednet/config/aortath_landmarks.yaml')


@ex.config
def landmark_config():
    data_reader = midasmednet.dataset.read_zarr
    restore_name = None
    lambda_l2 = 0.001
                   
@ex.capture
def transform():
    Rotaiton

@ex.automain
def main(run_name,
         log_dir,
         model_path,
         print_interval,
         max_epochs,
         learning_rate,
         data_path,
         training_subject_keys,
         validation_subject_keys,
         image_group,
         heatmap_group,
         samples_per_subject,
         class_probabilities,
         patch_size, batch_size,
         num_workers,
         in_channels,
         out_channels,
         f_maps,
         heatmap_treshold,
         heatmap_num_workers,
         data_reader,
         restore_name,
         _run):

    trainer = LandmarkTrainer(run_name,
                              log_dir,
                              model_path,
                              print_interval,
                              max_epochs,
                              learning_rate,
                              data_path,
                              training_subject_keys,
                              validation_subject_keys,
                              image_group,
                              heatmap_group,
                              samples_per_subject,
                              class_probabilities,
                              patch_size, batch_size,
                              num_workers,
                              in_channels,
                              out_channels,
                              f_maps,
                              heatmap_treshold,
                              heatmap_num_workers,
                              data_reader,
                              _run=_run,
                              restore_name=restore_name)

    trainer.run()
