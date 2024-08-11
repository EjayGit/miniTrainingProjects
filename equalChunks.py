# tODO
sample_list = [21,55,18,33,24,22,68,35,79]
splitNum = int(len(sample_list)/3)

start = 0
end = splitNum

for index in range(1,4):
    sample = list(reversed(sample_list[start:end]))
    print(f"Chunk-{index} = {sample}")
    start = end
    end += splitNum        
