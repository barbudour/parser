# ViewModelContainer<T> \- класс
Контейнер для моделей представления, доступных по имени.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public class ViewModelContainer<T> : IViewModelContainer<T>, 
    	IEnumerable<KeyValuePair<string, T>>, IEnumerable, ICloneable, 
    	ISealable
    where T : class, INotifyPropertyChanged
VB __Копировать
     Public Class ViewModelContainer(Of T As {Class, INotifyPropertyChanged})
    	Implements IViewModelContainer(Of T), IEnumerable(Of KeyValuePair(Of String, T)), 
    	IEnumerable, ICloneable, ISealable
C++ __Копировать
    generic<typename T>
    where T : ref class, INotifyPropertyChanged
    public ref class ViewModelContainer : IViewModelContainer<T>, 
    	IEnumerable<KeyValuePair<String^, T>>, IEnumerable, ICloneable, 
    	ISealable
F# __Копировать
     type ViewModelContainer<'T when 'T : not struct and INotifyPropertyChanged> = 
        class
            interface IViewModelContainer<'T>
            interface IEnumerable<KeyValuePair<string, 'T>>
            interface IEnumerable
            interface ICloneable
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ViewModelContainer<T>
Implements
    [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<[String](https://learn.microsoft.com/dotnet/api/system.string), T>>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [ISealable](T_Tessa_Platform_ISealable.htm), [IViewModelContainer](T_Tessa_UI_IViewModelContainer_1.htm)<T>
#### Параметры типа
T
    Тип моделей представления, содержащихся в контейнере.
##  __Конструкторы
[ViewModelContainer<T>()](M_Tessa_UI_ViewModelContainer_1__ctor.htm)| Создаёт
экземпляр класса с параметрами по умолчанию.  
---|---  
[ViewModelContainer<T>(IViewModelContainer<T>)](M_Tessa_UI_ViewModelContainer_1__ctor_1.htm)|
Создаёт экземпляр класса, являющийся полной копией заданного контейнера.  
## __Свойства
[Count](P_Tessa_UI_ViewModelContainer_1_Count.htm)| Число моделей
представления, зарегистрированных в контейнере.  
---|---  
[IsSealed](P_Tessa_UI_ViewModelContainer_1_IsSealed.htm)| Признак того, что
объект был защищён от изменений.  
[Item](P_Tessa_UI_ViewModelContainer_1_Item.htm)| Получает или задаёт модель
представления, доступную по заданному имени.  
##  __Методы
[CheckSealed](M_Tessa_UI_ViewModelContainer_1_CheckSealed.htm)|  Выбрасывает
исключение [Tessa.Platform.ObjectSealedException], если объект был защищён от
изменений.  
---|---  
[Clone](M_Tessa_UI_ViewModelContainer_1_Clone.htm)| Создаёт полную копию
контейнера.  
[Contains(String)](M_Tessa_UI_ViewModelContainer_1_Contains.htm)| Возвращает
признак того, что модель представления с заданным именем присутствует в
контейнере.  
[Contains(T)](M_Tessa_UI_ViewModelContainer_1_Contains_1.htm)| Возвращает
признак того, что заданная модель представления присутствует в контейнере.  
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
[Get<TResult>](M_Tessa_UI_ViewModelContainer_1_Get__1.htm)|  Возвращает модель
представления, доступную по заданному имени и с указанным типом. Выбрасывает
исключение, если модель представления не найдена или её тип не соответствует
указанному типу TResult.  
[GetEnumerator](M_Tessa_UI_ViewModelContainer_1_GetEnumerator.htm)| Возвращает
итератор по элементам коллекции.  
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
[Seal](M_Tessa_UI_ViewModelContainer_1_Seal.htm)| Защищает объект от
изменений.  
[SealInternal](M_Tessa_UI_ViewModelContainer_1_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGet(String)](M_Tessa_UI_ViewModelContainer_1_TryGet.htm)|  Пытается
получить модель представления, доступную по заданному имени. Возвращает null,
если модель представления не найдена.  
[TryGet(String, T)](M_Tessa_UI_ViewModelContainer_1_TryGet_1.htm)| Пытается
получить модель представления, доступную по заданному имени.  
[TryGet<TResult>(String)](M_Tessa_UI_ViewModelContainer_1_TryGet__1.htm)|
Пытается получить модель представления, доступную по заданному имени.
Возвращает null, если модель представления не найдена.  
## __Методы расширения
[AsArray<KeyValuePair<String,
T>>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
---|---  
[ForEach<KeyValuePair<String,
T>>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<KeyValuePair<String, T>, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IndexOf<KeyValuePair<String,
T>>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|  Возвращает
индекс первого вхождения элемента в последовательность, определяемый
посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<KeyValuePair<String,
T>>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|  Возвращает
индекс первого вхождения элемента в последовательность, определяемый
посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[OrderByDependencies<KeyValuePair<String,
T>>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<KeyValuePair<String,
T>>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<KeyValuePair<String, T>,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<KeyValuePair<String, T>,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<KeyValuePair<String,
T>>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|  Сортирует
значения последовательности по возрастанию по локализованному ключу, который
определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<KeyValuePair<String,
T>>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<KeyValuePair<String,
T>>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ToDictionaryAsync<KeyValuePair<String, T>, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToObservableCollection<KeyValuePair<String,
T>>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<KeyValuePair<String,
T>>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<KeyValuePair<String,
T>>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<KeyValuePair<String,
T>>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
