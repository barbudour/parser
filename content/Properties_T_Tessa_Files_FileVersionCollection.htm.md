# FileVersionCollection - свойства
##  __Свойства
[Added](P_Tessa_Files_FileVersionCollection_Added.htm)|  Версия файла, которая
была добавлена и ещё не была сохранена, или null, если такая версия
отсутствует. Для файла может быть одновременно создано не более одной такой
версии.  
---|---  
[AreComprehensive](P_Tessa_Files_FileVersionCollection_AreComprehensive.htm)|
Признак того, что коллекция содержит полный список версий в кэше. Если признак
установлен, то не потребуется получать список версий при их выводе
пользователю. По умолчанию значение false.  
[CanSuspendNotifications](P_Tessa_Platform_Collections_SuspendableObservableCollection_1_CanSuspendNotifications.htm)|
Признак того, что вызов
[SuspendNotifications()](M_Tessa_Platform_Collections_SuspendableObservableCollection_1_SuspendNotifications.htm)
подавляет уведомления об изменении.  
(Унаследован от
[SuspendableObservableCollection<T>](T_Tessa_Platform_Collections_SuspendableObservableCollection_1.htm))  
[Count](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.count#system-
collections-objectmodel-collection-1-count)| Gets the number of elements
actually contained in the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileVersion](T_Tessa_Files_IFileVersion.htm)>)  
[Item[Int32]](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.item#system-
collections-objectmodel-collection-1-item\(system-int32\))| Gets or sets the
element at the specified index.  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileVersion](T_Tessa_Files_IFileVersion.htm)>)  
[Item[TKey]](P_Tessa_Platform_Collections_ObservableCollectionLookup_3_Item.htm)|
Получает одно из значений, доступных по заданному ключу, которое
гарантированно не равно null. При отсутствии таких значений выбрасывает
исключение [System.Collections.Generic.KeyNotFoundException].  
(Унаследован от [ObservableCollectionLookup<TKey, TItem,
TCollection>](T_Tessa_Platform_Collections_ObservableCollectionLookup_3.htm))  
[Items](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.items#system-
collections-objectmodel-collection-1-items)| Gets a
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)
wrapper around the
[Collection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1).  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileVersion](T_Tessa_Files_IFileVersion.htm)>)  
[Last](P_Tessa_Files_FileVersionCollection_Last.htm)| Актуальная (последняя)
версия файла.  
##  __См. также
#### Ссылки
[FileVersionCollection - ](T_Tessa_Files_FileVersionCollection.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
