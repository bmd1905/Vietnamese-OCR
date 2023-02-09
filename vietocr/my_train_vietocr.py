import matplotlib.pyplot as plt
from PIL import Image
import torch
from vietocr.vietocr.tool.predictor import Predictor
from vietocr.vietocr.tool.config import Cfg
from vietocr.vietocr.tool.config import Cfg
from vietocr.vietocr.model.trainer import Trainer

config = Cfg.load_config_from_name('vgg_transformer')
# print(config)
# quit()
dataset_params = {
    'name':'hw',
    'data_root':'/Users/bmd1905/Desktop/dataset/data_line',
    'train_annotation':'train_line_annotation.txt',
    'valid_annotation':'test_line_annotation.txt'
}

params = {
         'print_every':1,
         'valid_every':1*10,
          'iters':100,
          #'checkpoint':'./checkpoint/transformerocr_checkpoint.pth',    
          'export':'./weights/seq2seq_test_local.pth',
          'metrics': 100
         }

config['trainer'].update(params)
config['dataset'].update(dataset_params)

device = torch.device('mps')
config['device'] = device

config['dataloader']['num_workers'] = 0
config['trainer']['batch_size'] = 1

# config['transformer']['num_encoder_layers'] = 1
# config['transformer']['num_decoder_layers'] = 1

#num_encoder_layers


trainer = Trainer(config, pretrained=True)


trainer.config.save('config.yml')


trainer.train()
print("Done")

