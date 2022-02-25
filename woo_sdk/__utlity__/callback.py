import inspect
import glob
import importlib
import pandas as pd
import time
import datetime as dt

from ..__modules__ import logger

def get_functions(unkwn_mod):
    return inspect.getmembers(unkwn_mod, inspect.isfunction)

def get_args(unkwn_mod):
    return inspect.getfullargspec(unkwn_mod)[0]

def args_matcher(string_args, matching_args):
    
    # based on curr args build data list
    try:
        data_list = []
        for string_name in string_args:
            data_list.append(matching_args[string_name])
    except:
        logger.critical("Args and data_dict don't match !!!")
        raise Exception("Args and data_dict don't match !!!")
    
    return data_list

def run_all_functions(unkwn_mod, matching_args, target_func):
    for method_name, method_ref in get_functions(unkwn_mod):
        if target_func in method_name:

            # print(f"[+1] ({(unkwn_mod.__name__).split('.')[1]}.py) {target_func}()")

            string_args   = get_args(method_ref)

            try:
                args_data_list = args_matcher(string_args, matching_args)
            except  Exception as e:

                # TODO: Handle this
                logger.critical(f"[{unkwn_mod.__name__}.{target_func}()]{str(e)}")
                return { 'error' : '  [MISMATCHED_ARGS] {}'.format(unkwn_mod.__name__)}
            
            try:
                func_output = method_ref(*args_data_list)
                # print('[-]   > success  ')
                return func_output
            except Exception as e:
                # TODO: Handle this
                # print((f'> EXCEPTION THROWN <'))
                logger.critical(f"[{unkwn_mod.__name__}.{target_func}()]{str(e)}")
                return { 'error' : f' raised Exception' }


def run_all_modules(lst_mods, matching_args, target_func, callback=None):
    all_module_return_data = []
    for unkwn_mod in lst_mods:
        unkwn_mod = importlib.import_module(unkwn_mod)

        START_TIME = time.time()

        try:
            return_data = run_all_functions(unkwn_mod, matching_args, target_func)
        except:
            None
        
        try:
            if callback != None and unkwn_mod.__name__ != '__daily__.__pycache__': 
                if isinstance(return_data, pd.DataFrame):
                    if not return_data.empty:
                        callback(return_data, unkwn_mod.__name__)
                        logger.info(f"({unkwn_mod.__name__}) Took {round(time.time() - START_TIME, 2)}s")

                else:
                    if return_data != None:
                        callback(return_data, unkwn_mod.__name__)
                        logger.info(f"({unkwn_mod.__name__}) Took {round(time.time() - START_TIME, 2)}s")

        except Exception as e:
            logger.critical(f"(Exception) {str(e)}")

        # all_module_return_data.append(return_data) if return_data != None else None
    

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
'                       FOLDER HANDLERS                                '

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def run_folder(matching_args, folder_name, target_func='main',callback=None):
    lst_mods = [f_name.replace('.py','').replace('/','.') for f_name in glob.glob('{}/*'.format(folder_name))]
    run_all_modules(lst_mods, matching_args, target_func, callback)

