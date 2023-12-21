# ISearchQueryMetadata - интерфейс
Интерфейс метаданных поискового запроса
## __Definition
 **Пространство имён:**
[Tessa.Views.SearchQueries](N_Tessa_Views_SearchQueries.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISearchQueryMetadata : INamedViewMetadataItem, 
    	IViewMetadataItem, INamedObject, ISealable, IValidationObject, IValidatable, 
    	ICloneable, IExtensionsMetadata, IParametersOwner, IParametersStateOwner
VB __Копировать
     Public Interface ISearchQueryMetadata
    	Inherits INamedViewMetadataItem, IViewMetadataItem, INamedObject, ISealable, 
    	IValidationObject, IValidatable, ICloneable, IExtensionsMetadata, IParametersOwner, 
    	IParametersStateOwner
C++ __Копировать
     public interface class ISearchQueryMetadata : INamedViewMetadataItem, 
    	IViewMetadataItem, INamedObject, ISealable, IValidationObject, IValidatable, 
    	ICloneable, IExtensionsMetadata, IParametersOwner, IParametersStateOwner
F# __Копировать
     type ISearchQueryMetadata = 
        interface
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
Implements
    [ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable), [INamedObject](T_Tessa_Platform_Collections_INamedObject.htm), [ISealable](T_Tessa_Platform_ISealable.htm), [IValidatable](T_Tessa_Platform_Validation_IValidatable.htm), [IValidationObject](T_Tessa_Platform_Validation_IValidationObject.htm), [INamedViewMetadataItem](T_Tessa_Views_Metadata_INamedViewMetadataItem.htm), [IViewMetadataItem](T_Tessa_Views_Metadata_IViewMetadataItem.htm), [IExtensionsMetadata](T_Tessa_Views_Workplaces_IExtensionsMetadata.htm), [IParametersOwner](T_Tessa_Views_Workplaces_IParametersOwner.htm), [IParametersStateOwner](T_Tessa_Views_Workplaces_IParametersStateOwner.htm)
##  __Свойства
[Alias](P_Tessa_Views_Metadata_INamedViewMetadataItem_Alias.htm)|  Псевдоним
элемента метаданных  
(Унаследован от
[INamedViewMetadataItem](T_Tessa_Views_Metadata_INamedViewMetadataItem.htm))  
---|---  
[CreatedByUserID](P_Tessa_Views_SearchQueries_ISearchQueryMetadata_CreatedByUserID.htm)|
Идентификатор пользователя создавший поисковый запрос  
[Extensions](P_Tessa_Views_Workplaces_IExtensionsMetadata_Extensions.htm)|
Gets возвращает список имен типов расширений  
(Унаследован от
[IExtensionsMetadata](T_Tessa_Views_Workplaces_IExtensionsMetadata.htm))  
[ID](P_Tessa_Views_SearchQueries_ISearchQueryMetadata_ID.htm)|  Идентификатор
поискового запроса  
[IsPublic](P_Tessa_Views_SearchQueries_ISearchQueryMetadata_IsPublic.htm)|
Признак общедоступного поискового запроса  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[Items](P_Tessa_Views_SearchQueries_ISearchQueryMetadata_Items.htm)|  Список
дочерних элементов  
[ModificationDateTime](P_Tessa_Views_SearchQueries_ISearchQueryMetadata_ModificationDateTime.htm)|
Дата и время последнего изменения  
[Parameters](P_Tessa_Views_Workplaces_IParametersOwner_Parameters.htm)|  Gets
or sets Список параметров  
(Унаследован от
[IParametersOwner](T_Tessa_Views_Workplaces_IParametersOwner.htm))  
[ParametersByState](P_Tessa_Views_Workplaces_IParametersStateOwner_ParametersByState.htm)|
Список значений заданных для определенных состояний родительского
представления в связке мастер-детейл при нахождении представления в режиме
столбца  
(Унаследован от
[IParametersStateOwner](T_Tessa_Views_Workplaces_IParametersStateOwner.htm))  
[TemplateCompositionID](P_Tessa_Views_SearchQueries_ISearchQueryMetadata_TemplateCompositionID.htm)|
Идентификатор шаблона для поисковых запросов содержащих структуру.  
[ValidationResult](P_Tessa_Views_SearchQueries_ISearchQueryMetadata_ValidationResult.htm)|
Результат формирования поискового запроса  
[ViewAlias](P_Tessa_Views_SearchQueries_ISearchQueryMetadata_ViewAlias.htm)|
Дата и время последнего изменения запроса  
## __Методы
[Clone](https://learn.microsoft.com/dotnet/api/system.icloneable.clone#system-
icloneable-clone)| Creates a new object that is a copy of the current
instance.  
(Унаследован от
[ICloneable](https://learn.microsoft.com/dotnet/api/system.icloneable))  
---|---  
[GetName](M_Tessa_Platform_Collections_INamedObject_GetName.htm)|  Возвращает
имя объекта  
(Унаследован от [INamedObject](T_Tessa_Platform_Collections_INamedObject.htm))  
[IsValid](M_Tessa_Platform_Validation_IValidatable_IsValid.htm)| Выполняет
проверку объекта на валидность и возвращает признак того, что объект является
валидным.  
(Унаследован от [IValidatable](T_Tessa_Platform_Validation_IValidatable.htm))  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[Validate](M_Tessa_Platform_Validation_IValidationObject_Validate.htm)|
Выполняет валидацию текущего объекта и всех его дочерних объектов.  
(Унаследован от
[IValidationObject](T_Tessa_Platform_Validation_IValidationObject.htm))  
##  __Методы расширения
[Validate](M_Tessa_Platform_Validation_ValidationExtensions_Validate.htm)|
Выполняет валидацию объекта и всех его дочерних объектов.  
(Определяется
[ValidationExtensions](T_Tessa_Platform_Validation_ValidationExtensions.htm))  
---|---  
##  __См. также
#### Ссылки
[Tessa.Views.SearchQueries - пространство
имён](N_Tessa_Views_SearchQueries.htm)
