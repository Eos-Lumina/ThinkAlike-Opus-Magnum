# Test script to check write permissions in archive_legacy
with open(r'F:\ThinkAlike_Project\archive_legacy\write_test.txt', 'w', encoding='utf-8') as f:
    f.write('Write test successful.')
print('Write test file created.')
