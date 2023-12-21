# WeakDictionary<TKey, TValue> \- класс
##  __Definition
 **Пространство имён:**
[Tessa.Platform.Collections](N_Tessa_Platform_Collections.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class WeakDictionary<TKey, TValue> : IDictionary<TKey, TValue>, 
    	ICollection<KeyValuePair<TKey, TValue>>, IEnumerable<KeyValuePair<TKey, TValue>>, 
    	IEnumerable, IReadOnlyDictionary<TKey, TValue>, IReadOnlyCollection<KeyValuePair<TKey, TValue>>
    where TKey : class
VB __Копировать
     Public Class WeakDictionary(Of TKey As Class, TValue)
    	Implements IDictionary(Of TKey, TValue), ICollection(Of KeyValuePair(Of TKey, TValue)), 
    	IEnumerable(Of KeyValuePair(Of TKey, TValue)), IEnumerable, 
    	IReadOnlyDictionary(Of TKey, TValue), IReadOnlyCollection(Of KeyValuePair(Of TKey, TValue))
C++ __Копировать
    generic<typename TKey, typename TValue>
    where TKey : ref class
    public ref class WeakDictionary : IDictionary<TKey, TValue>, 
    	ICollection<KeyValuePair<TKey, TValue>>, IEnumerable<KeyValuePair<TKey, TValue>>, 
    	IEnumerable, IReadOnlyDictionary<TKey, TValue>, IReadOnlyCollection<KeyValuePair<TKey, TValue>>
F# __Копировать
     type WeakDictionary<'TKey, 'TValue when 'TKey : not struct> = 
        class
            interface IDictionary<'TKey, 'TValue>
            interface ICollection<KeyValuePair<'TKey, 'TValue>>
            interface IEnumerable<KeyValuePair<'TKey, 'TValue>>
            interface IEnumerable
            interface IReadOnlyDictionary<'TKey, 'TValue>
            interface IReadOnlyCollection<KeyValuePair<'TKey, 'TValue>>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ WeakDictionary<TKey, TValue>
Implements
    [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<TKey, TValue>>, [IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)<TKey, TValue>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<TKey, TValue>>, [IReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlycollection-1)<[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<TKey, TValue>>, [IReadOnlyDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary-2)<TKey, TValue>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)
#### Параметры типа
TKey
TValue
##  __Конструкторы
[WeakDictionary<TKey,
TValue>()](M_Tessa_Platform_Collections_WeakDictionary_2__ctor.htm)|
Инициализирует новый экземпляр класса WeakDictionary<TKey, TValue>  
---|---  
[WeakDictionary<TKey, TValue>(IDictionary<TKey,
TValue>)](M_Tessa_Platform_Collections_WeakDictionary_2__ctor_1.htm)|
Инициализирует новый экземпляр класса WeakDictionary<TKey, TValue>  
[WeakDictionary<TKey,
TValue>(Int32)](M_Tessa_Platform_Collections_WeakDictionary_2__ctor_2.htm)|
Инициализирует новый экземпляр класса WeakDictionary<TKey, TValue>  
##  __Свойства
[Count](P_Tessa_Platform_Collections_WeakDictionary_2_Count.htm)|  
---|---  
[Item](P_Tessa_Platform_Collections_WeakDictionary_2_Item.htm)|  
[Keys](P_Tessa_Platform_Collections_WeakDictionary_2_Keys.htm)|  
[Values](P_Tessa_Platform_Collections_WeakDictionary_2_Values.htm)|  
## __Методы
[Add](M_Tessa_Platform_Collections_WeakDictionary_2_Add.htm)|  
---|---  
[Clear](M_Tessa_Platform_Collections_WeakDictionary_2_Clear.htm)|  
[ContainsKey](M_Tessa_Platform_Collections_WeakDictionary_2_ContainsKey.htm)|  
[ContainsValue](M_Tessa_Platform_Collections_WeakDictionary_2_ContainsValue.htm)|  
[CopyTo](M_Tessa_Platform_Collections_WeakDictionary_2_CopyTo.htm)|  
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
[GetEnumerator](M_Tessa_Platform_Collections_WeakDictionary_2_GetEnumerator.htm)|  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Remove](M_Tessa_Platform_Collections_WeakDictionary_2_Remove.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetValue](M_Tessa_Platform_Collections_WeakDictionary_2_TryGetValue.htm)|  
## __Методы расширения
[AddRange<KeyValuePair<TKey,
TValue>>](M_Tessa_Platform_Collections_Extensions_AddRange__1.htm)|  Добавляет
значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
---|---  
[AddRange<KeyValuePair<TKey,
TValue>>](M_Tessa_Platform_Collections_Extensions_AddRange__1_1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[AsArray<KeyValuePair<TKey,
TValue>>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[ForEach<KeyValuePair<TKey,
TValue>>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<KeyValuePair<TKey, TValue>, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IndexOf<KeyValuePair<TKey,
TValue>>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|  Возвращает
индекс первого вхождения элемента в последовательность, определяемый
посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<KeyValuePair<TKey,
TValue>>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
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
[OrderByDependencies<KeyValuePair<TKey,
TValue>>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<KeyValuePair<TKey,
TValue>>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<KeyValuePair<TKey, TValue>,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<KeyValuePair<TKey, TValue>,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<KeyValuePair<TKey,
TValue>>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<KeyValuePair<TKey,
TValue>>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RemoveRange<KeyValuePair<TKey,
TValue>>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<KeyValuePair<TKey,
TValue>>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1_1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<KeyValuePair<TKey,
TValue>>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ToDictionaryAsync<KeyValuePair<TKey, TValue>, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToObservableCollection<KeyValuePair<TKey,
TValue>>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<KeyValuePair<TKey,
TValue>>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<KeyValuePair<TKey,
TValue>>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<KeyValuePair<TKey,
TValue>>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Collections - пространство
имён](N_Tessa_Platform_Collections.htm)
