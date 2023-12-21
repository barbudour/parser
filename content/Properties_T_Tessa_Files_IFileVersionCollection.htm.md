# IFileVersionCollection - свойства
##  __Свойства
[Added](P_Tessa_Files_IFileVersionCollection_Added.htm)|  Версия файла,
которая была добавлена и ещё не была сохранена, или null, если такая версия
отсутствует. Для файла может быть одновременно создано не более одной такой
версии.  
---|---  
[AreComprehensive](P_Tessa_Files_IFileVersionCollection_AreComprehensive.htm)|
Признак того, что коллекция содержит полный список версий в кэше. Если признак
установлен, то не потребуется получать список версий при их выводе
пользователю. По умолчанию значение false.  
[Count](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.count#system-
collections-generic-icollection-1-count)| Gets the number of elements
contained in the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IFileVersion](T_Tessa_Files_IFileVersion.htm)>)  
[IsReadOnly](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.isreadonly#system-
collections-generic-icollection-1-isreadonly)| Gets a value indicating whether
the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)
is read-only.  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IFileVersion](T_Tessa_Files_IFileVersion.htm)>)  
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
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IFileVersion](T_Tessa_Files_IFileVersion.htm)>)  
[Last](P_Tessa_Files_IFileVersionCollection_Last.htm)| Актуальная (последняя)
версия файла.  
##  __См. также
#### Ссылки
[IFileVersionCollection - ](T_Tessa_Files_IFileVersionCollection.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
