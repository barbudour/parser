# NullSearchQueryMetadata - класс
Фейковый класс для отображения пустых метаданных поискового запроса
## __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class NullSearchQueryMetadata : SearchQueryMetadata
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class NullSearchQueryMetadata
    	Inherits SearchQueryMetadata
C++ __Копировать
    [SerializableAttribute]
    public ref class NullSearchQueryMetadata sealed : public SearchQueryMetadata
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type NullSearchQueryMetadata = 
        class
            inherit SearchQueryMetadata
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValidationObject](T_Tessa_Platform_Validation_ValidationObject.htm) __[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm) __[NamedViewMetadataItem](T_Tessa_Views_Metadata_NamedViewMetadataItem.htm) __[SearchQueryMetadata](T_Tessa_Views_SearchQueries_SearchQueryMetadata.htm) __ NullSearchQueryMetadata
##  __Свойства
[Alias](P_Tessa_Views_Metadata_NamedViewMetadataItem_Alias.htm)|  Gets or sets
Псевдоним элемента метаданных  
(Унаследован от
[NamedViewMetadataItem](T_Tessa_Views_Metadata_NamedViewMetadataItem.htm))  
---|---  
[CreatedByUserID](P_Tessa_Views_SearchQueries_SearchQueryMetadata_CreatedByUserID.htm)|
Идентификатор пользователя, создавшего поисковый запрос.  
(Унаследован от
[SearchQueryMetadata](T_Tessa_Views_SearchQueries_SearchQueryMetadata.htm))  
[Extensions](P_Tessa_Views_SearchQueries_SearchQueryMetadata_Extensions.htm)|
Список имен типов расширений.  
(Унаследован от
[SearchQueryMetadata](T_Tessa_Views_SearchQueries_SearchQueryMetadata.htm))  
[ID](P_Tessa_Views_SearchQueries_SearchQueryMetadata_ID.htm)|  Идентификатор
поискового запроса.  
(Унаследован от
[SearchQueryMetadata](T_Tessa_Views_SearchQueries_SearchQueryMetadata.htm))  
[Instance](P_Tessa_Views_NullSearchQueryMetadata_Instance.htm)|  Gets
Возвращает экземпляр объекта  
[IsPublic](P_Tessa_Views_SearchQueries_SearchQueryMetadata_IsPublic.htm)|
Признак общедоступного поискового запроса.  
(Унаследован от
[SearchQueryMetadata](T_Tessa_Views_SearchQueries_SearchQueryMetadata.htm))  
[IsSealed](P_Tessa_Views_Metadata_ViewMetadataItem_IsSealed.htm)| Признак
того, что объект был защищён от изменений.  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
[Items](P_Tessa_Views_SearchQueries_SearchQueryMetadata_Items.htm)|  Список
дочерних элементов  
(Унаследован от
[SearchQueryMetadata](T_Tessa_Views_SearchQueries_SearchQueryMetadata.htm))  
[ModificationDateTime](P_Tessa_Views_SearchQueries_SearchQueryMetadata_ModificationDateTime.htm)|
Дата и время последнего изменения.  
(Унаследован от
[SearchQueryMetadata](T_Tessa_Views_SearchQueries_SearchQueryMetadata.htm))  
[Parameters](P_Tessa_Views_SearchQueries_SearchQueryMetadata_Parameters.htm)|
Список параметров запроса.  
(Унаследован от
[SearchQueryMetadata](T_Tessa_Views_SearchQueries_SearchQueryMetadata.htm))  
[ParametersByState](P_Tessa_Views_SearchQueries_SearchQueryMetadata_ParametersByState.htm)|
Список значений, заданных для определенных состояний родительского
представления в связке мастер-детейл при нахождении представления в режиме
столбца.  
(Унаследован от
[SearchQueryMetadata](T_Tessa_Views_SearchQueries_SearchQueryMetadata.htm))  
[TemplateCompositionID](P_Tessa_Views_SearchQueries_SearchQueryMetadata_TemplateCompositionID.htm)|
Идентификатор шаблона для поисковых запросов содержащих структуру.  
(Унаследован от
[SearchQueryMetadata](T_Tessa_Views_SearchQueries_SearchQueryMetadata.htm))  
[ValidationResult](P_Tessa_Views_SearchQueries_SearchQueryMetadata_ValidationResult.htm)|
Результат формирования поискового запроса.  
(Унаследован от
[SearchQueryMetadata](T_Tessa_Views_SearchQueries_SearchQueryMetadata.htm))  
[ViewAlias](P_Tessa_Views_SearchQueries_SearchQueryMetadata_ViewAlias.htm)|
Алиас представления.  
(Унаследован от
[SearchQueryMetadata](T_Tessa_Views_SearchQueries_SearchQueryMetadata.htm))  
##  __Методы
[CheckSealed](M_Tessa_Views_Metadata_ViewMetadataItem_CheckSealed.htm)|
Проверка защиты метаданных от изменения  
(Унаследован от
[ViewMetadataItem](T_Tessa_Views_Metadata_ViewMetadataItem.htm))  
---|---  
[Clone](M_Tessa_Views_SearchQueries_SearchQueryMetadata_Clone.htm)|  Создает
новый объект, который является копией текущего экземпляра.  
(Унаследован от
[SearchQueryMetadata](T_Tessa_Views_SearchQueries_SearchQueryMetadata.htm))  
[Deserialize](M_Tessa_Views_SearchQueries_SearchQueryMetadata_Deserialize.htm)|
The deserialize.  
(Унаследован от
[SearchQueryMetadata](T_Tessa_Views_SearchQueries_SearchQueryMetadata.htm))  
[Equals](M_Tessa_Views_NullSearchQueryMetadata_Equals.htm)|  Определяет, равен
ли заданный объект
[Object](https://learn.microsoft.com/dotnet/api/system.object) текущему
объекту [Object](https://learn.microsoft.com/dotnet/api/system.object) .  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Views_NullSearchQueryMetadata_GetHashCode.htm)|  Играет
роль хэш-функции для определенного типа.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
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
(Унаследован от
[SearchQueryMetadata](T_Tessa_Views_SearchQueries_SearchQueryMetadata.htm))  
[InternalSeal](M_Tessa_Views_SearchQueries_SearchQueryMetadata_InternalSeal.htm)|
Осуществляет внутренние действия при защите класса от изменений. Перекрывается
в потомках для определения дополнительных действий при защите класса от
изменений.  
(Унаследован от
[SearchQueryMetadata](T_Tessa_Views_SearchQueries_SearchQueryMetadata.htm))  
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
(Унаследован от
[SearchQueryMetadata](T_Tessa_Views_SearchQueries_SearchQueryMetadata.htm))  
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
(Унаследован от
[SearchQueryMetadata](T_Tessa_Views_SearchQueries_SearchQueryMetadata.htm))  
##  __Операторы
[Equality(NullSearchQueryMetadata,
NullSearchQueryMetadata)](M_Tessa_Views_NullSearchQueryMetadata_op_Equality.htm)|
Оператор равенства  
---|---  
[Inequality(NullSearchQueryMetadata,
NullSearchQueryMetadata)](M_Tessa_Views_NullSearchQueryMetadata_op_Inequality.htm)|
Оператор неравенства  
## __Поля
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
##  __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
