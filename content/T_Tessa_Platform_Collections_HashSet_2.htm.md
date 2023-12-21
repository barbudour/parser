# HashSet<TKey, TValue> \- класс
Хэш коллекция, сочетающая преимущества [IDictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)
и
[ISet<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iset-1).
При этом ключ строится на основе экземпляра [!:TValue].
## __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public class HashSet<TKey, TValue> : ISet<TValue>, 
    	ICollection<TValue>, IEnumerable<TValue>, IEnumerable, IReadOnlyCollection<TValue>
VB __Копировать
    <SerializableAttribute>
    Public Class HashSet(Of TKey, TValue)
    	Implements ISet(Of TValue), ICollection(Of TValue), 
    	IEnumerable(Of TValue), IEnumerable, IReadOnlyCollection(Of TValue)
C++ __Копировать
    [SerializableAttribute]
    generic<typename TKey, typename TValue>
    public ref class HashSet : ISet<TValue>, 
    	ICollection<TValue>, IEnumerable<TValue>, IEnumerable, IReadOnlyCollection<TValue>
F# __Копировать
     [<SerializableAttribute>]
    type HashSet<'TKey, 'TValue> = 
        class
            interface ISet<'TValue>
            interface ICollection<'TValue>
            interface IEnumerable<'TValue>
            interface IEnumerable
            interface IReadOnlyCollection<'TValue>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ HashSet<TKey, TValue>
