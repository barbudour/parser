# ScanFileDialogSettings.DocumentTypeFilterFunc - свойство
Функция, получающая тип документа и возвращающая признак того, что этот тип
документа доступен для выбора.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public Func<ScanDocumentType, bool> DocumentTypeFilterFunc { get; set; }
VB __Копировать
     Public Property DocumentTypeFilterFunc As Func(Of ScanDocumentType, Boolean)
    	Get
    	Set
C++ __Копировать
     public:
    property Func<ScanDocumentType^, bool>^ DocumentTypeFilterFunc {
    	Func<ScanDocumentType^, bool>^ get ();
    	void set (Func<ScanDocumentType^, bool>^ value);
    }
F# __Копировать
     member DocumentTypeFilterFunc : Func<ScanDocumentType, bool> with get, set
#### Значение свойства
[Func](https://learn.microsoft.com/dotnet/api/system.func-2)<[ScanDocumentType](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentType.htm),
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)>
##  __См. также
#### Ссылки
[ScanFileDialogSettings -
](T_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
