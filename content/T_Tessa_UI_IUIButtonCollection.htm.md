# IUIButtonCollection - интерфейс
Коллекция кнопок диалогового окна [UIDialog](T_Tessa_UI_UIDialog.htm).
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IUIButtonCollection : IObservableCollection<IUIButton, IUIButtonCollection>, 
    	IList<IUIButton>, ICollection<IUIButton>, IEnumerable<IUIButton>, 
    	IEnumerable, INotifyCollectionChanged, INotifyPropertyChanged, ICloneable
VB __Копировать
     Public Interface IUIButtonCollection
    	Inherits IObservableCollection(Of IUIButton, IUIButtonCollection), IList(Of IUIButton), 
    	ICollection(Of IUIButton), IEnumerable(Of IUIButton), IEnumerable, 
    	INotifyCollectionChanged, INotifyPropertyChanged, ICloneable
C++ __Копировать
     public interface class IUIButtonCollection : IObservableCollection<IUIButton^, IUIButtonCollection^>, 
    	IList<IUIButton^>, ICollection<IUIButton^>, IEnumerable<IUIButton^>, 
    	IEnumerable, INotifyCollectionChanged, INotifyPropertyChanged, ICloneable
F# __Копировать
     type IUIButtonCollection = 
        interface
            interface IObservableCollection<IUIButton, IUIButtonCollection>
            interface IList<IUIButton>
            interface ICollection<IUIButton>
            interface IEnumerable<IUIButton>
            interface IEnumerable
            interface INotifyCollectionChanged
            interface INotifyPropertyChanged
            interface ICloneable
        end
Implements
    [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IUIButton](T_Tessa_UI_IUIButton.htm)>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[IUIButton](T_Tessa_UI_IUIButton.htm)>, [IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IUIButton](T_Tessa_UI_IUIButton.htm)>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [INotifyCollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged), [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [IObservableCollection](T_Tessa_Platform_Collections_IObservableCollection_2.htm)<[IUIButton](T_Tessa_UI_IUIButton.htm), IUIButtonCollection>
##  __Свойства
[Count](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.count#system-
collections-generic-icollection-1-count)| Gets the number of elements
contained in the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IUIButton](T_Tessa_UI_IUIButton.htm)>)  
---|---  
[IsReadOnly](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.isreadonly#system-
collections-generic-icollection-1-isreadonly)| Gets a value indicating whether
the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)
is read-only.  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IUIButton](T_Tessa_UI_IUIButton.htm)>)  
[Item](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1.item#system-
collections-generic-ilist-1-item\(system-int32\))| Gets or sets the element at
the specified index.  
(Унаследован от
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IUIButton](T_Tessa_UI_IUIButton.htm)>)  
##  __Методы
[Add](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.add#system-
collections-generic-icollection-1-add\(-0\))| Adds an item to the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IUIButton](T_Tessa_UI_IUIButton.htm)>)  
---|---  
[Clear](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.clear#system-
collections-generic-icollection-1-clear)| Removes all items from the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IUIButton](T_Tessa_UI_IUIButton.htm)>)  
[Clone](M_Tessa_Platform_Collections_IObservableCollection_2_Clone.htm)|
Выполняет глубокое копирование коллекции со всеми её элементами. Если элементы
поддерживают [System.ICloneable], то они также клонируются.  
(Унаследован от [IObservableCollection<TItem,
TCollection>](T_Tessa_Platform_Collections_IObservableCollection_2.htm))  
[Contains](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.contains#system-
collections-generic-icollection-1-contains\(-0\))| Determines whether the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)
contains a specific value.  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IUIButton](T_Tessa_UI_IUIButton.htm)>)  
[CopyTo](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.copyto#system-
collections-generic-icollection-1-copyto\(-0\(\)-system-int32\))| Copies the
elements of the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)
to an [Array](https://learn.microsoft.com/dotnet/api/system.array), starting
at a particular [Array](https://learn.microsoft.com/dotnet/api/system.array)
index.  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IUIButton](T_Tessa_UI_IUIButton.htm)>)  
[GetEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1.getenumerator#system-
collections-generic-ienumerable-1-getenumerator)| Returns an enumerator that
iterates through the collection.  
(Унаследован от
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[IUIButton](T_Tessa_UI_IUIButton.htm)>)  
[IndexOf](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1.indexof#system-
collections-generic-ilist-1-indexof\(-0\))| Determines the index of a specific
item in the
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1).  
(Унаследован от
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IUIButton](T_Tessa_UI_IUIButton.htm)>)  
[Insert](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1.insert#system-
collections-generic-ilist-1-insert\(system-int32-0\))| Inserts an item to the
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)
at the specified index.  
(Унаследован от
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IUIButton](T_Tessa_UI_IUIButton.htm)>)  
[Remove](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.remove#system-
collections-generic-icollection-1-remove\(-0\))| Removes the first occurrence
of a specific object from the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[IUIButton](T_Tessa_UI_IUIButton.htm)>)  
[RemoveAt](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1.removeat#system-
collections-generic-ilist-1-removeat\(system-int32\))| Removes the
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)
item at the specified index.  
(Унаследован от
[IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[IUIButton](T_Tessa_UI_IUIButton.htm)>)  
##  __События
[CollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged.collectionchanged)|
Occurs when the collection changes.  
(Унаследован от
[INotifyCollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged))  
---|---  
[PropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged.propertychanged)|
Occurs when a property value changes.  
(Унаследован от
[INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged))  
##  __Методы расширения
[AddRange<IUIButton>](M_Tessa_Platform_Collections_Extensions_AddRange__1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
---|---  
[AddRange<IUIButton>](M_Tessa_Platform_Collections_Extensions_AddRange__1_1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[AsArray<IUIButton>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[ConvertToListDictionaries<IUIButton>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления по умолчанию  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ConvertToListDictionaries<IUIButton>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1_1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления context  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ForEach<IUIButton>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<IUIButton, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<IUIButton>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<IUIButton>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_2.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начиная с заданного индекса и заканчивая последним
элементом.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<IUIButton>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<IUIButton>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_3.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начинающемся с заданного индекса и содержащем указанное
число элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InsertRange<IUIButton>](M_Tessa_Platform_Collections_Extensions_InsertRange__1.htm)|
Вставляет диапазон элементов в заданный список items, начиная с указанного
индекса index.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<IUIButton>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<IUIButton>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<IUIButton,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<IUIButton,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<IUIButton>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<IUIButton>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RemoveAll<IUIButton>](M_Tessa_Platform_Collections_Extensions_RemoveAll__1.htm)|
Удаляет все элементы, совпадающие по заданному предикату. Возвращает
количество удалённых элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<IUIButton>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<IUIButton>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1_1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<IUIButton>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToDictionaryAsync<IUIButton, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToObservableCollection<IUIButton>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<IUIButton>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<IUIButton>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<IUIButton>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
