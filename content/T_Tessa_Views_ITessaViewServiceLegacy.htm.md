# ITessaViewServiceLegacy - интерфейс
##  __Definition
 **Пространство имён:** [Tessa.Views](N_Tessa_Views.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [ServiceContractAttribute(Name = "ITessaViewService")]
    [SessionServiceAttribute("tessa/TessaViewService.svc", TransferMode.Buffered)]
    [ServiceKnownTypeAttribute(typeof(ViewMetadata))]
    [ServiceKnownTypeAttribute(typeof(ViewColumnMetadata))]
    [ServiceKnownTypeAttribute(typeof(ViewColumnCollection))]
    [ServiceKnownTypeAttribute(typeof(ViewAppearanceMetadata))]
    [ServiceKnownTypeAttribute(typeof(ViewParameterMetadata))]
    [ServiceKnownTypeAttribute(typeof(ViewReferenceMetadata))]
    [ServiceKnownTypeAttribute(typeof(ViewReferenceCollection))]
    [ServiceKnownTypeAttribute(typeof(ViewAppearanceCollection))]
    [ServiceKnownTypeAttribute(typeof(ViewParametersCollection))]
    [ServiceKnownTypeAttribute(typeof(ValidationResult))]
    [ServiceKnownTypeAttribute(typeof(ValidationResultItem))]
    [ServiceKnownTypeAttribute(typeof(ViewSubsetMetadata))]
    [ServiceKnownTypeAttribute(typeof(ViewSubsetCollection))]
    [ServiceKnownTypeAttribute(typeof(TessaViewRequest))]
    [ServiceKnownTypeAttribute(typeof(GetModelRequest))]
    [ServiceKnownTypeAttribute(typeof(ImportTessaViewRequest))]
    [ServiceKnownTypeAttribute(typeof(StoreTessaViewRequest))]
    [ServiceKnownTypeAttribute(typeof(TessaViewResult))]
    [ServiceKnownTypeAttribute(typeof(SortingColumnCollection))]
    [ServiceKnownTypeAttribute(typeof(ExtensionMetadata))]
    [ServiceKnownTypeAttribute(typeof(ViewExtensionCollection))]
    [ServiceKnownTypeAttribute(typeof(SortingColumn))]
    [ServiceKnownTypeAttribute(typeof(SearchQueryMetadata))]
    [ServiceKnownTypeAttribute(typeof(AutoCompleteInfo))]
    [ServiceKnownTypeAttribute(typeof(DropDownInfo))]
    [ServiceKnownTypeAttribute(typeof(DateTimeOffset))]
    [ServiceKnownTypeAttribute(typeof(ViewMetadataItem))]
    [ServiceKnownTypeAttribute(typeof(NamedViewMetadataItem))]
    [ServiceKnownTypeAttribute(typeof(AppearanceFontStyle))]
    public interface ITessaViewServiceLegacy
VB __Копировать
    <ServiceContractAttribute(Name := "ITessaViewService")>
    <SessionServiceAttribute("tessa/TessaViewService.svc", TransferMode.Buffered)>
    <ServiceKnownTypeAttribute(GetType(ViewMetadata))>
    <ServiceKnownTypeAttribute(GetType(ViewColumnMetadata))>
    <ServiceKnownTypeAttribute(GetType(ViewColumnCollection))>
    <ServiceKnownTypeAttribute(GetType(ViewAppearanceMetadata))>
    <ServiceKnownTypeAttribute(GetType(ViewParameterMetadata))>
    <ServiceKnownTypeAttribute(GetType(ViewReferenceMetadata))>
    <ServiceKnownTypeAttribute(GetType(ViewReferenceCollection))>
    <ServiceKnownTypeAttribute(GetType(ViewAppearanceCollection))>
    <ServiceKnownTypeAttribute(GetType(ViewParametersCollection))>
    <ServiceKnownTypeAttribute(GetType(ValidationResult))>
    <ServiceKnownTypeAttribute(GetType(ValidationResultItem))>
    <ServiceKnownTypeAttribute(GetType(ViewSubsetMetadata))>
    <ServiceKnownTypeAttribute(GetType(ViewSubsetCollection))>
    <ServiceKnownTypeAttribute(GetType(TessaViewRequest))>
    <ServiceKnownTypeAttribute(GetType(GetModelRequest))>
    <ServiceKnownTypeAttribute(GetType(ImportTessaViewRequest))>
    <ServiceKnownTypeAttribute(GetType(StoreTessaViewRequest))>
    <ServiceKnownTypeAttribute(GetType(TessaViewResult))>
    <ServiceKnownTypeAttribute(GetType(SortingColumnCollection))>
    <ServiceKnownTypeAttribute(GetType(ExtensionMetadata))>
    <ServiceKnownTypeAttribute(GetType(ViewExtensionCollection))>
    <ServiceKnownTypeAttribute(GetType(SortingColumn))>
    <ServiceKnownTypeAttribute(GetType(SearchQueryMetadata))>
    <ServiceKnownTypeAttribute(GetType(AutoCompleteInfo))>
    <ServiceKnownTypeAttribute(GetType(DropDownInfo))>
    <ServiceKnownTypeAttribute(GetType(DateTimeOffset))>
    <ServiceKnownTypeAttribute(GetType(ViewMetadataItem))>
    <ServiceKnownTypeAttribute(GetType(NamedViewMetadataItem))>
    <ServiceKnownTypeAttribute(GetType(AppearanceFontStyle))>
    Public Interface ITessaViewServiceLegacy
C++ __Копировать
    [ServiceContractAttribute(Name = L"ITessaViewService")]
    [SessionServiceAttribute(L"tessa/TessaViewService.svc", TransferMode::Buffered)]
    [ServiceKnownTypeAttribute(typeof(ViewMetadata))]
    [ServiceKnownTypeAttribute(typeof(ViewColumnMetadata))]
    [ServiceKnownTypeAttribute(typeof(ViewColumnCollection))]
    [ServiceKnownTypeAttribute(typeof(ViewAppearanceMetadata))]
    [ServiceKnownTypeAttribute(typeof(ViewParameterMetadata))]
    [ServiceKnownTypeAttribute(typeof(ViewReferenceMetadata))]
    [ServiceKnownTypeAttribute(typeof(ViewReferenceCollection))]
    [ServiceKnownTypeAttribute(typeof(ViewAppearanceCollection))]
    [ServiceKnownTypeAttribute(typeof(ViewParametersCollection))]
    [ServiceKnownTypeAttribute(typeof(ValidationResult))]
    [ServiceKnownTypeAttribute(typeof(ValidationResultItem))]
    [ServiceKnownTypeAttribute(typeof(ViewSubsetMetadata))]
    [ServiceKnownTypeAttribute(typeof(ViewSubsetCollection))]
    [ServiceKnownTypeAttribute(typeof(TessaViewRequest))]
    [ServiceKnownTypeAttribute(typeof(GetModelRequest))]
    [ServiceKnownTypeAttribute(typeof(ImportTessaViewRequest))]
    [ServiceKnownTypeAttribute(typeof(StoreTessaViewRequest))]
    [ServiceKnownTypeAttribute(typeof(TessaViewResult))]
    [ServiceKnownTypeAttribute(typeof(SortingColumnCollection))]
    [ServiceKnownTypeAttribute(typeof(ExtensionMetadata))]
    [ServiceKnownTypeAttribute(typeof(ViewExtensionCollection))]
    [ServiceKnownTypeAttribute(typeof(SortingColumn))]
    [ServiceKnownTypeAttribute(typeof(SearchQueryMetadata))]
    [ServiceKnownTypeAttribute(typeof(AutoCompleteInfo))]
    [ServiceKnownTypeAttribute(typeof(DropDownInfo))]
    [ServiceKnownTypeAttribute(typeof(DateTimeOffset))]
    [ServiceKnownTypeAttribute(typeof(ViewMetadataItem))]
    [ServiceKnownTypeAttribute(typeof(NamedViewMetadataItem))]
    [ServiceKnownTypeAttribute(typeof(AppearanceFontStyle))]
    public interface class ITessaViewServiceLegacy
F# __Копировать
     [<ServiceContractAttribute(Name = "ITessaViewService")>]
    [<SessionServiceAttribute("tessa/TessaViewService.svc", TransferMode.Buffered)>]
    [<ServiceKnownTypeAttribute(typeof(ViewMetadata))>]
    [<ServiceKnownTypeAttribute(typeof(ViewColumnMetadata))>]
    [<ServiceKnownTypeAttribute(typeof(ViewColumnCollection))>]
    [<ServiceKnownTypeAttribute(typeof(ViewAppearanceMetadata))>]
    [<ServiceKnownTypeAttribute(typeof(ViewParameterMetadata))>]
    [<ServiceKnownTypeAttribute(typeof(ViewReferenceMetadata))>]
    [<ServiceKnownTypeAttribute(typeof(ViewReferenceCollection))>]
    [<ServiceKnownTypeAttribute(typeof(ViewAppearanceCollection))>]
    [<ServiceKnownTypeAttribute(typeof(ViewParametersCollection))>]
    [<ServiceKnownTypeAttribute(typeof(ValidationResult))>]
    [<ServiceKnownTypeAttribute(typeof(ValidationResultItem))>]
    [<ServiceKnownTypeAttribute(typeof(ViewSubsetMetadata))>]
    [<ServiceKnownTypeAttribute(typeof(ViewSubsetCollection))>]
    [<ServiceKnownTypeAttribute(typeof(TessaViewRequest))>]
    [<ServiceKnownTypeAttribute(typeof(GetModelRequest))>]
    [<ServiceKnownTypeAttribute(typeof(ImportTessaViewRequest))>]
    [<ServiceKnownTypeAttribute(typeof(StoreTessaViewRequest))>]
    [<ServiceKnownTypeAttribute(typeof(TessaViewResult))>]
    [<ServiceKnownTypeAttribute(typeof(SortingColumnCollection))>]
    [<ServiceKnownTypeAttribute(typeof(ExtensionMetadata))>]
    [<ServiceKnownTypeAttribute(typeof(ViewExtensionCollection))>]
    [<ServiceKnownTypeAttribute(typeof(SortingColumn))>]
    [<ServiceKnownTypeAttribute(typeof(SearchQueryMetadata))>]
    [<ServiceKnownTypeAttribute(typeof(AutoCompleteInfo))>]
    [<ServiceKnownTypeAttribute(typeof(DropDownInfo))>]
    [<ServiceKnownTypeAttribute(typeof(DateTimeOffset))>]
    [<ServiceKnownTypeAttribute(typeof(ViewMetadataItem))>]
    [<ServiceKnownTypeAttribute(typeof(NamedViewMetadataItem))>]
    [<ServiceKnownTypeAttribute(typeof(AppearanceFontStyle))>]
    type ITessaViewServiceLegacy = interface end
##  __Методы
[GetData](M_Tessa_Views_ITessaViewServiceLegacy_GetData.htm)|  Осуществляет
запрос данных представления  
---|---  
## __См. также
#### Ссылки
[Tessa.Views - пространство имён](N_Tessa_Views.htm)
