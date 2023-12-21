# ArgumentEnumerator - класс
Supports parsing of command-line arguments and iterating over them.
## __Definition
 **Пространство имён:**
[Tessa.Platform.CommandLine](N_Tessa_Platform_CommandLine.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ArgumentEnumerator : IEnumerable<KeyValuePair<string, string>>, 
    	IEnumerable, IEnumerator<KeyValuePair<string, string>>, 
    	IEnumerator, IDisposable
VB __Копировать
     Public NotInheritable Class ArgumentEnumerator
    	Implements IEnumerable(Of KeyValuePair(Of String, String)), 
    	IEnumerable, IEnumerator(Of KeyValuePair(Of String, String)), 
    	IEnumerator, IDisposable
C++ __Копировать
     public ref class ArgumentEnumerator sealed : IEnumerable<KeyValuePair<String^, String^>>, 
    	IEnumerable, IEnumerator<KeyValuePair<String^, String^>>, 
    	IEnumerator, IDisposable
F# __Копировать
     [<SealedAttribute>]
    type ArgumentEnumerator = 
        class
            interface IEnumerable<KeyValuePair<string, string>>
            interface IEnumerable
            interface IEnumerator<KeyValuePair<string, string>>
            interface IEnumerator
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ArgumentEnumerator
Implements
    [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<[String](https://learn.microsoft.com/dotnet/api/system.string), [String](https://learn.microsoft.com/dotnet/api/system.string)>>, [IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerator-1)<[KeyValuePair](https://learn.microsoft.com/dotnet/api/system.collections.generic.keyvaluepair-2)<[String](https://learn.microsoft.com/dotnet/api/system.string), [String](https://learn.microsoft.com/dotnet/api/system.string)>>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [IEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.ienumerator), [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)
##  __Конструкторы
[ArgumentEnumerator(String)](M_Tessa_Platform_CommandLine_ArgumentEnumerator__ctor_2.htm)|
Initializes a new instance of the ArgumentEnumerator class with the specified
[String](https://learn.microsoft.com/dotnet/api/system.string) which
represents command-line arguments.  
---|---  
[ArgumentEnumerator(String[])](M_Tessa_Platform_CommandLine_ArgumentEnumerator__ctor_3.htm)|
Initializes a new instance of the ArgumentEnumerator class with the specified
array of [String](https://learn.microsoft.com/dotnet/api/system.string) each
represents a single command-line argument.  
[ArgumentEnumerator(Char,
String)](M_Tessa_Platform_CommandLine_ArgumentEnumerator__ctor.htm)|
Инициализирует новый экземпляр класса ArgumentEnumerator  
[ArgumentEnumerator(Char,
String[])](M_Tessa_Platform_CommandLine_ArgumentEnumerator__ctor_1.htm)|
Инициализирует новый экземпляр класса ArgumentEnumerator  
##  __Свойства
[Current](P_Tessa_Platform_CommandLine_ArgumentEnumerator_Current.htm)|  Gets
the current argument name/value pair in the collection.  
---|---  
[CurrentName](P_Tessa_Platform_CommandLine_ArgumentEnumerator_CurrentName.htm)|
Gets the current argument name in the collection.  
[CurrentValue](P_Tessa_Platform_CommandLine_ArgumentEnumerator_CurrentValue.htm)|
Gets the current argument value in the collection.  
[DefaultNamePrefix](P_Tessa_Platform_CommandLine_ArgumentEnumerator_DefaultNamePrefix.htm)|  
[Empty](P_Tessa_Platform_CommandLine_ArgumentEnumerator_Empty.htm)|  Gets an
empty ArgumentEnumerator.  
[NamePrefix](P_Tessa_Platform_CommandLine_ArgumentEnumerator_NamePrefix.htm)|  
## __Методы
[ContinueFromCurrent](M_Tessa_Platform_CommandLine_ArgumentEnumerator_ContinueFromCurrent.htm)|
Creates a continuation that enumerates arguments starting from current.  
---|---  
[Dispose](M_Tessa_Platform_CommandLine_ArgumentEnumerator_Dispose.htm)|
Releases all resources used by the current instance of the ArgumentEnumerator
class.  
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
[GetEnumerator](M_Tessa_Platform_CommandLine_ArgumentEnumerator_GetEnumerator.htm)|
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MoveNext](M_Tessa_Platform_CommandLine_ArgumentEnumerator_MoveNext.htm)|
Advances the enumerator to the next element of the collection.  
[Reset](M_Tessa_Platform_CommandLine_ArgumentEnumerator_Reset.htm)|  Sets the
enumerator to its initial position which is before the first element in the
collection.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[AsArray<KeyValuePair<String,
String>>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
---|---  
[ForEach<KeyValuePair<String,
String>>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<KeyValuePair<String, String>, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IndexOf<KeyValuePair<String,
String>>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|  Возвращает
индекс первого вхождения элемента в последовательность, определяемый
посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<KeyValuePair<String,
String>>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
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
[OrderByDependencies<KeyValuePair<String,
String>>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<KeyValuePair<String,
String>>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<KeyValuePair<String, String>,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<KeyValuePair<String, String>,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<KeyValuePair<String,
String>>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<KeyValuePair<String,
String>>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<KeyValuePair<String,
String>>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ToDictionaryAsync<KeyValuePair<String, String>, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToObservableCollection<KeyValuePair<String,
String>>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<KeyValuePair<String,
String>>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<KeyValuePair<String,
String>>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<KeyValuePair<String,
String>>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.CommandLine - пространство
имён](N_Tessa_Platform_CommandLine.htm)
