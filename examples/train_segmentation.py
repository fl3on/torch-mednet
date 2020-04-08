from midasmednet.segmentation import SegmentationTrainer
from sacred import Experiment
import midasmednet.dataset
ex = Experiment('landmark_segmentation')
ex.add_config('/home/raheppt1/projects/mednet/config/aortath_segmentation.yaml')

@ex.config
def segmentation_config():
    data_reader = midasmednet.dataset.read_h5

@ex.capture
def start_segmentation(run_name,
                        log_dir,
                        model_path,
                        print_interval,
                        max_epochs,
                        learning_rate,
                        data_path,
                        training_subject_keys,
                        validation_subject_keys,
                        image_group,
                        label_group,
                        samples_per_subject,
                        class_probabilities,
                        patch_size, batch_size,
                        num_workers,
                        in_channels,
                        out_channels,
                        f_maps,
                        data_reader):

    trainer = SegmentationTrainer(run_name,
                                    log_dir,
                                    model_path,
                                    print_interval,
                                    max_epochs,
                                    learning_rate,
                                    data_path,
                                    training_subject_keys,
                                    validation_subject_keys,
                                    image_group,
                                    label_group,
                                    samples_per_subject,
                                    class_probabilities,
                                    patch_size, batch_size,
                                    num_workers,
                                    in_channels,
                                    out_channels,
                                    f_maps,
                                    data_reader)
    trainer.run()

@ex.automain
def main():
    start_segmentation()
    
