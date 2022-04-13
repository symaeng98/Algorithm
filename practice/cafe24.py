#########문제 1번#########
# def downHeap(args, index):
#     if (len(args)-1)<index*2:
#         return
#     elif (len(args)-1) == index*2:
#         if len(args[index]) > len(args[index*2]):
#             swap(args,index,index*2)
#             downHeap(args,index*2)
#         elif len(args[index]) == len(args[index*2]):
#             if args[index]<args[index*2]:
#                 swap(args,index,index*2)
#                 downHeap(args,index*2)
#     else:
#         if len(args[index*2])<len(args[index*2+1]):
#             minIndex = index*2
#         elif len(args[index*2])==len(args[index*2+1]):
#             if args[index*2]<args[index*2+1]:
#                 minIndex = index*2+1
#             else:
#                 minIndex = index*2
#         else:
#             minIndex = index*2+1
#         if len(args[index]) > len(args[minIndex]):
#             swap(args,index,minIndex)
#             downHeap(args, minIndex)
#         elif len(args[index]) == len(args[minIndex]):
#             if args[index]<args[minIndex]:
#                 swap(args,index,minIndex)
#                 downHeap(args, minIndex)
# def upHeap(args, index):
#     if index==1:
#         return
#     if len(args[index])<len(args[index//2]):
#         swap(args,index,index//2)
#         upHeap(args,index//2)
#     elif len(args[index])==len(args[index//2]):
#         if args[index]>args[index//2]:
#             swap(args,index,index//2)
#             upHeap(args,index//2)
#         else:
#             return
#     else:
#         return
#
# def swap(args, index1, index2):
#     tmp = args[index1]
#     args[index1] = args[index2]
#     args[index2] = tmp
#
# N = int(input())
# args = []
# for _ in range(N):
#     args.append(input())
# b = ['#']
# for a in args:
#     if a in b:
#         continue
#     b.append(a)
#     upHeap(b, len(b)-1)
# length = len(b)-1
# answer = []
# for i in range(length):
#     answer.append(b[1])
#     b[1] = b[len(b)-1]
#     b.pop(len(b)-1)
#     downHeap(b,1)

########문제 2번#########

