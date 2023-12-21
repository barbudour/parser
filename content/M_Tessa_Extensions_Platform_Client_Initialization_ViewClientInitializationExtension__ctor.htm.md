# ViewClientInitializationExtension - конструктор
Инициализирует новый экземпляр класса
[ViewClientInitializationExtension](T_Tessa_Extensions_Platform_Client_Initialization_ViewClientInitializationExtension.htm)
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Initialization](N_Tessa_Extensions_Platform_Client_Initialization.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public ViewClientInitializationExtension(
    	[OptionalDependencyAttribute] IViewServiceInitializer viewServiceInitializer,
    	IViewMetadataConverter<IJsonViewMetadata, IViewMetadata> jsonViewMetadataConverter,
    	ViewMetadataEvaluationContextFactory evaluationContextFactory
    )
VB __Копировать
     Public Sub New ( 
    	<OptionalDependencyAttribute> viewServiceInitializer As IViewServiceInitializer,
    	jsonViewMetadataConverter As IViewMetadataConverter(Of IJsonViewMetadata, IViewMetadata),
    	evaluationContextFactory As ViewMetadataEvaluationContextFactory
    )
C++ __Копировать
     public:
    ViewClientInitializationExtension(
    	[OptionalDependencyAttribute] IViewServiceInitializer^ viewServiceInitializer, 
    	IViewMetadataConverter<IJsonViewMetadata^, IViewMetadata^>^ jsonViewMetadataConverter, 
    	ViewMetadataEvaluationContextFactory^ evaluationContextFactory
    )
F# __Копировать
     new : 
            [<OptionalDependencyAttribute>] viewServiceInitializer : IViewServiceInitializer * 
            jsonViewMetadataConverter : IViewMetadataConverter<IJsonViewMetadata, IViewMetadata> * 
            evaluationContextFactory : ViewMetadataEvaluationContextFactory -> ViewClientInitializationExtension
#### Параметры
viewServiceInitializer
[IViewServiceInitializer](T_Tessa_Views_IViewServiceInitializer.htm)
jsonViewMetadataConverter
[IViewMetadataConverter](T_Tessa_Views_Json_Converters_IViewMetadataConverter_2.htm)<[IJsonViewMetadata](T_Tessa_Views_Json_IJsonViewMetadata.htm),
[IViewMetadata](T_Tessa_Views_Metadata_IViewMetadata.htm)>
evaluationContextFactory
[ViewMetadataEvaluationContextFactory](T_Tessa_Views_Parser_SyntaxTree_ViewMetadata_ViewMetadataEvaluationContextFactory.htm)
## __См. также
#### Ссылки
[ViewClientInitializationExtension -
](T_Tessa_Extensions_Platform_Client_Initialization_ViewClientInitializationExtension.htm)
[Tessa.Extensions.Platform.Client.Initialization - пространство
имён](N_Tessa_Extensions_Platform_Client_Initialization.htm)
