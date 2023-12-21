# SynchronizedSuspendableObservableCollection<T> \- класс
Обощенная коллекция элементов поддерживающая синхронизированный доступ к
списку элементов с уведомлениями о изменении списка.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public class SynchronizedSuspendableObservableCollection<T> : IDisposable, 
    	IList<T>, ICollection<T>, IEnumerable<T>, IEnumerable, IList, 
    	ICollection, IReadOnlyList<T>, IReadOnlyCollection<T>, INotifyCollectionChanged, INotifyPropertyChanged
VB __Копировать
    <SerializableAttribute>
    Public Class SynchronizedSuspendableObservableCollection(Of T)
    	Implements IDisposable, IList(Of T), ICollection(Of T), 
    	IEnumerable(Of T), IEnumerable, IList, ICollection, IReadOnlyList(Of T), 
    	IReadOnlyCollection(Of T), INotifyCollectionChanged, INotifyPropertyChanged
C++ __Копировать
    [SerializableAttribute]
    generic<typename T>
    public ref class SynchronizedSuspendableObservableCollection : IDisposable, 
    	IList<T>, ICollection<T>, IEnumerable<T>, IEnumerable, IList, 
    	ICollection, IReadOnlyList<T>, IReadOnlyCollection<T>, INotifyCollectionChanged, INotifyPropertyChanged
