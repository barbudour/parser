# ComplexPropertyCollection<TComplexProperty> \- класс
Represents a collection of properties that can be sent to and retrieved from
EWS.
## __Definition
 **Пространство имён:**
[Tessa.Exchange.WebServices.Data](N_Tessa_Exchange_WebServices_Data.htm)  
 **Сборка:** Tessa.Server (в Tessa.Server.dll) Версия: 3.6.0.17
C# __Копировать
    [EditorBrowsableAttribute(EditorBrowsableState.Never)]
    public abstract class ComplexPropertyCollection<TComplexProperty> : ComplexProperty, 
    	IEnumerable<TComplexProperty>, IEnumerable
    where TComplexProperty : ComplexProperty
VB __Копировать
    <EditorBrowsableAttribute(EditorBrowsableState.Never)>
    Public MustInherit Class ComplexPropertyCollection(Of TComplexProperty As ComplexProperty)
    	Inherits ComplexProperty
    	Implements IEnumerable(Of TComplexProperty), IEnumerable
C++ __Копировать
    [EditorBrowsableAttribute(EditorBrowsableState::Never)]
    generic<typename TComplexProperty>
    where TComplexProperty : ComplexProperty
    public ref class ComplexPropertyCollection abstract : public ComplexProperty, 
    	IEnumerable<TComplexProperty>, IEnumerable
F# __Копировать
     [<AbstractClassAttribute>]
    [<EditorBrowsableAttribute(EditorBrowsableState.Never)>]
    type ComplexPropertyCollection<'TComplexProperty when 'TComplexProperty : ComplexProperty> = 
        class
            inherit ComplexProperty
            interface IEnumerable<'TComplexProperty>
            interface IEnumerable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ComplexProperty](T_Tessa_Exchange_WebServices_Data_ComplexProperty.htm) __ ComplexPropertyCollection<TComplexProperty>
