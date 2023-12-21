# PdfScanDocumentGenerator - конструктор
Создаёт экземпляр класса с указанием дополнительных параметров, связанных с
генерацией документов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public PdfScanDocumentGenerator(
    	IUnityContainer unityContainer,
    	bool addStamp,
    	Dictionary<string, Object> info = null
    )
VB __Копировать
     Public Sub New ( 
    	unityContainer As IUnityContainer,
    	addStamp As Boolean,
    	Optional info As Dictionary(Of String, Object) = Nothing
    )
C++ __Копировать
     public:
    PdfScanDocumentGenerator(
    	IUnityContainer^ unityContainer, 
    	bool addStamp, 
    	Dictionary<String^, Object^>^ info = nullptr
    )
F# __Копировать
     new : 
            unityContainer : IUnityContainer * 
            addStamp : bool * 
            ?info : Dictionary<string, Object> 
    (* Defaults:
            let _info = defaultArg info null
    *)
    -> PdfScanDocumentGenerator
#### Параметры
unityContainer IUnityContainer
     Контейнер Unity, содержащий зависимости для обработки PDF. Не должен быть равен null. 
addStamp [Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)
    Признак того, что при генерации документа должен быть добавлен штамп.
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
     Дополнительные параметры, связанные с генерацией документов, могут использоваться в расширениях. Если параметр равен null, то дополнительные параметры не передаются. 
## __См. также
#### Ссылки
[PdfScanDocumentGenerator -
](T_Tessa_Extensions_Platform_Client_Scanning_PdfScanDocumentGenerator.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
