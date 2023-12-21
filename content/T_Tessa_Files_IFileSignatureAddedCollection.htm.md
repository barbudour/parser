# IFileSignatureAddedCollection - интерфейс
Коллекция подписей для версии файла, которые были добавлены и ещё не были
сохранены.
## __Definition
 **Пространство имён:** [Tessa.Files](N_Tessa_Files.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IFileSignatureAddedCollection : IFileSignatureCollectionBase<IFileSignatureAddedCollection>, 
    	IFileEntityCollection<IFileSignature, IFileSignatureAddedCollection>, IObservableCollectionLookup<Guid, IFileSignature, IFileSignatureAddedCollection>, 
    	IObservableCollection<IFileSignature, IFileSignatureAddedCollection>, IList<IFileSignature>, 
    	ICollection<IFileSignature>, IEnumerable<IFileSignature>, IEnumerable, 
    	INotifyCollectionChanged, INotifyPropertyChanged, ICloneable, ILookupContainer<Guid, IFileSignature>, 
    	IControllableCollection<IFileSignature>
VB __Копировать
     Public Interface IFileSignatureAddedCollection
    	Inherits IFileSignatureCollectionBase(Of IFileSignatureAddedCollection), IFileEntityCollection(Of IFileSignature, IFileSignatureAddedCollection), 
    	IObservableCollectionLookup(Of Guid, IFileSignature, IFileSignatureAddedCollection), IObservableCollection(Of IFileSignature, IFileSignatureAddedCollection), 
    	IList(Of IFileSignature), ICollection(Of IFileSignature), IEnumerable(Of IFileSignature), 
    	IEnumerable, INotifyCollectionChanged, INotifyPropertyChanged, ICloneable, ILookupContainer(Of Guid, IFileSignature), 
    	IControllableCollection(Of IFileSignature)
C++ __Копировать
     public interface class IFileSignatureAddedCollection : IFileSignatureCollectionBase<IFileSignatureAddedCollection^>, 
    	IFileEntityCollection<IFileSignature^, IFileSignatureAddedCollection^>, IObservableCollectionLookup<Guid, IFileSignature^, IFileSignatureAddedCollection^>, 
    	IObservableCollection<IFileSignature^, IFileSignatureAddedCollection^>, IList<IFileSignature^>, 
    	ICollection<IFileSignature^>, IEnumerable<IFileSignature^>, IEnumerable, 
    	INotifyCollectionChanged, INotifyPropertyChanged, ICloneable, ILookupContainer<Guid, IFileSignature^>, 
    	IControllableCollection<IFileSignature^>
F# __Копировать
     type IFileSignatureAddedCollection = 
        interface
            interface IFileSignatureCollectionBase<IFileSignatureAddedCollection>
            interface IFileEntityCollection<IFileSignature, IFileSignatureAddedCollection>
            interface IObservableCollectionLookup<Guid, IFileSignature, IFileSignatureAddedCollection>
            interface IObservableCollection<IFileSignature, IFileSignatureAddedCollection>
            interface IList<IFileSignature>
            interface ICollection<IFileSignature>
            interface IEnumerable<IFileSignature>
            interface IEnumerable
            interface INotifyCollectionChanged
            interface INotifyPropertyChanged
            interface ICloneable
            interface ILookupContainer<Guid, IFileSignature>
            interface IControllableCollection<IFileSignature>
        end
Implements
    [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>, [IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [INotifyCollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged), [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [IFileEntityCollection](T_Tessa_Files_IFileEntityCollection_2.htm)<[IFileSignature](T_Tessa_Files_IFileSignature.htm), IFileSignatureAddedCollection>, [IFileSignatureCollectionBase](T_Tessa_Files_IFileSignatureCollectionBase_1.htm)<IFileSignatureAddedCollection>, [IControllableCollection](T_Tessa_Platform_Collections_IControllableCollection_1.htm)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>, [ILookupContainer](T_Tessa_Platform_Collections_ILookupContainer_2.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid), [IFileSignature](T_Tessa_Files_IFileSignature.htm)>, [IObservableCollection](T_Tessa_Platform_Collections_IObservableCollection_2.htm)<[IFileSignature](T_Tessa_Files_IFileSignature.htm), IFileSignatureAddedCollection>, [IObservableCollectionLookup](T_Tessa_Platform_Collections_IObservableCollectionLookup_3.htm)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid), [IFileSignature](T_Tessa_Files_IFileSignature.htm), IFileSignatureAddedCollection>
##  __Свойства
[Count](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.count#system-
collections-generic-icollection-1-count)| Gets the number of elements
contained in the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>)  
---|---  
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
##  __Методы
[Add](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.add#system-
collections-generic-icollection-1-add\(-0\))| Adds an item to the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>)  
---|---  
[AddChecked](M_Tessa_Platform_Collections_IControllableCollection_1_AddChecked.htm)|
Добавляет файл в коллекцию, если он проходит проверку в событии ItemChecking.  
(Унаследован от
[IControllableCollection<TItem>](T_Tessa_Platform_Collections_IControllableCollection_1.htm))  
[Clear](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.clear#system-
collections-generic-icollection-1-clear)| Removes all items from the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>)  
[Clone](M_Tessa_Platform_Collections_IObservableCollection_2_Clone.htm)|
Выполняет глубокое копирование коллекции со всеми её элементами. Если элементы
поддерживают [System.ICloneable], то они также клонируются.  
(Унаследован от [IObservableCollection<TItem,
TCollection>](T_Tessa_Platform_Collections_IObservableCollection_2.htm))  
[Contains(T)](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.contains#system-
collections-generic-icollection-1-contains\(-0\))| Determines whether the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)
contains a specific value.  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>)  
[Contains(TKey)](M_Tessa_Platform_Collections_ILookupContainer_2_Contains.htm)|
Возвращает признак того, что контейнер содержит хотя бы одно значение по
заданному ключу.  
(Унаследован от [ILookupContainer<TKey,
TValue>](T_Tessa_Platform_Collections_ILookupContainer_2.htm))  
[CopyTo](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.copyto#system-
collections-generic-icollection-1-copyto\(-0\(\)-system-int32\))| Copies the
elements of the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)
to an [Array](https://learn.microsoft.com/dotnet/api/system.array), starting
at a particular [Array](https://learn.microsoft.com/dotnet/api/system.array)
index.  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>)  
[GetAll](M_Tessa_Platform_Collections_ILookupContainer_2_GetAll.htm)|
Возвращает все значения, доступные по заданному ключу. Если таких значений
нет, то возвращается пустая коллекция.  
(Унаследован от [ILookupContainer<TKey,
TValue>](T_Tessa_Platform_Collections_ILookupContainer_2.htm))  
[GetEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1.getenumerator#system-
collections-generic-ienumerable-1-getenumerator)| Returns an enumerator that
iterates through the collection.  
(Унаследован от
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>)  
[IndexOf](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1.indexof#system-
collections-generic-ilist-1-indexof\(-0\))| Determines the index of a specific
item in the
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1).  
(Унаследован от
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>)  
[Insert](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1.insert#system-
collections-generic-ilist-1-insert\(system-int32-0\))| Inserts an item to the
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)
at the specified index.  
(Унаследован от
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>)  
[Remove(T)](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.remove#system-
collections-generic-icollection-1-remove\(-0\))| Removes the first occurrence
of a specific object from the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>)  
[Remove(TKey)](M_Tessa_Platform_Collections_ILookupContainer_2_Remove.htm)|
Удаляет одно из значений, содержащихся в контейнере по заданному ключу.
Возвращает признак того, что одно из значений было удалено.  
(Унаследован от [ILookupContainer<TKey,
TValue>](T_Tessa_Platform_Collections_ILookupContainer_2.htm))  
[RemoveAll](M_Tessa_Platform_Collections_ILookupContainer_2_RemoveAll.htm)|
Удаляет все значения, содержащиеся в контейнере по заданному ключу. Возвращает
признак того, что хотя бы одно из значений было удалено.  
(Унаследован от [ILookupContainer<TKey,
TValue>](T_Tessa_Platform_Collections_ILookupContainer_2.htm))  
[RemoveAt](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1.removeat#system-
collections-generic-ilist-1-removeat\(system-int32\))| Removes the
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)
item at the specified index.  
(Унаследован от
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IFileSignature](T_Tessa_Files_IFileSignature.htm)>)  
[RemoveChecked](M_Tessa_Platform_Collections_IControllableCollection_1_RemoveChecked.htm)|
Удаляет файл из коллекции, если он проходит проверку в событии ItemChecking.  
(Унаследован от
[IControllableCollection<TItem>](T_Tessa_Platform_Collections_IControllableCollection_1.htm))  
[TryGet](M_Tessa_Platform_Collections_ILookupContainer_2_TryGet.htm)|
Возвращает одно из значений по заданному ключу или null, если контейнер не
содержит значений.  
(Унаследован от [ILookupContainer<TKey,
TValue>](T_Tessa_Platform_Collections_ILookupContainer_2.htm))  
##  __События
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged.collectionchanged)|
Occurs when the collection changes.  
(Унаследован от
[INotifyCollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged))  
---|---  
[ItemChecking](E_Tessa_Platform_Collections_IControllableCollection_1_ItemChecking.htm)|
Событие, которое выполняется перед добавлением или удалением элемента в
методах AddChecked или RemoveChecked. В событии выполняемое действие можно
отменить.  
(Унаследован от
[IControllableCollection<TItem>](T_Tessa_Platform_Collections_IControllableCollection_1.htm))  
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
##  __Методы расширения
[AddRange<IFileSignature>](M_Tessa_Platform_Collections_Extensions_AddRange__1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
---|---  
[AddRange<IFileSignature>](M_Tessa_Platform_Collections_Extensions_AddRange__1_1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[AddWithNotificationAsync](M_Tessa_Files_FileExtensions_AddWithNotificationAsync_2.htm)|
Добавляет несколько подписей файла с уведомлением их источников Source. При
этом автоматически устанавливается свойство
[Added](P_Tessa_Files_IFileSignatureCollection_Added.htm), если тип коллекции
signatures задан соответствующий. Этот метод следует использовать для
стандартного добавления новых подписей.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[AddWithNotificationAsync](M_Tessa_Files_FileExtensions_AddWithNotificationAsync_3.htm)|
Добавляет подпись файла с уведомлением её источника Source. При этом
автоматически устанавливается свойство
[Added](P_Tessa_Files_IFileSignatureCollection_Added.htm), если тип коллекции
signatures задан соответствующий. Этот метод следует использовать для
стандартного добавления новой подписи.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[AsArray<IFileSignature>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[ConvertToListDictionaries<IFileSignature>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления по умолчанию  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ConvertToListDictionaries<IFileSignature>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1_1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления context  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ForEach<IFileSignature>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<IFileSignature, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<IFileSignature>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<IFileSignature>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<IFileSignature>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_2.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начиная с заданного индекса и заканчивая последним
элементом.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<IFileSignature>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_3.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начинающемся с заданного индекса и содержащем указанное
число элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InsertRange<IFileSignature>](M_Tessa_Platform_Collections_Extensions_InsertRange__1.htm)|
Вставляет диапазон элементов в заданный список items, начиная с указанного
индекса index.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<IFileSignature>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<IFileSignature>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<IFileSignature,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<IFileSignature,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<IFileSignature>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<IFileSignature>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RemoveAll<IFileSignature>](M_Tessa_Platform_Collections_Extensions_RemoveAll__1.htm)|
Удаляет все элементы, совпадающие по заданному предикату. Возвращает
количество удалённых элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<IFileSignature>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<IFileSignature>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1_1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveWithNotificationAsync](M_Tessa_Files_FileExtensions_RemoveWithNotificationAsync_2.htm)|
Удаляет подписи файла с уведомлением их источников Source. Этот метод следует
использовать для стандартного удаления подписей файла.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[RemoveWithNotificationAsync](M_Tessa_Files_FileExtensions_RemoveWithNotificationAsync_3.htm)|
Удаляет подпись файла с уведомлением её источника Source. Этот метод следует
использовать для стандартного удаления подписи файла.  
(Определяется [FileExtensions](T_Tessa_Files_FileExtensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<IFileSignature>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToDictionaryAsync<IFileSignature, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToObservableCollection<IFileSignature>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<IFileSignature>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<IFileSignature>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<IFileSignature>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Files - пространство имён](N_Tessa_Files.htm)
