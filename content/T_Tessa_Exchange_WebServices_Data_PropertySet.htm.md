# PropertySet - класс
Represents a set of item or folder properties. Property sets are used to
indicate what properties of an item or folder should be loaded when binding to
an existing item or folder or when loading an item or folder's properties.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class PropertySet : IEnumerable<PropertyDefinitionBase>, 
    	IEnumerable
VB __Копировать
     Public NotInheritable Class PropertySet
    	Implements IEnumerable(Of PropertyDefinitionBase), IEnumerable
C++ __Копировать
     public ref class PropertySet sealed : IEnumerable<PropertyDefinitionBase^>, 
    	IEnumerable
F# __Копировать
     [<SealedAttribute>]
    type PropertySet = 
        class
            interface IEnumerable<PropertyDefinitionBase>
            interface IEnumerable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ PropertySet
Implements
    [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<[PropertyDefinitionBase](T_Tessa_Exchange_WebServices_Data_PropertyDefinitionBase.htm)>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)
##  __Конструкторы
[PropertySet()](M_Tessa_Exchange_WebServices_Data_PropertySet__ctor.htm)|
Initializes a new instance of PropertySet based upon BasePropertySet.IdOnly.  
---|---  
[PropertySet(BasePropertySet)](M_Tessa_Exchange_WebServices_Data_PropertySet__ctor_2.htm)|
Initializes a new instance of PropertySet.  
[PropertySet(IEnumerable<PropertyDefinitionBase>)](M_Tessa_Exchange_WebServices_Data_PropertySet__ctor_1.htm)|
Initializes a new instance of PropertySet based upon BasePropertySet.IdOnly.  
[PropertySet(PropertyDefinitionBase[])](M_Tessa_Exchange_WebServices_Data_PropertySet__ctor_5.htm)|
Initializes a new instance of PropertySet based upon BasePropertySet.IdOnly.  
[PropertySet(BasePropertySet,
IEnumerable<PropertyDefinitionBase>)](M_Tessa_Exchange_WebServices_Data_PropertySet__ctor_3.htm)|
Initializes a new instance of PropertySet.  
[PropertySet(BasePropertySet,
PropertyDefinitionBase[])](M_Tessa_Exchange_WebServices_Data_PropertySet__ctor_4.htm)|
Initializes a new instance of PropertySet.  
## __Свойства
[AddBlankTargetToLinks](P_Tessa_Exchange_WebServices_Data_PropertySet_AddBlankTargetToLinks.htm)|
Gets or sets value indicating whether or not to add blank target attribute to
anchor links.  
---|---  
[BasePropertySet](P_Tessa_Exchange_WebServices_Data_PropertySet_BasePropertySet.htm)|
Gets or sets the base property set the property set is based upon.  
[BlockExternalImages](P_Tessa_Exchange_WebServices_Data_PropertySet_BlockExternalImages.htm)|
Gets or sets value indicating whether or not to convert inline images to data
URLs.  
[ConvertHtmlCodePageToUTF8](P_Tessa_Exchange_WebServices_Data_PropertySet_ConvertHtmlCodePageToUTF8.htm)|
Gets or sets value indicating whether or not to convert HTML code page to UTF8
encoding.  
[Count](P_Tessa_Exchange_WebServices_Data_PropertySet_Count.htm)|  Gets the
number of explicitly added properties in this set.  
[FilterHtmlContent](P_Tessa_Exchange_WebServices_Data_PropertySet_FilterHtmlContent.htm)|
Gets or sets value indicating whether or not to filter potentially unsafe HTML
content from message bodies.  
[InlineImageUrlTemplate](P_Tessa_Exchange_WebServices_Data_PropertySet_InlineImageUrlTemplate.htm)|
Gets or sets a value of the URL template to use for the src attribute of
inline IMG elements.  
[Item](P_Tessa_Exchange_WebServices_Data_PropertySet_Item.htm)|  Gets the
[PropertyDefinitionBase](T_Tessa_Exchange_WebServices_Data_PropertyDefinitionBase.htm)
at the specified index.  
[MaximumBodySize](P_Tessa_Exchange_WebServices_Data_PropertySet_MaximumBodySize.htm)|
Gets or sets the maximum size of the body to be retrieved.  
[RequestedBodyType](P_Tessa_Exchange_WebServices_Data_PropertySet_RequestedBodyType.htm)|
Gets or sets type of body that should be loaded on items. If RequestedBodyType
is null, body is returned as HTML if available, plain text otherwise.  
[RequestedNormalizedBodyType](P_Tessa_Exchange_WebServices_Data_PropertySet_RequestedNormalizedBodyType.htm)|
Gets or sets type of normalized body that should be loaded on items. If null,
the should return the same value as body type.  
[RequestedUniqueBodyType](P_Tessa_Exchange_WebServices_Data_PropertySet_RequestedUniqueBodyType.htm)|
Gets or sets type of body that should be loaded on items. If null, the should
return the same value as body type.  
## __Методы
[Add](M_Tessa_Exchange_WebServices_Data_PropertySet_Add.htm)|  Adds the
specified property to the property set.  
---|---  
[AddRange](M_Tessa_Exchange_WebServices_Data_PropertySet_AddRange.htm)|  Adds
the specified properties to the property set.  
[Clear](M_Tessa_Exchange_WebServices_Data_PropertySet_Clear.htm)|  Remove all
explicitly added properties from the property set.  
[Contains](M_Tessa_Exchange_WebServices_Data_PropertySet_Contains.htm)|
Determines whether the specified property has been explicitly added to this
property set using the Add or AddRange methods.  
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
[GetEnumerator](M_Tessa_Exchange_WebServices_Data_PropertySet_GetEnumerator.htm)|
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
[Remove](M_Tessa_Exchange_WebServices_Data_PropertySet_Remove.htm)|  Removes
the specified property from the set.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Операторы
[ Implicit(BasePropertySet to
PropertySet)](M_Tessa_Exchange_WebServices_Data_PropertySet_op_Implicit.htm)|
Implements an implicit conversion between PropertySet and BasePropertySet.  
---|---  
## __Поля
[FirstClassProperties](F_Tessa_Exchange_WebServices_Data_PropertySet_FirstClassProperties.htm)|
Returns a predefined property set that includes the first class properties of
an item or folder.  
---|---  
[IdOnly](F_Tessa_Exchange_WebServices_Data_PropertySet_IdOnly.htm)|  Returns a
predefined property set that only includes the Id property.  
## __Методы расширения
[AsArray<PropertyDefinitionBase>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
---|---  
[ConvertToListDictionaries<PropertyDefinitionBase>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления по умолчанию  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ConvertToListDictionaries<PropertyDefinitionBase>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1_1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления context  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ForEach<PropertyDefinitionBase>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<PropertyDefinitionBase, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IndexOf<PropertyDefinitionBase>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<PropertyDefinitionBase>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
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
[OrderByDependencies<PropertyDefinitionBase>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<PropertyDefinitionBase>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<PropertyDefinitionBase,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<PropertyDefinitionBase,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<PropertyDefinitionBase>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<PropertyDefinitionBase>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<PropertyDefinitionBase>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ToDictionaryAsync<PropertyDefinitionBase, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToObservableCollection<PropertyDefinitionBase>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<PropertyDefinitionBase>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<PropertyDefinitionBase>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<PropertyDefinitionBase>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
