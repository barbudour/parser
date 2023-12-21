# SealableList<T> \- класс
Список, поддерживающий защиту от изменений.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public class SealableList<T> : IList<T>, 
    	ICollection<T>, IEnumerable<T>, IEnumerable, IList, ICollection, 
    	IReadOnlyList<T>, IReadOnlyCollection<T>, ISealable, INotifyCollectionChanged
VB __Копировать
    <SerializableAttribute>
    Public Class SealableList(Of T)
    	Implements IList(Of T), ICollection(Of T), 
    	IEnumerable(Of T), IEnumerable, IList, ICollection, IReadOnlyList(Of T), 
    	IReadOnlyCollection(Of T), ISealable, INotifyCollectionChanged
C++ __Копировать
    [SerializableAttribute]
    generic<typename T>
    public ref class SealableList : IList<T>, 
    	ICollection<T>, IEnumerable<T>, IEnumerable, IList, ICollection, 
    	IReadOnlyList<T>, IReadOnlyCollection<T>, ISealable, INotifyCollectionChanged
F# __Копировать
     [<SerializableAttribute>]
    type SealableList<'T> = 
        class
            interface IList<'T>
            interface ICollection<'T>
            interface IEnumerable<'T>
            interface IEnumerable
            interface IList
            interface ICollection
            interface IReadOnlyList<'T>
            interface IReadOnlyCollection<'T>
            interface ISealable
            interface INotifyCollectionChanged
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SealableList<T>
Derived
[Tessa.Platform.Collections.SealableObjectList<T>](T_Tessa_Platform_Collections_SealableObjectList_1.htm)
[Tessa.UI.Cards.FormViewModelCollection](T_Tessa_UI_Cards_FormViewModelCollection.htm)
Implements
    [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<T>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<T>, [IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<T>, [IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<T>, [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)<T>, [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.icollection), [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IList](https://learn.microsoft.com/dotnet/api/system.collections.ilist), [INotifyCollectionChanged](https://learn.microsoft.com/dotnet/api/system.collections.specialized.inotifycollectionchanged), [ISealable](T_Tessa_Platform_ISealable.htm)
#### Параметры типа
T
    Тип элементов списка.
##  __Конструкторы
[SealableList<T>()](M_Tessa_Platform_Collections_SealableList_1__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
[SealableList<T>(Boolean)](M_Tessa_Platform_Collections_SealableList_1__ctor_1.htm)|
Создаёт экземпляр класса с указанием признака того, что объект должен быть
защищён от изменений.  
[SealableList<T>(IEnumerable<T>)](M_Tessa_Platform_Collections_SealableList_1__ctor_2.htm)|
Создаёт экземпляр класса с указанием коллекции элементов, используемой для
инициализации списка.  
[SealableList<T>(Int32)](M_Tessa_Platform_Collections_SealableList_1__ctor_4.htm)|
Создаёт экземпляр класса с указанием начальной вместимости списка.  
[SealableList<T>(IEnumerable<T>,
Boolean)](M_Tessa_Platform_Collections_SealableList_1__ctor_3.htm)|  Создаёт
экземпляр класса с указанием коллекции элементов, используемой для
инициализации списка, и признака того, что объект должен быть защищён от
изменений.  
## __Свойства
[Count](P_Tessa_Platform_Collections_SealableList_1_Count.htm)| Количество
элементов в коллекции.  
---|---  
[IsSealed](P_Tessa_Platform_Collections_SealableList_1_IsSealed.htm)| Признак
того, что объект был защищён от изменений.  
[Item](P_Tessa_Platform_Collections_SealableList_1_Item.htm)| Получает или
задаёт элемент по отсчитываемому от нуля индексу.  
##  __Методы
[Add](M_Tessa_Platform_Collections_SealableList_1_Add.htm)| Добавляет заданный
элемент в коллекцию.  
---|---  
[AddInternal](M_Tessa_Platform_Collections_SealableList_1_AddInternal.htm)|
Добавляет заданный элемент в коллекцию без проверки на защиту объекта от
изменений.
Метод может быть переопределён в классах-наследниках.  
[CheckSealed](M_Tessa_Platform_Collections_SealableList_1_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
[Clear](M_Tessa_Platform_Collections_SealableList_1_Clear.htm)| Удаляет все
элементы коллекции.  
[ClearInternal](M_Tessa_Platform_Collections_SealableList_1_ClearInternal.htm)|
Удаляет все элементы из коллекции без проверки на защиту объекта от изменений.
Метод может быть переопределён в классах-наследниках.  
[Contains](M_Tessa_Platform_Collections_SealableList_1_Contains.htm)|
Возвращает признак того, что заданный элемент содержится в коллекции.  
[CopyTo](M_Tessa_Platform_Collections_SealableList_1_CopyTo.htm)| Копирует
элементы коллекции в массив, начиная с заданного отсчитываемого от нуля
индекса.  
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
[GetEnumerator](M_Tessa_Platform_Collections_SealableList_1_GetEnumerator.htm)|
Возвращает итератор по элементам коллекции.  
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
[IndexOf](M_Tessa_Platform_Collections_SealableList_1_IndexOf.htm)| Возвращает
отсчитываемый от нуля индекс заданного элемента в коллекции.  
[Insert](M_Tessa_Platform_Collections_SealableList_1_Insert.htm)| Вставляет
элемент в заданную позицию.  
[InsertInternal](M_Tessa_Platform_Collections_SealableList_1_InsertInternal.htm)|
Вставляет элемент в заданную позицию без проверки на защиту объекта от
изменений.
Метод может быть переопределён в классах-наследниках.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Remove](M_Tessa_Platform_Collections_SealableList_1_Remove.htm)| Удаляет
заданный элемент из коллекции.  
[RemoveAt](M_Tessa_Platform_Collections_SealableList_1_RemoveAt.htm)| Удаляет
элемент в заданной позиции.  
[RemoveAtInternal](M_Tessa_Platform_Collections_SealableList_1_RemoveAtInternal.htm)|
Удаляет элемент в заданной позиции без проверки на защиту объекта от
изменений.  
[RemoveInternal](M_Tessa_Platform_Collections_SealableList_1_RemoveInternal.htm)|
Удаляет заданный элемент из коллекции без проверки на защиту объекта от
изменений.
Метод может быть переопределён в классах-наследниках.  
[Seal](M_Tessa_Platform_Collections_SealableList_1_Seal.htm)| Защищает объект
от изменений.  
[SealInternal](M_Tessa_Platform_Collections_SealableList_1_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.  
[SetInternal](M_Tessa_Platform_Collections_SealableList_1_SetInternal.htm)|
Устанавливает элемент по отсчитываемому от нуля индексу без проверки на защиту
объекта от изменений.
Метод может быть переопределён в классах-наследниках.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[CollectionChanged](E_Tessa_Platform_Collections_SealableList_1_CollectionChanged.htm)|
Событие, уведомляющее об изменении коллекции у модели представления.  
---|---  
##  __Методы расширения
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
[Tessa.Platform.Collections - пространство
имён](N_Tessa_Platform_Collections.htm)
