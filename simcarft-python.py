import os

def generate_talent_blocks(class_name, spec_name, template, talent_positions, talent_values, filename):
    """
    Generate talent combination blocks for any class/spec
    
    Parameters:
    class_name: e.g., "warrior", "deathknight"
    spec_name: e.g., "Prot", "Blood"
    template: the template string with placeholders like {t1}, {t2}, etc.
    talent_positions: list of talent positions to iterate through
    talent_values: list of possible values for each talent
    filename: output filename
    """
    
    # Generate all combinations
    blocks = []
    
    # Create nested loops based on the number of talent positions
    from itertools import product
    talent_combinations = product(talent_values, repeat=len(talent_positions))
    
    for combo in talent_combinations:
        # Create format dictionary
        format_dict = {}
        for i, talent_value in enumerate(combo):
            format_dict[f't{talent_positions[i]}'] = talent_value
        
        block = template.format(**format_dict)
        blocks.append(block)
    
    return blocks, len(blocks)

def main():
    # ===== CONFIGURATION - EDIT THESE VALUES =====
    
    # Class and spec info
    CLASS_NAME = "paladin"
    SPEC_NAME = "Prot"
    OUTPUT_FILENAME = "ww_monk_talent_combinations.txt"
    
    # Talent configuration
    TALENT_POSITIONS = [1, 3, 6, 7]  # Which talent positions to vary
    TALENT_VALUES = [1, 2, 3]  # Possible talent values
    
    # Template - use {t1}, {t3}, {t5}, {t6}, {t7} for placeholders
    TEMPLATE = '''monk="ww_monk-{t1}-0-{t3}-0-0-{t6}-{t7}"
talents={t1}0{t3}00{t6}{t7}
level=100
race=blood_elf
role=dps
position=back
spec=windwalker

actions.precombat=flask,type=greater_draenic_agility_flask
actions.precombat+=/food,type=clefthoof_sausages
actions.precombat+=/snapshot_stats

head=bladefang_hood,id=124580,bonus_id=487:648
neck=vexed_chain,id=124610,bonus_id=487:648
shoulder=bladefang_spaulders,id=124588,bonus_id=486:648
back=marshwater_cloak,id=124616,bonus_id=488:648
chest=bladefang_chestguard,id=124567,bonus_id=490:648
wrist=bladefang_bracers,id=124564,bonus_id=486:648
hands=bladefang_gauntlets,id=124576,bonus_id=490:648
waist=bladefang_belt,id=124592,bonus_id=488:648
legs=bladefang_gauntlets,id=124576,bonus_id=489:648
feet=bladefang_boots,id=124572,bonus_id=490:648
finger1=arduous_circle,id=124604,bonus_id=488:648
finger2=arduous_band,id=124598,bonus_id=488:648
trinket1=saberblade_insignia,id=124622,bonus_id=604:647
trinket2=spineshard_crest,id=124623,bonus_id=604:648
main_hand=hammer_of_wicked_infusion,id=124371
off_hand=hammer_of_wicked_infusion,id=124371


'''
    #main_hand=bite_of_the_bleeding_hollow,id=124379
    # Output folders
    FOLDERS = [
        r"E:\Simcarft-testek-wod\Windwalkermonk",
        r"E:\Simcarft-testek-wod\Windwalkermonk"  # You can add more folders here
    ]
    
    # ===== END CONFIGURATION =====
    
    # Generate blocks
    all_blocks, total_blocks = generate_talent_blocks(
        CLASS_NAME, SPEC_NAME, TEMPLATE, TALENT_POSITIONS, TALENT_VALUES, OUTPUT_FILENAME
    )
    
    # Save to each specified folder
    for folder_path in FOLDERS:
        try:
            # Create the folder if it doesn't exist
            os.makedirs(folder_path, exist_ok=True)
            
            # Create the full file path
            full_path = os.path.join(folder_path, OUTPUT_FILENAME)
            
            # Write the file
            with open(full_path, 'w') as f:
                for i, block in enumerate(all_blocks, 1):
                    f.write(block)
                    if i < len(all_blocks):
                        f.write('\n')
            
            print(f"✓ Successfully saved to: {full_path}")
            
        except Exception as e:
            print(f"✗ Error saving to {folder_path}: {e}")
    
    print(f"\nGenerated {total_blocks} complete {SPEC_NAME} {CLASS_NAME} talent combination blocks!")
    print(f"Total combinations: {len(TALENT_VALUES)}^{len(TALENT_POSITIONS)} = {total_blocks}")

if __name__ == "__main__":
    main()