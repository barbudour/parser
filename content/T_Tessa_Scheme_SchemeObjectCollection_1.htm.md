# SchemeObjectCollection<T> \- класс
##  __Definition
 **Пространство имён:** [Tessa.Scheme](N_Tessa_Scheme.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class SchemeObjectCollection<T> : IList<T>, 
    	ICollection<T>, IEnumerable<T>, IEnumerable, IReadOnlyList<T>, IReadOnlyCollection<T>, 
    	INotifyCollectionChanged, INotifyPropertyChanged
    where T : SchemeObject
VB __Копировать
     Public MustInherit Class SchemeObjectCollection(Of T As SchemeObject)
    	Implements IList(Of T), ICollection(Of T), 
    	IEnumerable(Of T), IEnumerable, IReadOnlyList(Of T), IReadOnlyCollection(Of T), 
    	INotifyCollectionChanged, INotifyPropertyChanged
C++ __Копировать
    generic<typename T>
    where T : SchemeObject
    public ref class SchemeObjectCollection abstract : IList<T>, 
    	ICollection<T>, IEnumerable<T>, IEnumerable, IReadOnlyList<T>, IReadOnlyCollection<T>, 
    	INotifyCollectionChanged, INotifyPropertyChanged
F# __Копировать
     [<AbstractClassAttribute>]
    type SchemeObjectCollection<'T when 'T : SchemeObject> = 
        class
            interface IList<'T>
            interface ICollection<'T>
            interface IEnumerable<'T>
            interface IEnumerable
            interface IReadOnlyList<'T>
            interface IReadOnlyCollection<'T>
            interface INotifyCollectionChanged
            interface INotifyPropertyChanged
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SchemeObjectCollection<T>
Derived
[Tessa.Scheme.SchemeForeignKeyColumnCollection](T_Tessa_Scheme_SchemeForeignKeyColumnCollection.htm)
[Tessa.Scheme.SchemeIncludedColumnCollection](T_Tessa_Scheme_SchemeIncludedColumnCollection.htm)
[Tessa.Scheme.SchemeIndexedColumnCollection](T_Tessa_Scheme_SchemeIndexedColumnCollection.htm)
[Tessa.Scheme.SchemeNamedObjectCollection<T>](T_Tessa_Scheme_SchemeNamedObjectCollection_1.htm)
[Tessa.Scheme.SchemeRecordCollection](T_Tessa_Scheme_SchemeRecordCollection.htm)
Implements
    [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<T>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<T>, [IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<T>, [IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<T>, [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<T>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [INotifyCollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged), [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged)
#### Параметры типа
T
##  __Свойства
[Count](P_Tessa_Scheme_SchemeObjectCollection_1_Count.htm)|  
---|---  
[IsSealed](P_Tessa_Scheme_SchemeObjectCollection_1_IsSealed.htm)|  
[Item](P_Tessa_Scheme_SchemeObjectCollection_1_Item.htm)|  
[Parent](P_Tessa_Scheme_SchemeObjectCollection_1_Parent.htm)|  
## __Методы
[Add](M_Tessa_Scheme_SchemeObjectCollection_1_Add.htm)|  
---|---  
[CheckIsSealed](M_Tessa_Scheme_SchemeObjectCollection_1_CheckIsSealed.htm)|  
[Clear](M_Tessa_Scheme_SchemeObjectCollection_1_Clear.htm)|  
[ClearItems](M_Tessa_Scheme_SchemeObjectCollection_1_ClearItems.htm)|  
[Construct](M_Tessa_Scheme_SchemeObjectCollection_1_Construct.htm)|  
[Contains](M_Tessa_Scheme_SchemeObjectCollection_1_Contains.htm)|  
[Copy](M_Tessa_Scheme_SchemeObjectCollection_1_Copy.htm)|  
[CopyTo](M_Tessa_Scheme_SchemeObjectCollection_1_CopyTo.htm)|  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetEnumerator](M_Tessa_Scheme_SchemeObjectCollection_1_GetEnumerator.htm)|  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[HaveSameKey](M_Tessa_Scheme_SchemeObjectCollection_1_HaveSameKey.htm)|  
[IndexOf](M_Tessa_Scheme_SchemeObjectCollection_1_IndexOf.htm)|  
[Insert](M_Tessa_Scheme_SchemeObjectCollection_1_Insert.htm)|  
[InsertItem](M_Tessa_Scheme_SchemeObjectCollection_1_InsertItem.htm)|  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MoveItem](M_Tessa_Scheme_SchemeObjectCollection_1_MoveItem.htm)|  
[Remove](M_Tessa_Scheme_SchemeObjectCollection_1_Remove.htm)|  
[RemoveAt](M_Tessa_Scheme_SchemeObjectCollection_1_RemoveAt.htm)|  
[RemoveItem](M_Tessa_Scheme_SchemeObjectCollection_1_RemoveItem.htm)|  
[ReplaceItem](M_Tessa_Scheme_SchemeObjectCollection_1_ReplaceItem.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetItem(Func<T, Int32, Boolean>,
T)](M_Tessa_Scheme_SchemeObjectCollection_1_TryGetItem.htm)|  
[TryGetItem(Int32,
T)](M_Tessa_Scheme_SchemeObjectCollection_1_TryGetItem_1.htm)|  
[ValidateInsertingItem](M_Tessa_Scheme_SchemeObjectCollection_1_ValidateInsertingItem.htm)|  
[ValidateItemUniqueness](M_Tessa_Scheme_SchemeObjectCollection_1_ValidateItemUniqueness.htm)|  
[ValidateRemovingItem](M_Tessa_Scheme_SchemeObjectCollection_1_ValidateRemovingItem.htm)|  
## __События
[CollectionChanged](E_Tessa_Scheme_SchemeObjectCollection_1_CollectionChanged.htm)|  
---|---  
[PropertyChanged](E_Tessa_Scheme_SchemeObjectCollection_1_PropertyChanged.htm)|  
## __Методы расширения
[AddRange<T>](M_Tessa_Platform_Collections_Extensions_AddRange__1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
---|---  
[AddRange<T>](M_Tessa_Platform_Collections_Extensions_AddRange__1_1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[AsArray<T>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[ConvertToListDictionaries<T>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления по умолчанию  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ConvertToListDictionaries<T>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1_1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления context  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ForEach<T>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<T, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IndexOf<T>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<T>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_2.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начиная с заданного индекса и заканчивая последним
элементом.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<T>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<T>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_3.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начинающемся с заданного индекса и содержащем указанное
число элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InsertRange<T>](M_Tessa_Platform_Collections_Extensions_InsertRange__1.htm)|
Вставляет диапазон элементов в заданный список items, начиная с указанного
индекса index.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IsolatedClone<T>](M_Tessa_Scheme_IEnumerableExtensions_IsolatedClone__1.htm)|  
(Определяется
[IEnumerableExtensions](T_Tessa_Scheme_IEnumerableExtensions.htm))  
[LastIndexOf<T>](M_Tessa_Platform_Collections_Extensions_LastIndexOf__1.htm)|
Возвращает индекс последнего вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[LastIndexOf<T>](M_Tessa_Platform_Collections_Extensions_LastIndexOf__1_1.htm)|
Возвращает индекс последнего вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<T>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<T>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<T,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<T,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<T>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<T>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RemoveAll<T>](M_Tessa_Platform_Collections_Extensions_RemoveAll__1.htm)|
Удаляет все элементы, совпадающие по заданному предикату. Возвращает
количество удалённых элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<T>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<T>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1_1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<T>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ToDictionaryAsync<T, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToObservableCollection<T>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<T>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<T>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<T>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Scheme - пространство имён](N_Tessa_Scheme.htm)
