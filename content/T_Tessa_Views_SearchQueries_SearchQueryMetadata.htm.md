# SearchQueryMetadata - класс
Метаданные поискового запроса.
## __Definition
 **Пространство имён:**
[Tessa.Views.SearchQueries](N_Tessa_Views_SearchQueries.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    [KnownTypeAttribute(typeof(ValidationResult))]
    [KnownTypeAttribute(typeof(ValidationResultItem))]
    [KnownTypeAttribute(typeof(SearchQueryCollection))]
    public class SearchQueryMetadata : NamedViewMetadataItem, 
    	ISearchQueryMetadata, INamedViewMetadataItem, IViewMetadataItem, INamedObject, ISealable, 
    	IValidationObject, IValidatable, ICloneable, IExtensionsMetadata, IParametersOwner, 
    	IParametersStateOwner
VB __Копировать
    <SerializableAttribute>
    <DataContractAttribute>
    <KnownTypeAttribute(GetType(ValidationResult))>
    <KnownTypeAttribute(GetType(ValidationResultItem))>
    <KnownTypeAttribute(GetType(SearchQueryCollection))>
    Public Class SearchQueryMetadata
    	Inherits NamedViewMetadataItem
    	Implements ISearchQueryMetadata, INamedViewMetadataItem, IViewMetadataItem, INamedObject, 
    	ISealable, IValidationObject, IValidatable, ICloneable, IExtensionsMetadata, 
    	IParametersOwner, IParametersStateOwner
C++ __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    [KnownTypeAttribute(typeof(ValidationResult))]
    [KnownTypeAttribute(typeof(ValidationResultItem))]
    [KnownTypeAttribute(typeof(SearchQueryCollection))]
    public ref class SearchQueryMetadata : public NamedViewMetadataItem, 
    	ISearchQueryMetadata, INamedViewMetadataItem, IViewMetadataItem, INamedObject, ISealable, 
    	IValidationObject, IValidatable, ICloneable, IExtensionsMetadata, IParametersOwner, 
    	IParametersStateOwner
F# __Копировать
     [<SerializableAttribute>]
    [<DataContractAttribute>]
    [<KnownTypeAttribute(typeof(ValidationResult))>]
    [<KnownTypeAttribute(typeof(ValidationResultItem))>]
    [<KnownTypeAttribute(typeof(SearchQueryCollection))>]
    type SearchQueryMetadata = 
        class
            inherit NamedViewMetadataItem
            interface ISearchQueryMetadata
            interface INamedViewMetadataItem
            interface IViewMetadataItem
            interface INamedObject
            interface ISealable
            interface IValidationObject
            interface IValidatable
            interface ICloneable
            interface IExtensionsMetadata
            interface IParametersOwner
            interface IParametersStateOwner
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm) __[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm) __[NamedViewMetadataItem](T_Tessa_Views_Metadata_NamedViewMetadataItem.htm) __ SearchQueryMetadata
Derived
[Tessa.Views.NullSearchQueryMetadata](T_Tessa_Views_NullSearchQueryMetadata.htm)
Implements
    [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [INamedObject](T_Tessa_Platform_Collections_INamedObject.htm), [ISealable](T_Tessa_Platform_ISealable.htm), [IValidatable](T_Tessa_Platform_Validation_IValidatable.htm), [IValidationObject](T_Tessa_Platform_Validation_IValidationObject.htm), [INamedViewMetadataItem](T_Tessa_Views_Metadata_INamedViewMetadataItem.htm), [IViewMetadataItem](T_Tessa_Views_Metadata_IViewMetadataItem.htm), [ISearchQueryMetadata](T_Tessa_Views_SearchQueries_ISearchQueryMetadata.htm), [IExtensionsMetadata](T_Tessa_Views_Workplaces_IExtensionsMetadata.htm), [IParametersOwner](T_Tessa_Views_Workplaces_IParametersOwner.htm), [IParametersStateOwner](T_Tessa_Views_Workplaces_IParametersStateOwner.htm)
##  __Конструкторы
[SearchQueryMetadata](M_Tessa_Views_SearchQueries_SearchQueryMetadata__ctor.htm)|
Initializes a new instance of the SearchQueryMetadata class. Инициализирует
новый экземпляр класса
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
---|---  
## __Свойства
[Alias](P_Tessa_Views_Metadata_NamedViewMetadataItem_Alias.htm)|  Gets or sets
Псевдоним элемента метаданных  
(Унаследован от
[NamedViewMetadataItem](T_Tessa_Views_Metadata_NamedViewMetadataItem.htm))  
---|---  
[CreatedByUserID](P_Tessa_Views_SearchQueries_SearchQueryMetadata_CreatedByUserID.htm)|
Идентификатор пользователя, создавшего поисковый запрос.  
[Extensions](P_Tessa_Views_SearchQueries_SearchQueryMetadata_Extensions.htm)|
Список имен типов расширений.  
[ID](P_Tessa_Views_SearchQueries_SearchQueryMetadata_ID.htm)|  Идентификатор
поискового запроса.  
[IsPublic](P_Tessa_Views_SearchQueries_SearchQueryMetadata_IsPublic.htm)|
Признак общедоступного поискового запроса.  
[IsSealed](P_Tessa_Views_Metadata_ViewMetadataItem_IsSealed.htm)| Признак
того, что объект был защищён от изменений.  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[Items](P_Tessa_Views_SearchQueries_SearchQueryMetadata_Items.htm)|  Список
дочерних элементов  
[ModificationDateTime](P_Tessa_Views_SearchQueries_SearchQueryMetadata_ModificationDateTime.htm)|
Дата и время последнего изменения.  
[Parameters](P_Tessa_Views_SearchQueries_SearchQueryMetadata_Parameters.htm)|
Список параметров запроса.  
[ParametersByState](P_Tessa_Views_SearchQueries_SearchQueryMetadata_ParametersByState.htm)|
Список значений, заданных для определенных состояний родительского
представления в связке мастер-детейл при нахождении представления в режиме
столбца.  
[TemplateCompositionID](P_Tessa_Views_SearchQueries_SearchQueryMetadata_TemplateCompositionID.htm)|
Идентификатор шаблона для поисковых запросов содержащих структуру.  
[ValidationResult](P_Tessa_Views_SearchQueries_SearchQueryMetadata_ValidationResult.htm)|
Результат формирования поискового запроса.  
[ViewAlias](P_Tessa_Views_SearchQueries_SearchQueryMetadata_ViewAlias.htm)|
Алиас представления.  
## __Методы
[CheckSealed](M_Tessa_Views_Metadata_ViewMetadataItem_CheckSealed.htm)|
Проверка защиты метаданных от изменения  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
---|---  
[Clone](M_Tessa_Views_SearchQueries_SearchQueryMetadata_Clone.htm)|  Создает
новый объект, который является копией текущего экземпляра.  
(Переопределяет
[ViewMetadataItem.Clone()](M_Tessa_Views_Metadata_ViewMetadataItem_Clone.htm))  
[Deserialize](M_Tessa_Views_SearchQueries_SearchQueryMetadata_Deserialize.htm)|
The deserialize.  
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
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetName](M_Tessa_Views_Metadata_NamedViewMetadataItem_GetName.htm)|
Возвращает имя объекта  
(Унаследован от
[NamedViewMetadataItem](T_Tessa_Views_Metadata_NamedViewMetadataItem.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetValidationName](M_Tessa_Views_SearchQueries_SearchQueryMetadata_GetValidationName.htm)|
Возвращает строку, определяющую имя объекта, или null, если имя объекта ещё
неизвестно или объект не содержит имени.  
(Переопределяет
[NamedViewMetadataItem.GetValidationName()](M_Tessa_Views_Metadata_NamedViewMetadataItem_GetValidationName.htm))  
[InternalSeal](M_Tessa_Views_SearchQueries_SearchQueryMetadata_InternalSeal.htm)|
Осуществляет внутренние действия при защите класса от изменений. Перекрывается
в потомках для определения дополнительных действий при защите класса от
изменений.  
(Переопределяет
[ViewMetadataItem.InternalSeal()](M_Tessa_Views_Metadata_ViewMetadataItem_InternalSeal.htm))  
[IsValid](M_Tessa_Platform_Validation_ValidationObject_IsValid.htm)| Выполняет
проверку объекта на валидность и возвращает признак того, что объект является
валидным.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnDeserialized](M_Tessa_Views_Metadata_ViewMetadataItem_OnDeserialized.htm)|
Вызывается после процесса десериализации элемента метаданных Может
перекрываться в потомках  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[OnDeserializedMethod](M_Tessa_Views_Metadata_ViewMetadataItem_OnDeserializedMethod.htm)|
Вызывается после десериализации элемента метаданных  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[OnDeserializing](M_Tessa_Views_Metadata_ViewMetadataItem_OnDeserializing.htm)|
Вызывается перед десериализацией элемента метаданных Может перекрываться в
потомках  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[OnDeserializingMethod](M_Tessa_Views_Metadata_ViewMetadataItem_OnDeserializingMethod.htm)|
Вызывается перед десериализацией элемента метаданных  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[OnSerialized](M_Tessa_Views_Metadata_ViewMetadataItem_OnSerialized.htm)|
Вызывается после окончания процесса сериализации элемента метаданных. Может
перекрываться в потомках  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[OnSerializedMethod](M_Tessa_Views_Metadata_ViewMetadataItem_OnSerializedMethod.htm)|
Вызывается после окончания процесса сериализации элемента метаданных.  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[OnSerializing](M_Tessa_Views_Metadata_ViewMetadataItem_OnSerializing.htm)|
Вызывается перед началом процесса сериализации элемента метаданных. Может
перекрываться в потомках  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[OnSerializingMethod](M_Tessa_Views_Metadata_ViewMetadataItem_OnSerializingMethod.htm)|
Вызывается перед началом процесса сериализации элемента метаданных.  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[Seal](M_Tessa_Views_Metadata_ViewMetadataItem_Seal.htm)| Защищает объект от
изменений.  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[Serializing](M_Tessa_Views_SearchQueries_SearchQueryMetadata_Serializing.htm)|
The serializing.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Validate()](M_Tessa_Platform_Validation_ValidationObject_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[Validate(IValidationResultBuilder)](M_Tessa_Platform_Validation_ValidationObject_Validate_1.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm))  
[ValidateInternal](M_Tessa_Views_SearchQueries_SearchQueryMetadata_ValidateInternal.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Переопределяет
[NamedViewMetadataItem.ValidateInternal(IValidationResultBuilder)](M_Tessa_Views_Metadata_NamedViewMetadataItem_ValidateInternal.htm))  
##  __Поля
[isDeserializing](F_Tessa_Views_Metadata_ViewMetadataItem_isDeserializing.htm)|
Признак десериализации объекта  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
---|---  
[isSerializing](F_Tessa_Views_Metadata_ViewMetadataItem_isSerializing.htm)|
Признак сериализации объекта  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Validate](M_Tessa_Platform_Validation_ValidationExtensions_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Views.SearchQueries - пространство
имён](N_Tessa_Views_SearchQueries.htm)
