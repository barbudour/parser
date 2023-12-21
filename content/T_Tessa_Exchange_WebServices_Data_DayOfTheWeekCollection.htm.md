# DayOfTheWeekCollection - класс
Represents a collection of DayOfTheWeek values.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class DayOfTheWeekCollection : ComplexProperty, 
    	IEnumerable<DayOfTheWeek>, IEnumerable
VB __Копировать
     Public NotInheritable Class DayOfTheWeekCollection
    	Inherits ComplexProperty
    	Implements IEnumerable(Of DayOfTheWeek), IEnumerable
C++ __Копировать
     public ref class DayOfTheWeekCollection sealed : public ComplexProperty, 
    	IEnumerable<DayOfTheWeek>, IEnumerable
F# __Копировать
     [<SealedAttribute>]
    type DayOfTheWeekCollection = 
        class
            inherit ComplexProperty
            interface IEnumerable<DayOfTheWeek>
            interface IEnumerable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __ DayOfTheWeekCollection
Implements
    [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[DayOfTheWeek](T_Tessa_Exchange_WebServices_Data_DayOfTheWeek.htm)>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)
##  __Свойства
[Count](P_Tessa_Exchange_WebServices_Data_DayOfTheWeekCollection_Count.htm)|
Gets the number of days in the collection.  
---|---  
[Item](P_Tessa_Exchange_WebServices_Data_DayOfTheWeekCollection_Item.htm)|
Gets the DayOfTheWeek at a specific index in the collection.  
## __Методы
[Add](M_Tessa_Exchange_WebServices_Data_DayOfTheWeekCollection_Add.htm)|  Adds
a day to the collection if it is not already present.  
---|---  
[AddRange](M_Tessa_Exchange_WebServices_Data_DayOfTheWeekCollection_AddRange.htm)|
Adds multiple days to the collection if they are not already present.  
[Clear](M_Tessa_Exchange_WebServices_Data_DayOfTheWeekCollection_Clear.htm)|
Clears the collection.  
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
[GetEnumerator](M_Tessa_Exchange_WebServices_Data_DayOfTheWeekCollection_GetEnumerator.htm)|
Gets an enumerator that iterates through the elements of the collection.  
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
[Remove](M_Tessa_Exchange_WebServices_Data_DayOfTheWeekCollection_Remove.htm)|
Remove a specific day from the collection.  
[RemoveAt](M_Tessa_Exchange_WebServices_Data_DayOfTheWeekCollection_RemoveAt.htm)|
Removes the day at a specific index.  
[ToString](M_Tessa_Exchange_WebServices_Data_DayOfTheWeekCollection_ToString.htm)|
Builds string representation of the collection.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
##  __Методы расширения
[AsArray<DayOfTheWeek>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
---|---  
[ForEach<DayOfTheWeek>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<DayOfTheWeek, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IndexOf<DayOfTheWeek>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<DayOfTheWeek>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
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
[OrderByDependencies<DayOfTheWeek>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<DayOfTheWeek>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<DayOfTheWeek,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<DayOfTheWeek,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<DayOfTheWeek>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<DayOfTheWeek>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<DayOfTheWeek>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ToDictionaryAsync<DayOfTheWeek, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToObservableCollection<DayOfTheWeek>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<DayOfTheWeek>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<DayOfTheWeek>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<DayOfTheWeek>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
