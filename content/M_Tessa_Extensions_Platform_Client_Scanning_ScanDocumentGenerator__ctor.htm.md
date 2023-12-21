# ScanDocumentGenerator - конструктор
Создаёт экземпляр класса с указанием дополнительных параметров, связанных с
генерацией документов.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     protected ScanDocumentGenerator(
    	Dictionary<string, Object> info = null
    )
VB __Копировать
     Protected Sub New ( 
    	Optional info As Dictionary(Of String, Object) = Nothing
    )
C++ __Копировать
     protected:
    ScanDocumentGenerator(
    	Dictionary<String^, Object^>^ info = nullptr
    )
F# __Копировать
     new : 
            ?info : Dictionary<string, Object> 
    (* Defaults:
            let _info = defaultArg info null
    *)
    -> ScanDocumentGenerator
#### Параметры
info
[Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)<[String](https://learn.microsoft.com/dotnet/api/system.string),
[Object](https://learn.microsoft.com/dotnet/api/system.object)> (Optional)
     Дополнительные параметры, связанные с генерацией документов, могут использоваться в расширениях. Если параметр равен null, то дополнительные параметры не передаются. 
## __См. также
#### Ссылки
[ScanDocumentGenerator -
](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentGenerator.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