F# __Копировать
     [<SerializableAttribute>]
    type SynchronizedSuspendableObservableCollection<'T> = 
        class
            interface IDisposable
            interface IList<'T>
            interface ICollection<'T>
            interface IEnumerable<'T>
            interface IEnumerable
            interface IList
            interface ICollection
            interface IReadOnlyList<'T>
            interface IReadOnlyCollection<'T>
            interface INotifyCollectionChanged
            interface INotifyPropertyChanged
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SynchronizedSuspendableObservableCollection<T>
Derived
[Tessa.UI.Views.Parameters.ViewParameters](T_Tessa_UI_Views_Parameters_ViewParameters.htm)
Implements
    [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<T>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<T>, [IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<T>, [IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<T>, [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<T>, [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.icollection), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IList](https://learn.microsoft.com/dotnet/api/system.collections.ilist), [INotifyCollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged), [INotifyPropertyChanged](https://learn.microsoft.com/dotnet/api/system.componentmodel.inotifypropertychanged), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
#### Параметры типа
T
     Тип элементов коллекции 
## __Конструкторы
[SynchronizedSuspendableObservableCollection<T>()](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1__ctor.htm)|
Initializes a new instance of the
SynchronizedSuspendableObservableCollection<T> class.  
---|---  
[SynchronizedSuspendableObservableCollection<T>(Action<Action>)](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1__ctor_1.htm)|
Initializes a new instance of the
SynchronizedSuspendableObservableCollection<T> class.  
[SynchronizedSuspendableObservableCollection<T>(IEnumerable<T>)](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1__ctor_2.htm)|
Initializes a new instance of the
SynchronizedSuspendableObservableCollection<T> class.  
[SynchronizedSuspendableObservableCollection<T>(IEnumerable<T>,
Action<Action>)](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1__ctor_3.htm)|
Initializes a new instance of the
SynchronizedSuspendableObservableCollection<T> class.  
## __Свойства
[Count](P_Tessa_UI_SynchronizedSuspendableObservableCollection_1_Count.htm)|
Gets the number of elements contained in the
[ICollection](https://learn.microsoft.com/dotnet/api/system.collections.icollection).  
---|---  
[ExecuteInContextAction](P_Tessa_UI_SynchronizedSuspendableObservableCollection_1_ExecuteInContextAction.htm)|
Gets Делегат осуществляющий выполнение уведомлений о наступлении событий в
заданом контексте  
[IsFixedSize](P_Tessa_UI_SynchronizedSuspendableObservableCollection_1_IsFixedSize.htm)|
Gets a value indicating whether Признак коллекции фиксированного размера .  
[IsReadOnly](P_Tessa_UI_SynchronizedSuspendableObservableCollection_1_IsReadOnly.htm)|
Gets a value indicating whether Признак коллекции только для чтения  
[IsSynchronized](P_Tessa_UI_SynchronizedSuspendableObservableCollection_1_IsSynchronized.htm)|
Gets a value indicating whether Признак потоко-безопасного доступа к элементам
коллекции  
[Item](P_Tessa_UI_SynchronizedSuspendableObservableCollection_1_Item.htm)|
Gets or sets the element at the specified index.  
[SyncRoot](P_Tessa_UI_SynchronizedSuspendableObservableCollection_1_SyncRoot.htm)|
Gets объект используемый для синхронизированного доступа к элементам коллекции  
## __Методы
[Add](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_Add.htm)| Adds
an item to the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
---|---  
[BlockReentrancy](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_BlockReentrancy.htm)|
Осуществляет блокировку повтороного вызова событий  
[CheckReentrancy](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_CheckReentrancy.htm)|
Проверяет возможность осуществления вызова обработчиков событий. В случае если
вызов обработчиков уже осуществляется вызывает исключение.
[InvalidOperationException](https://learn.microsoft.com/dotnet/api/system.invalidoperationexception)  
[Clear](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_Clear.htm)|
Removes all items from the
[IList](https://learn.microsoft.com/dotnet/api/system.collections.ilist).  
[Contains](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_Contains.htm)|
Determines whether the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)
contains a specific value.  
[CopyTo](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_CopyTo.htm)|
Copies the elements of the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)
to an [Array](https://learn.microsoft.com/dotnet/api/system.array), starting
at a particular [Array](https://learn.microsoft.com/dotnet/api/system.array)
index.  
[Dispose()](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_Dispose.htm)|
Performs application-defined tasks associated with freeing, releasing, or
resetting unmanaged resources.  
[Dispose(Boolean)](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_Dispose_1.htm)|
Осуществляет освобождение используемых ресурсов  
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
[GetEnumerator](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_GetEnumerator.htm)|
Returns an enumerator that iterates through the collection.  
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
[IndexOf](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_IndexOf.htm)|
Determines the index of a specific item in the
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1).  
[Insert](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_Insert.htm)|
Inserts an item to the
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)
at the specified index.  
[InvokeExecuteInContext](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_InvokeExecuteInContext.htm)|
Осуществляет вызов действия action в контексте заданном в
[ExecuteInContextAction](P_Tessa_UI_SynchronizedSuspendableObservableCollection_1_ExecuteInContextAction.htm)  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Move](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_Move.htm)|
Осуществляет перенос элемента из позиции oldIndex в позицию newIndex  
[OnCollectionChanged](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_OnCollectionChanged.htm)|
Вызывается при изменении коллекции элементов.  
[OnPropertyChanged](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_OnPropertyChanged.htm)|
Осуществляет вызов обработчиков изменения свойств объекта  
[Remove](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_Remove.htm)|
Removes the first occurrence of a specific object from the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
[RemoveAt](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_RemoveAt.htm)|
Removes the
[IList](https://learn.microsoft.com/dotnet/api/system.collections.ilist) item
at the specified index.  
[SuspendNotifications](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_SuspendNotifications.htm)|
Осуществляет блокировку вызова обработчиков событий изменения коллекции  
[ToArray](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_ToArray.htm)|
Создает новый массив и осуществляет копирование элементов в него  
[ToList](M_Tessa_UI_SynchronizedSuspendableObservableCollection_1_ToList.htm)|
Создает список и осуществляет копирование элементов в него  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[CollectionChanged](E_Tessa_UI_SynchronizedSuspendableObservableCollection_1_CollectionChanged.htm)|
Occurs when an item is added, removed, changed, moved, or the entire list is
refreshed.  
---|---  
[PropertyChanged](E_Tessa_UI_SynchronizedSuspendableObservableCollection_1_PropertyChanged.htm)|
Событие изменения свойств коллекции  
##  __Поля
[ItemsLocker](F_Tessa_UI_SynchronizedSuspendableObservableCollection_1_ItemsLocker.htm)|
The items locker.  
---|---  
## __Методы расширения
[AddRange<T>](M_Tessa_Platform_Collections_Extensions_AddRange__1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
---|---  
[AddRange<T>](M_Tessa_Platform_Collections_Extensions_AddRange__1_1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[AddRangeForList](M_Tessa_Platform_Collections_Extensions_AddRangeForList.htm)|
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
[InsertRangeForList](M_Tessa_Platform_Collections_Extensions_InsertRangeForList.htm)|
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
[RemoveAllForList](M_Tessa_Platform_Collections_Extensions_RemoveAllForList.htm)|
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
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
