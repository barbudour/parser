# FileSignatureCollection - свойства
##  __Свойства
[Added](P_Tessa_Files_FileSignatureCollection_Added.htm)|  Подписи для версии
файла, которые были добавлены и ещё не были сохранены, или пустая коллекция,
если не было добавлено ни одной подписи. Для версии файла может быть
одновременно создано неограниченное количество подписей.  
---|---  
[AreComprehensive](P_Tessa_Files_FileSignatureCollection_AreComprehensive.htm)|
Признак того, что коллекция содержит полный список подписей в кэше. Если
признак установлен, то не потребуется получать список подписей при их выводе
пользователю, если запрашивается вывод подписей без загруженных данных. По
умолчанию значение false.  
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
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>)  
[HasComprehensiveData](P_Tessa_Files_FileSignatureCollection_HasComprehensiveData.htm)|
Признак того, что коллекция содержит полный список подписей в кэше, в т.ч.
бинарные данные подписей. Если признак установлен, то не потребуется получать
список подписей при их выводе пользователю. По умолчанию значение false.  
[Item[Int32]](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1.item#system-
collections-objectmodel-collection-1-item\(system-int32\))| Gets or sets the
element at the specified index.  
(Унаследован от
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>)  
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
[Collection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.collection-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>)  
##  __См. также
#### Ссылки
[FileSignatureCollection - ](T_Tessa_Files_FileSignatureCollection.htm)
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