Derived
[Tessa.Exchange.WebServices.Data.AddressEntityCollection](T_Tessa_Exchange_WebServices_Data_AddressEntityCollection.htm)
[Tessa.Exchange.WebServices.Data.AttachmentCollection](T_Tessa_Exchange_WebServices_Data_AttachmentCollection.htm)
[Tessa.Exchange.WebServices.Data.AttendeeCollection](T_Tessa_Exchange_WebServices_Data_AttendeeCollection.htm)
[Tessa.Exchange.WebServices.Data.AttributedStringCollection](T_Tessa_Exchange_WebServices_Data_AttributedStringCollection.htm)
[Tessa.Exchange.WebServices.Data.AttributionCollection](T_Tessa_Exchange_WebServices_Data_AttributionCollection.htm)
[Tessa.Exchange.WebServices.Data.CompanyInsightValueCollection](T_Tessa_Exchange_WebServices_Data_CompanyInsightValueCollection.htm)
[Tessa.Exchange.WebServices.Data.ComputedInsightValuePropertyCollection](T_Tessa_Exchange_WebServices_Data_ComputedInsightValuePropertyCollection.htm)
[Tessa.Exchange.WebServices.Data.ContactEntityCollection](T_Tessa_Exchange_WebServices_Data_ContactEntityCollection.htm)
[Tessa.Exchange.WebServices.Data.ContactPhoneEntityCollection](T_Tessa_Exchange_WebServices_Data_ContactPhoneEntityCollection.htm)
[Tessa.Exchange.WebServices.Data.ConversationNodeCollection](T_Tessa_Exchange_WebServices_Data_ConversationNodeCollection.htm)
[Tessa.Exchange.WebServices.Data.DeletedOccurrenceInfoCollection](T_Tessa_Exchange_WebServices_Data_DeletedOccurrenceInfoCollection.htm)
[Tessa.Exchange.WebServices.Data.EmailAddressCollection](T_Tessa_Exchange_WebServices_Data_EmailAddressCollection.htm)
[Tessa.Exchange.WebServices.Data.EmailAddressEntityCollection](T_Tessa_Exchange_WebServices_Data_EmailAddressEntityCollection.htm)
[Tessa.Exchange.WebServices.Data.EmailUserEntityCollection](T_Tessa_Exchange_WebServices_Data_EmailUserEntityCollection.htm)
[Tessa.Exchange.WebServices.Data.ExtendedPropertyCollection](T_Tessa_Exchange_WebServices_Data_ExtendedPropertyCollection.htm)
[Tessa.Exchange.WebServices.Data.FolderIdCollection](T_Tessa_Exchange_WebServices_Data_FolderIdCollection.htm)
[Tessa.Exchange.WebServices.Data.FolderPermissionCollection](T_Tessa_Exchange_WebServices_Data_FolderPermissionCollection.htm)
[Tessa.Exchange.WebServices.Data.GroupMemberCollection](T_Tessa_Exchange_WebServices_Data_GroupMemberCollection.htm)
[Tessa.Exchange.WebServices.Data.InsightValueCollection](T_Tessa_Exchange_WebServices_Data_InsightValueCollection.htm)
[Tessa.Exchange.WebServices.Data.InternetMessageHeaderCollection](T_Tessa_Exchange_WebServices_Data_InternetMessageHeaderCollection.htm)
[Tessa.Exchange.WebServices.Data.ItemIdCollection](T_Tessa_Exchange_WebServices_Data_ItemIdCollection.htm)
[Tessa.Exchange.WebServices.Data.JobInsightValueCollection](T_Tessa_Exchange_WebServices_Data_JobInsightValueCollection.htm)
[Tessa.Exchange.WebServices.Data.MeetingSuggestionCollection](T_Tessa_Exchange_WebServices_Data_MeetingSuggestionCollection.htm)
[Tessa.Exchange.WebServices.Data.OccurrenceInfoCollection](T_Tessa_Exchange_WebServices_Data_OccurrenceInfoCollection.htm)
[Tessa.Exchange.WebServices.Data.PersonaEmailAddressCollection](T_Tessa_Exchange_WebServices_Data_PersonaEmailAddressCollection.htm)
[Tessa.Exchange.WebServices.Data.PersonInsightCollection](T_Tessa_Exchange_WebServices_Data_PersonInsightCollection.htm)
[Tessa.Exchange.WebServices.Data.PhoneEntityCollection](T_Tessa_Exchange_WebServices_Data_PhoneEntityCollection.htm)
[Tessa.Exchange.WebServices.Data.ProfileInsightValueCollection](T_Tessa_Exchange_WebServices_Data_ProfileInsightValueCollection.htm)
[Tessa.Exchange.WebServices.Data.RuleOperationErrorCollection](T_Tessa_Exchange_WebServices_Data_RuleOperationErrorCollection.htm)
[Tessa.Exchange.WebServices.Data.SkillInsightValueCollection](T_Tessa_Exchange_WebServices_Data_SkillInsightValueCollection.htm)
[Tessa.Exchange.WebServices.Data.TaskSuggestionCollection](T_Tessa_Exchange_WebServices_Data_TaskSuggestionCollection.htm)
[Tessa.Exchange.WebServices.Data.UrlEntityCollection](T_Tessa_Exchange_WebServices_Data_UrlEntityCollection.htm)
Подробнее __Less __
Implements
    [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)<TComplexProperty>, [IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)
#### Параметры типа
TComplexProperty
    ComplexProperty type.
