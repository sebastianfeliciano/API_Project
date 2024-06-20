class example:
  def __str__(self):
    return 'I am a user-defined object'

my_obj = example()
obj_hash_value = hash(my_obj)

print(my_obj)
print(obj_hash_value)