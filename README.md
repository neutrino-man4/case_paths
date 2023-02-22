## CASE Paths (formerly pofah: Physics Objects For Anomaly Hunting)

The input/output paths can be found here. 

These paths are stored as key-value pairs in the form of Python dictionaries present in the following scripts (only necessary ones to get it all running are mentioned below):
- `path_constants/sample_dict.py`
    - reading input files for training/testing the VAE: `base_dir_events` 
- `path_constants/sample_dict_file_parts_input.py`
    - same as above: `base_dir`
- `path_constants/sample_dict_file_parts_reco.py`
    - writing the reconstructed files to disk: `base_dir` (these files are moderately large so watch your disk quota)
- `path_constants/experiment_dict.py` 
    - saving trained model: `model_dir`
    - saving 
    - rest should be self-explanatory. 
- `path_constants/sample_dict_file_parts_selected.py`
    - Dump the background and injected signal data used for the QR: `base_dir`

The necessary directories for each run of the VAE are created by the `/util/experiment.py` script. In the scripts you encounter in `case_vae/`, you'll find an object of the form `experiment = expe.Experiment(model_dir=True,..)` somewhere in the code. This initializes the `Experiment` module within this class, which then creates the `model_dir` whose path is in the definition. All other required directories can likewise be created, the possible options can be found in the `experiment.py` script mentioned above. Go and take a look!