##  __Свойства
[Count](P_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1_Count.htm)|
Gets the total number of properties in the collection.  
---|---  
[Item](P_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1_Item.htm)|
Gets the property at the specified index.  
## __Методы
[Contains](M_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1_Contains.htm)|
Determines whether a specific property is in the collection.  
---|---  
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
[GetEnumerator](M_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1_GetEnumerator.htm)|
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
[IndexOf](M_Tessa_Exchange_WebServices_Data_ComplexPropertyCollection_1_IndexOf.htm)|
Searches for a specific property and return its zero-based index within the
collection.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[AsArray<TComplexProperty>](M_Tessa_Platform_Collections_EnumerableExtensions_AsArray__1.htm)|
Преобразует коллекцию в массив. В случае, если коллекция не является массивом,
к ней применяется
[ToArray<TSource>(IEnumerable<TSource>)](https://learn.microsoft.com/dotnet/api/system.linq.enumerable.toarray#system-
linq-enumerable-toarray-1\(system-collections-generic-
ienumerable\(\(-0\)\)\)).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
---|---  
[ConvertToListDictionaries<TComplexProperty>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления по умолчанию  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ConvertToListDictionaries<TComplexProperty>](M_Tessa_Views_Mapping_DictionaryConverter_ConvertToListDictionaries__1_1.htm)|
Осуществляет сопоставлению коллекции source на коллекцию коллекций ключ-
значение в соответствии с контекстом сопоставления context  
(Определяется
[DictionaryConverter](T_Tessa_Views_Mapping_DictionaryConverter.htm))  
[ForEach<TComplexProperty>](M_Tessa_Platform_Collections_EnumerableExtensions_ForEach__1.htm)|
Выполняет указанное действие с каждым элементом коллекции
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1).  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[FullOuterJoin<TComplexProperty, TInner, TKey,
TResult>](M_Tessa_Platform_Collections_Extensions_FullOuterJoin__4.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[IndexOf<TComplexProperty>](M_Tessa_Platform_Collections_Extensions_IndexOf__1.htm)|
Возвращает индекс первого вхождения элемента в последовательность,
определяемый посредством заданного выражения.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[IndexOf<TComplexProperty>](M_Tessa_Platform_Collections_Extensions_IndexOf__1_1.htm)|
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
[OrderByDependencies<TComplexProperty>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<TComplexProperty>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__1_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<TComplexProperty,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByDependencies<TComplexProperty,
TKey>](M_Tessa_Platform_Collections_Extensions_OrderByDependencies__2_1.htm)|  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[OrderByLocalized<TComplexProperty>](M_Tessa_Platform_PlatformExtensions_OrderByLocalized__1.htm)|
Сортирует значения последовательности по возрастанию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[OrderByLocalizedDescending<TComplexProperty>](M_Tessa_Platform_PlatformExtensions_OrderByLocalizedDescending__1.htm)|
Сортирует значения последовательности по убыванию по локализованному ключу,
который определяется для каждого элемента.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[RunWithMaxDegreeOfParallelismAsync<TComplexProperty>](M_Tessa_Platform_PlatformExtensions_RunWithMaxDegreeOfParallelismAsync__1.htm)|
Выполняет асинхронную обработку элементов с ограничением на максимальное
количество параллельных задач.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[ToDictionaryAsync<TComplexProperty, TKey,
TElement>](M_Tessa_Platform_PlatformExtensions_ToDictionaryAsync__3.htm)|
Создает словарь [Dictionary<TKey,
TValue>](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)
из объекта
[IEnumerable<T>](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)
в соответствии с заданными функциями синхронного селектора ключа и
асинхронного селектора значения.  
(Определяется [PlatformExtensions](T_Tessa_Platform_PlatformExtensions.htm))  
[ToObservableCollection<TComplexProperty>](M_Tessa_Platform_Collections_Extensions_ToObservableCollection__1.htm)|
Преобразует коллекцию IEnumerable в ObservableCollection  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[ToSealableList<TComplexProperty>](M_Tessa_Platform_Collections_Extensions_ToSealableList__1.htm)|
Возвращает список объектов, поддерживающий защиту от изменений. Каждый из
объектов T в списке либо не реализует интерфейс
[ISealable](T_Tessa_Platform_ISealable.htm), либо защита от изменений таких
объектов не активируется вместе со списком.  
(Определяется [Extensions](T_Tessa_Platform_Collections_Extensions.htm))  
[TryFirst<TComplexProperty>](M_Tessa_Platform_Collections_EnumerableExtensions_TryFirst__1.htm)|
Возвращает первый элемент последовательности, удовлетворяющий условию.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
[TrySingleOrDefault<TComplexProperty>](M_Tessa_Platform_Collections_EnumerableExtensions_TrySingleOrDefault__1.htm)|
Возвращает единственный конкретный элемент коллекции или значение по умолчанию
для типа, если этот элемент не найден.  
(Определяется
[EnumerableExtensions](T_Tessa_Platform_Collections_EnumerableExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Exchange.WebServices.Data - пространство
имён](N_Tessa_Exchange_WebServices_Data.htm)
