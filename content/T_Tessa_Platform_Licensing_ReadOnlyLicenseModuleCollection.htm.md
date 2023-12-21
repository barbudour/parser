# ReadOnlyLicenseModuleCollection - класс
Коллекция модулей, подключенных в лицензии
[ILicense](T_Tessa_Platform_Licensing_ILicense.htm), доступная только для
чтения.
## __Definition
 **Пространство имён:**
[Tessa.Platform.Licensing](N_Tessa_Platform_Licensing.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ReadOnlyLicenseModuleCollection : ReadOnlyCollection<ILicenseModule>, 
    	ILicenseModuleCollection, IList<ILicenseModule>, ICollection<ILicenseModule>, 
    	IEnumerable<ILicenseModule>, IEnumerable
VB __Копировать
     Public NotInheritable Class ReadOnlyLicenseModuleCollection
    	Inherits ReadOnlyCollection(Of ILicenseModule)
    	Implements ILicenseModuleCollection, IList(Of ILicenseModule), 
    	ICollection(Of ILicenseModule), IEnumerable(Of ILicenseModule), IEnumerable
C++ __Копировать
     public ref class ReadOnlyLicenseModuleCollection sealed : public ReadOnlyCollection<ILicenseModule^>, 
    	ILicenseModuleCollection, IList<ILicenseModule^>, ICollection<ILicenseModule^>, 
    	IEnumerable<ILicenseModule^>, IEnumerable
F# __Копировать
     [<SealedAttribute>]
    type ReadOnlyLicenseModuleCollection = 
        class
            inherit ReadOnlyCollection<ILicenseModule>
            interface ILicenseModuleCollection
            interface IList<ILicenseModule>
            interface ICollection<ILicenseModule>
            interface IEnumerable<ILicenseModule>
            interface IEnumerable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)> __ ReadOnlyLicenseModuleCollection
Implements
    [ICollection](https://learn.microsoft.com/dotnet/api/system.collections.generic.icollection-1)<[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)>, [IList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)<[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable), [ILicenseModuleCollection](T_Tessa_Platform_Licensing_ILicenseModuleCollection.htm)
##  __Конструкторы
[ReadOnlyLicenseModuleCollection](M_Tessa_Platform_Licensing_ReadOnlyLicenseModuleCollection__ctor.htm)|
Создаёт экземпляр коллекции с указанием входящих в неё модулей.  
---|---  
## __Свойства
[Count](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.count#system-
collections-objectmodel-readonlycollection-1-count)| Gets the number of
elements contained in the
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)
instance.  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)>)  
---|---  
[Item[Guid]](P_Tessa_Platform_Licensing_ReadOnlyLicenseModuleCollection_Item.htm)|
Возвращает модуль лицензии по его идентификатору.  
[Item[Int32]](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.item#system-
collections-objectmodel-readonlycollection-1-item\(system-int32\))| Gets the
element at the specified index.  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)>)  
[Items](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.items#system-
collections-objectmodel-readonlycollection-1-items)| Returns the
[IList<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ilist-1)
that the
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)
wraps.  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)>)  
##  __Методы
[Contains(Guid)](M_Tessa_Platform_Licensing_ReadOnlyLicenseModuleCollection_Contains.htm)|
Возвращает признак того, что в лицензию включён модуль с заданным
идентификатором.  
---|---  
[Contains(T)](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.contains#system-
collections-objectmodel-readonlycollection-1-contains\(-0\))| Determines
whether an element is in the
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1).  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)>)  
[CopyTo](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.copyto#system-
collections-objectmodel-readonlycollection-1-copyto\(-0\(\)-system-int32\))|
Copies the entire
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)
to a compatible one-dimensional
[Array](https://learn.microsoft.com/dotnet/api/system.array), starting at the
specified index of the target array.  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)>)  
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
[GetEnumerator](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.getenumerator#system-
collections-objectmodel-readonlycollection-1-getenumerator)| Returns an
enumerator that iterates through the
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1).  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)>)  
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
[IndexOf](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1.indexof#system-
collections-objectmodel-readonlycollection-1-indexof\(-0\))| Searches for the
specified object and returns the zero-based index of the first occurrence
within the entire
[ReadOnlyCollection<T>](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1).  
(Унаследован от
[ReadOnlyCollection](https://learn.microsoft.com/dotnet/api/system.collections.objectmodel.readonlycollection-1)<[ILicenseModule](T_Tessa_Platform_Licensing_ILicenseModule.htm)>)  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToReadOnly](M_Tessa_Platform_Licensing_ReadOnlyLicenseModuleCollection_ToReadOnly.htm)|
Возвращает доступную только для чтения обёртку для текущего состояния текущего
объекта. При изменении текущего объекта возвращённая обёртка не изменяется.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGet](M_Tessa_Platform_Licensing_ReadOnlyLicenseModuleCollection_TryGet.htm)|
Возвращает модуль лицензии по его идентификатору или null, если
соответствующий модуль отсутствует.  
## __Методы расширения
[AddRange<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_AddRange__1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
---|---  
[AddRange<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_AddRange__1_1.htm)|
Добавляет значения items в коллекцию collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[AsArray<ILicenseModule>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[ConvertToListDictionaries<ILicenseModule>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления по умолчанию  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ConvertToListDictionaries<ILicenseModule>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1_1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления context  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ForEach<ILicenseModule>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<ILicenseModule, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[HasEnterpriseOrContains](M_Tessa_Platform_Licensing_LicensingExtensions_HasEnterpriseOrContains.htm)|
Возвращает признак того, что коллекция содержит модуль лицензии с указанным
идентификатором moduleID или что лицензия является Enterprise-редакцией, в
соответствии с которой модуль должен быть добавлен автоматически.  
(Определяется
[LicensingExtensions](T_Tessa_Platform_Licensing_LicensingExtensions.htm))  
[IndexOf<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного компаратора
[IEqualityComparer<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1).  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_2.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начиная с заданного индекса и заканчивая последним
элементом.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_3.htm)|
Выполняет поиск элемента, удовлетворяющего условиям указанного предиката, и
возвращает отсчитываемый от нуля индекс первого вхождения в диапазоне
элементов списка, начинающемся с заданного индекса и содержащем указанное
число элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[InsertRange<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_InsertRange__1.htm)|
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
[OrderByDependencies<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<ILicenseModule,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<ILicenseModule,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<ILicenseModule>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<ILicenseModule>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RemoveAll<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_RemoveAll__1.htm)|
Удаляет все элементы, совпадающие по заданному предикату. Возвращает
количество удалённых элементов.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RemoveRange<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_RemoveRange__1_1.htm)|
Удаляет значения items из коллекции collection.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<ILicenseModule>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ToDictionaryAsync<ILicenseModule, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToLicenseModuleCollection](M_Tessa_Platform_Licensing_LicensingExtensions_ToLicenseModuleCollection.htm)|
Преобразует тип объекта
[ILicenseModuleCollection](T_Tessa_Platform_Licensing_ILicenseModuleCollection.htm)
в
[LicenseModuleCollection](T_Tessa_Platform_Licensing_LicenseModuleCollection.htm)
или создаёт новый объект
[LicenseModuleCollection](T_Tessa_Platform_Licensing_LicenseModuleCollection.htm),
свойства которого получены из заданного объекта.  
(Определяется
[LicensingExtensions](T_Tessa_Platform_Licensing_LicensingExtensions.htm))  
[ToObservableCollection<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<ILicenseModule>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<ILicenseModule>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<ILicenseModule>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Licensing - пространство имён](N_Tessa_Platform_Licensing.htm)
