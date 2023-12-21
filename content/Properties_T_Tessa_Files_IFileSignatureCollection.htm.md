# IFileSignatureCollection - свойства
##  __Свойства
[Added](P_Tessa_Files_IFileSignatureCollection_Added.htm)|  Подписи для версии
файла, которые были добавлены и ещё не были сохранены, или пустая коллекция,
если не было добавлено ни одной подписи. Для версии файла может быть
одновременно создано неограниченное количество подписей.  
---|---  
[AreComprehensive](P_Tessa_Files_IFileSignatureCollection_AreComprehensive.htm)|
Признак того, что коллекция содержит полный список подписей в кэше. Если
признак установлен, то не потребуется получать список подписей при их выводе
пользователю, если запрашивается вывод подписей без загруженных данных. По
умолчанию значение false.  
[Count](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.count#system-
collections-generic-icollection-1-count)| Gets the number of elements
contained in the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>)  
[HasComprehensiveData](P_Tessa_Files_IFileSignatureCollection_HasComprehensiveData.htm)|
Признак того, что коллекция содержит полный список подписей в кэше, в т.ч.
бинарные данные подписей. Если признак установлен, то не потребуется получать
список подписей при их выводе пользователю. По умолчанию значение false.  
[IsReadOnly](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.isreadonly#system-
collections-generic-icollection-1-isreadonly)| Gets a value indicating whether
the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)
is read-only.  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>)  
[Item[TKey]](P_Tessa_Platform_Collections_ILookupContainer_2_Item.htm)|
Получает одно из значений, доступных по заданному ключу, которое
гарантированно не равно null. При отсутствии таких значений выбрасывает
исключение [System.Collections.Generic.KeyNotFoundException].  
(Унаследован от [ILookupContainer<TKey,
TValue>](T_Tessa_Platform_Collections_ILookupContainer_2.htm))  
[Item[Int32]](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1.item#system-
collections-generic-ilist-1-item\(system-int32\))| Gets or sets the element at
the specified index.  
(Унаследован от
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>)  
##  __См. также
#### Ссылки
[IFileSignatureCollection - ](T_Tessa_Files_IFileSignatureCollection.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
