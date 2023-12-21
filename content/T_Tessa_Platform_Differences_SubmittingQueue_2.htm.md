# SubmittingQueue<TObject, TItem> \- класс
##  __Definition
 **Пространство имён:**
[Tessa.Platform.Differences](N_Tessa_Platform_Differences.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class SubmittingQueue<TObject, TItem> : SubmittingQueue, 
    	IList<TItem>, ICollection<TItem>, IEnumerable<TItem>, IEnumerable
    where TItem : SubmittingQueueItem<TObject>
VB __Копировать
     Public MustInherit Class SubmittingQueue(Of TObject, TItem As SubmittingQueueItem(Of TObject))
    	Inherits SubmittingQueue
    	Implements IList(Of TItem), ICollection(Of TItem), 
    	IEnumerable(Of TItem), IEnumerable
C++ __Копировать
    generic<typename TObject, typename TItem>
    where TItem : SubmittingQueueItem<TObject>
    public ref class SubmittingQueue abstract : public SubmittingQueue, 
    	IList<TItem>, ICollection<TItem>, IEnumerable<TItem>, IEnumerable
F# __Копировать
     [<AbstractClassAttribute>]
    type SubmittingQueue<'TObject, 'TItem when 'TItem : SubmittingQueueItem<'TObject>> = 
        class
            inherit SubmittingQueue
            interface IList<'TItem>
            interface ICollection<'TItem>
            interface IEnumerable<'TItem>
            interface IEnumerable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm) __ SubmittingQueue<TObject, TItem>
Derived
[Tessa.Localization.Differences.LocalizationSubmittingQueue](T_Tessa_Localization_Differences_LocalizationSubmittingQueue.htm)
[Tessa.Scheme.Differences.SchemeSubmittingQueue](T_Tessa_Scheme_Differences_SchemeSubmittingQueue.htm)
Implements
    [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<TItem>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<TItem>, [IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<TItem>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)
#### Параметры типа
TObject
TItem
##  __Конструкторы
[SubmittingQueue<TObject,
TItem>](M_Tessa_Platform_Differences_SubmittingQueue_2__ctor.htm)|
Инициализирует новый экземпляр класса SubmittingQueue<TObject, TItem>  
---|---  
##  __Свойства
[Count](P_Tessa_Platform_Differences_SubmittingQueue_Count.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
---|---  
[Exception](P_Tessa_Platform_Differences_SubmittingQueue_Exception.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
[FaultedItem](P_Tessa_Platform_Differences_SubmittingQueue_FaultedItem.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
[Item](P_Tessa_Platform_Differences_SubmittingQueue_2_Item.htm)|  
[State](P_Tessa_Platform_Differences_SubmittingQueue_State.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
##  __Методы
[AddItem](M_Tessa_Platform_Differences_SubmittingQueue_AddItem.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
---|---  
[Contains(TItem)](M_Tessa_Platform_Differences_SubmittingQueue_2_Contains.htm)|  
[Contains(SubmittingQueueItem)](M_Tessa_Platform_Differences_SubmittingQueue_Contains.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
[CopyTo(TItem[],
Int32)](M_Tessa_Platform_Differences_SubmittingQueue_2_CopyTo.htm)|  
[CopyTo(SubmittingQueueItem[],
Int32)](M_Tessa_Platform_Differences_SubmittingQueue_CopyTo.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
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
[GetEnumerator](M_Tessa_Platform_Differences_SubmittingQueue_2_GetEnumerator.htm)|  
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
[IndexOf(TItem)](M_Tessa_Platform_Differences_SubmittingQueue_2_IndexOf.htm)|  
[IndexOf(SubmittingQueueItem)](M_Tessa_Platform_Differences_SubmittingQueue_IndexOf.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RefreshAsync](M_Tessa_Platform_Differences_SubmittingQueue_RefreshAsync.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
[RefreshCoreAsync](M_Tessa_Platform_Differences_SubmittingQueue_RefreshCoreAsync.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
[SetFaultedItem](M_Tessa_Platform_Differences_SubmittingQueue_SetFaultedItem.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
[SubmitAddedItemAsync](M_Tessa_Platform_Differences_SubmittingQueue_2_SubmitAddedItemAsync.htm)|  
[SubmitAsync](M_Tessa_Platform_Differences_SubmittingQueue_SubmitAsync.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
[SubmitCoreAsync](M_Tessa_Platform_Differences_SubmittingQueue_SubmitCoreAsync.htm)|  
(Унаследован от
[SubmittingQueue](T_Tessa_Platform_Differences_SubmittingQueue.htm))  
[SubmitItemAsync](M_Tessa_Platform_Differences_SubmittingQueue_2_SubmitItemAsync.htm)|  
(Переопределяет [SubmittingQueue.SubmitItemAsync(SubmittingQueueItem,
CancellationToken)](M_Tessa_Platform_Differences_SubmittingQueue_SubmitItemAsync.htm))  
[SubmitModifiedItemAsync](M_Tessa_Platform_Differences_SubmittingQueue_2_SubmitModifiedItemAsync.htm)|  
[SubmitRemovedItemAsync](M_Tessa_Platform_Differences_SubmittingQueue_2_SubmitRemovedItemAsync.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[AddRange<TItem>](M_Tessa_Platform_Collections_Extensions_AddRange__1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
---|---  
[AddRange<TItem>](M_Tessa_Platform_Collections_Extensions_AddRange__1_1.htm)|
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
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IndexOf<TItem>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<TItem>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_2.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начиная с заданного индекса и заканчивая последним
элементом.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<TItem>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<TItem>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_3.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начинающемся с заданного индекса и содержащем указанное
число элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InsertRange<TItem>](M_Tessa_Platform_Collections_Extensions_InsertRange__1.htm)|
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
[RemoveAll<TItem>](M_Tessa_Platform_Collections_Extensions_RemoveAll__1.htm)|
Удаляет все элементы, совпадающие по заданному предикату. Возвращает
количество удалённых элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<TItem>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<TItem>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1_1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<TItem>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
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
[Tessa.Platform.Differences - пространство
имён](N_Tessa_Platform_Differences.htm)