Derived
[Tessa.Applications.Synchronization.LocalFileEntryCollection](T_Tessa_Applications_Synchronization_LocalFileEntryCollection.htm)
[Tessa.Localization.LocalizationEntryCollection](T_Tessa_Localization_LocalizationEntryCollection.htm)
[Tessa.Localization.LocalizationLibraryByIdentifierCollection](T_Tessa_Localization_LocalizationLibraryByIdentifierCollection.htm)
[Tessa.Localization.LocalizationLibraryByNameCollection](T_Tessa_Localization_LocalizationLibraryByNameCollection.htm)
[Tessa.Localization.LocalizationStringCollection](T_Tessa_Localization_LocalizationStringCollection.htm)
Implements
    [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<TValue>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<TValue>, [IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<TValue>, [ISet](https://learn.microsoft.com/dotnet/api/system.collections.generic.iset-1)<TValue>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)
#### Параметры типа
TKey
    Тип ключа.
TValue
    Тип хранимых элементов.
##  __Конструкторы
[HashSet<TKey, TValue>(Func<TValue, TKey>,
IEnumerable<TValue>)](M_Tessa_Platform_Collections_HashSet_2__ctor.htm)|
Создаёт хэш коллекцию с заданным ключом, содержащую переданные значения.  
---|---  
[HashSet<TKey, TValue>(Func<TValue, TKey>,
IEqualityComparer<TKey>)](M_Tessa_Platform_Collections_HashSet_2__ctor_1.htm)|
Создаёт пустую хэш коллекцию с заданным ключом и функцией сравнения ключей.  
[HashSet<TKey, TValue>(Func<TValue, TKey>,
Int32)](M_Tessa_Platform_Collections_HashSet_2__ctor_4.htm)|  Создаёт пустую
хэш коллекцию с заданным ключом и заданным начальным размером коллекции.  
[HashSet<TKey, TValue>(Func<TValue, TKey>, IEqualityComparer<TKey>,
IEnumerable<TValue>)](M_Tessa_Platform_Collections_HashSet_2__ctor_2.htm)|
Создаёт пустую хэш коллекцию с заданным ключом, функцией сравнения ключей и
заданными значениями.  
[HashSet<TKey, TValue>(Func<TValue, TKey>, IEqualityComparer<TKey>,
Int32)](M_Tessa_Platform_Collections_HashSet_2__ctor_3.htm)|  Создаёт пустую
хэш коллекцию с заданным ключом, функцией сравнения ключей и заданным
начальным размером коллекции.  
## __Свойства
[Count](P_Tessa_Platform_Collections_HashSet_2_Count.htm)|  Количество
элементов в коллекции.  
---|---  
[Item](P_Tessa_Platform_Collections_HashSet_2_Item.htm)|  Получить/установить
значение по заданному ключу.  
## __Методы
[Add](M_Tessa_Platform_Collections_HashSet_2_Add.htm)| Adds an element to the
current set and returns a value to indicate if the element was successfully
added.  
---|---  
[Clear](M_Tessa_Platform_Collections_HashSet_2_Clear.htm)| Removes all items
from the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
[Contains](M_Tessa_Platform_Collections_HashSet_2_Contains.htm)| Determines
whether the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)
contains a specific value.  
[ContainsKey](M_Tessa_Platform_Collections_HashSet_2_ContainsKey.htm)|
Проверить, содержится ли в коллекции элемент с заданным ключом.  
[CopyTo](M_Tessa_Platform_Collections_HashSet_2_CopyTo.htm)| Copies the
elements of the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)
to an [Array](https://learn.microsoft.com/dotnet/api/system.array), starting
at a particular [Array](https://learn.microsoft.com/dotnet/api/system.array)
index.  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ExceptWith](M_Tessa_Platform_Collections_HashSet_2_ExceptWith.htm)| Removes
all elements in the specified collection from the current set.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetEnumerator](M_Tessa_Platform_Collections_HashSet_2_GetEnumerator.htm)|
Получить энумератор для коллекции.  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetPairs](M_Tessa_Platform_Collections_HashSet_2_GetPairs.htm)|  Вернуть
коллекцию [KeyValuePair<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)
содержащихся в сете элементов.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IntersectWith](M_Tessa_Platform_Collections_HashSet_2_IntersectWith.htm)|
Modifies the current set so that it contains only elements that are also in a
specified collection.  
[IsProperSubsetOf](M_Tessa_Platform_Collections_HashSet_2_IsProperSubsetOf.htm)|
Determines whether the current set is a proper (strict) subset of a specified
collection.  
[IsProperSupersetOf](M_Tessa_Platform_Collections_HashSet_2_IsProperSupersetOf.htm)|
Determines whether the current set is a proper (strict) superset of a
specified collection.  
[IsSubsetOf](M_Tessa_Platform_Collections_HashSet_2_IsSubsetOf.htm)|
Determines whether a set is a subset of a specified collection.  
[IsSupersetOf](M_Tessa_Platform_Collections_HashSet_2_IsSupersetOf.htm)|
Determines whether the current set is a superset of a specified collection.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Overlaps](M_Tessa_Platform_Collections_HashSet_2_Overlaps.htm)| Determines
whether the current set overlaps with the specified collection.  
[Remove](M_Tessa_Platform_Collections_HashSet_2_Remove.htm)| Removes the first
occurrence of a specific object from the
[ICollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1).  
[RemoveByKey](M_Tessa_Platform_Collections_HashSet_2_RemoveByKey.htm)|
Удалить элемент с заданным ключом из коллекции.  
[Replace](M_Tessa_Platform_Collections_HashSet_2_Replace.htm)|  Заменить
элемент в коллекции.  
[SetEquals](M_Tessa_Platform_Collections_HashSet_2_SetEquals.htm)| Determines
whether the current set and the specified collection contain the same
elements.  
[SymmetricExceptWith](M_Tessa_Platform_Collections_HashSet_2_SymmetricExceptWith.htm)|
Modifies the current set so that it contains only elements that are present
either in the current set or in the specified collection, but not both.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetItem](M_Tessa_Platform_Collections_HashSet_2_TryGetItem.htm)|
Попробовать получить элемент по заданному ключу.  
[UnionWith](M_Tessa_Platform_Collections_HashSet_2_UnionWith.htm)| Modifies
the current set so that it contains all elements that are present in the
current set, in the specified collection, or in both.  
##  __Методы расширения
[AddRange<TValue>](M_Tessa_Platform_Collections_Extensions_AddRange__1_1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
---|---  
[AddRange<TValue>](M_Tessa_Platform_Collections_Extensions_AddRange__1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[AsArray<TValue>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[ConvertToListDictionaries<TValue>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления по умолчанию  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ConvertToListDictionaries<TValue>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1_1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления context  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ForEach<TValue>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<TValue, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IndexOf<TValue>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<TValue>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[OrderByDependencies<TValue>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<TValue>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<TValue,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<TValue,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<TValue>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<TValue>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RemoveRange<TValue>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1_1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<TValue>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<TValue>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ToDictionaryAsync<TValue, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToObservableCollection<TValue>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<TValue>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<TValue>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<TValue>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Collections - пространство
имён](N_Tessa_Platform_Collections.htm)
