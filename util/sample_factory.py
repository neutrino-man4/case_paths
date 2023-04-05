import os
from collections import OrderedDict
import pathlib
import case_paths.path_constants.sample_dict as sd
import case_paths.jet_sample as jesa
import case_paths.util.event_sample as evsa
import case_paths.util.utility_fun as utfu


class SamplePathDirFactory():

    def __init__(self, path_dict):
        self.base_dir = path_dict['base_dir']
        self.sample_dir = path_dict['sample_dir']
        self.sample_files = path_dict['file_names']

    def update_base_path(self, repl_dict):
        self.base_dir = utfu.multi_replace(self.base_dir, repl_dict)
        return self

    def sample_dir_path(self, id, additional_id=None, mkdir=False):
        #print(self.sample_dir)
        #print("hereeee")
        #print(self.sample_dir)

        #print(id)

        if id in self.sample_dir:
            print("YES!")
        else:
            print("WTF!!!")

        s_path = os.path.join(self.base_dir, self.sample_dir[id])
        if (bool(additional_id)):
            s_path = os.path.join(self.base_dir, self.sample_dir[id],self.sample_dir[additional_id])
            
        #print("WEIRRD!")
        if mkdir:
            pathlib.Path(s_path).mkdir(parents=True, exist_ok=True) # have to create directory for each sample here when writing results, not optimal, TODO: fix
        return s_path

    def sample_file_path(self, id, additional_id=None,mkdir=False,overwrite=False,customname=None):
        #print("XXX")
        #print(self.sample_files)
        #print(additional_id)
        s_path = self.sample_dir_path(id, additional_id=additional_id,mkdir=mkdir)

        #print("HAAAAAAA")
        #print(self.sample_files)
        #print(id)
        if overwrite == False:
            return os.path.join(s_path, self.sample_files[id]+'.h5')
        else:
            print(os.path.join(s_path, customname+'.h5'))
            return os.path.join(s_path, customname+'.h5')
    
    
##### utility functions

def read_inputs_to_sample_dict_from_file(sample_ids, paths):
    data = OrderedDict()
    for sample_id in sample_ids:
        data[sample_id] = js.JetSample.from_input_file(sample_id, read_fun(sample_id))
    return data




def read_inputs_to_sample_dict_from_dir(sample_ids, paths, cls, read_n=None, **cuts):
    data = OrderedDict()
    for sample_id in sample_ids:
        print('reading ', paths.sample_dir_path(sample_id))
        data[sample_id] = cls.from_input_dir(sample_id, paths.sample_dir_path(sample_id), read_n=read_n, **cuts)
    return data

def read_inputs_to_sample_dict_from_dir_with_JE_tags(sample_ids, paths, JE_tags, cls, read_n=None, **cuts):
    data = OrderedDict()
    for sample_id in sample_ids:
        for tag in JE_tags:
            print('reading ', os.path.join(paths.sample_dir_path(sample_id),tag))
            try:
                data[sample_id+f'_{tag}'] = cls.from_input_dir(sample_id+f'_{tag}', os.path.join(paths.sample_dir_path(sample_id),tag), read_n=read_n, **cuts)
                if tag == 'nominal':
                    data['weights']=dr.CaseDataReader(os.path.join(paths.sample_dir_path(sample_id),tag)).read_weights_from_dir()
                    # Additionally for the nominal file, we add the systematic uncertainty weights as an additional column to the dataset. 
            except:
                pass # in case the tag does not exist
    return data
def read_inputs_to_jet_sample_dict_from_dir(sample_ids, paths, read_n=None, **cuts):
    ''' read dictionary of JetSamples '''
    return read_inputs_to_sample_dict_from_dir(sample_ids, paths, jesa.JetSample, read_n=read_n, **cuts)

def read_inputs_to_jet_sample_dict_from_dir_with_JE_tags(sample_ids, paths, JE_tags, read_n=None, **cuts):
    ''' read dictionary of JetSamples '''
    return read_inputs_to_sample_dict_from_dir_with_JE_tags(sample_ids, paths, JE_tags, jesa.JetSample, read_n=read_n, **cuts)

def read_inputs_to_event_sample_dict_from_dir(sample_ids, paths, read_n=None, **cuts):
    ''' read dictionary of EventSamples '''
    return read_inputs_to_sample_dict_from_dir(sample_ids, paths, evsa.EventSample, read_n=read_n, **cuts)
