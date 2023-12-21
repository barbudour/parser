# SearchQueryClientInitializationExtension - конструктор
Инициализирует новый экземпляр класса
[SearchQueryClientInitializationExtension](T_Tessa_Extensions_Platform_Client_Initialization_SearchQueryClientInitializationExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Initialization](N_Tessa_Extensions_Platform_Client_Initialization.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public SearchQueryClientInitializationExtension(
    	[OptionalDependencyAttribute] ISearchQueryService searchQueryService,
    	IConverter<IJsonSearchQueryMetadata, ISearchQueryMetadata> jsonSearchQueryMetadataConverter
    )
VB __Копировать
     Public Sub New ( 
    	<OptionalDependencyAttribute> searchQueryService As ISearchQueryService,
    	jsonSearchQueryMetadataConverter As IConverter(Of IJsonSearchQueryMetadata, ISearchQueryMetadata)
    )
C++ __Копировать
     public:
    SearchQueryClientInitializationExtension(
    	[OptionalDependencyAttribute] ISearchQueryService^ searchQueryService, 
    	IConverter<IJsonSearchQueryMetadata^, ISearchQueryMetadata^>^ jsonSearchQueryMetadataConverter
    )
F# __Копировать
     new : 
            [<OptionalDependencyAttribute>] searchQueryService : ISearchQueryService * 
            jsonSearchQueryMetadataConverter : IConverter<IJsonSearchQueryMetadata, ISearchQueryMetadata> -> SearchQueryClientInitializationExtension
#### Параметры
searchQueryService
[ISearchQueryService](T_Tessa_Views_SearchQueries_ISearchQueryService.htm)
jsonSearchQueryMetadataConverter
[IConverter](T_Tessa_Views_Workplaces_Json_Converters_IConverter_2.htm)<[IJsonSearchQueryMetadata](T_Tessa_Views_Workplaces_Json_Metadata_IJsonSearchQueryMetadata.htm),
[ISearchQueryMetadata](T_Tessa_Views_SearchQueries_ISearchQueryMetadata.htm)>
## __См. также
#### Ссылки
[SearchQueryClientInitializationExtension -
](T_Tessa_Extensions_Platform_Client_Initialization_SearchQueryClientInitializationExtension.htm)
[Tessa.Extensions.Platform.Client.Initialization - пространство
имён](N_Tessa_Extensions_Platform_Client_Initialization.htm)
