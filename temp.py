from pathlib import Path
ref = Path('/Users/noashay/test/.swip/references.txt')

def update_ref_head(ref, commit_id: str) -> None:  ## change this function, don't assume head is file's first line
    with open(ref, "r") as file:
        ref_txt = file.readlines()
        _, current_commit_id = ref_txt[0].strip().split('=')
        ref_txt[0] = ref_txt[0].replace(current_commit_id, commit_id)
    with open(ref, "w") as file:
        file.writelines(ref_txt)

update_ref_head(ref, 'O')