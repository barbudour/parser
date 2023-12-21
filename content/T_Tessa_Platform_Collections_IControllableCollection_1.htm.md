# IControllableCollection<TItem> \- интерфейс
Коллекция объектов, для которой опционально контролируется добавление и
удаление.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IControllableCollection<TItem> : ICollection<TItem>, 
    	IEnumerable<TItem>, IEnumerable
    where TItem : class
VB __Копировать
     Public Interface IControllableCollection(Of TItem As Class)
    	Inherits ICollection(Of TItem), IEnumerable(Of TItem), 
    	IEnumerable
C++ __Копировать
    generic<typename TItem>
    where TItem : ref class
    public interface class IControllableCollection : ICollection<TItem>, 
    	IEnumerable<TItem>, IEnumerable
F# __Копировать
     type IControllableCollection<'TItem when 'TItem : not struct> = 
        interface
            interface ICollection<'TItem>
            interface IEnumerable<'TItem>
            interface IEnumerable
        end
Implements
    [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<TItem>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<TItem>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)
#### Параметры типа
TItem
    Ссылочный тип проверямого элемента.
##  __Свойства
[Count](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.count#system-
collections-generic-icollection-1-count)| Gets the number of elements
contained in the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<TItem>)  
---|---  
[IsReadOnly](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.isreadonly#system-
collections-generic-icollection-1-isreadonly)| Gets a value indicating whether
the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)
is read-only.  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<TItem>)  
##  __Методы
[Add](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.add#system-
collections-generic-icollection-1-add\(-0\))| Adds an item to the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<TItem>)  
---|---  
[AddChecked](M_Tessa_Platform_Collections_IControllableCollection_1_AddChecked.htm)|
Добавляет файл в коллекцию, если он проходит проверку в событии ItemChecking.  
[Clear](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.clear#system-
collections-generic-icollection-1-clear)| Removes all items from the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<TItem>)  
[Contains](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.contains#system-
collections-generic-icollection-1-contains\(-0\))| Determines whether the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)
contains a specific value.  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<TItem>)  
[CopyTo](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.copyto#system-
collections-generic-icollection-1-copyto\(-0\(\)-system-int32\))| Copies the
elements of the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)
to an [Array](https://learn.microsoft.com/dotnet/api/system.array), starting
at a particular [Array](https://learn.microsoft.com/dotnet/api/system.array)
index.  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<TItem>)  
[GetEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1.getenumerator#system-
collections-generic-ienumerable-1-getenumerator)| Returns an enumerator that
iterates through the collection.  
(Унаследован от
[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<TItem>)  
[Remove](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1.remove#system-
collections-generic-icollection-1-remove\(-0\))| Removes the first occurrence
of a specific object from the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
(Унаследован от
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<TItem>)  
[RemoveChecked](M_Tessa_Platform_Collections_IControllableCollection_1_RemoveChecked.htm)|
Удаляет файл из коллекции, если он проходит проверку в событии ItemChecking.  
## __События
[ItemChecking](E_Tessa_Platform_Collections_IControllableCollection_1_ItemChecking.htm)|
Событие, которое выполняется перед добавлением или удалением элемента в
методах AddChecked или RemoveChecked. В событии выполняемое действие можно
отменить.  
---|---  
## __Методы расширения
[AddRange<TItem>](M_Tessa_Platform_Collections_Extensions_AddRange__1_1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
---|---  
[AddRange<TItem>](M_Tessa_Platform_Collections_Extensions_AddRange__1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[AsArray<TItem>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[ConvertToListDictionaries<TItem>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления по умолчанию  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ConvertToListDictionaries<TItem>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1_1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления context  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ForEach<TItem>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<TItem, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<TItem>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<TItem>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<TItem>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<TItem>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<TItem,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<TItem,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<TItem>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<TItem>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RemoveRange<TItem>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1_1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<TItem>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<TItem>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToDictionaryAsync<TItem, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToObservableCollection<TItem>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<TItem>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<TItem>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<TItem>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Collections - пространство
имён](N_Tessa_Platform_Collections.htm)
