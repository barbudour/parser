# ScanFileDialogSettings.DocumentTypesOverride - свойство
Настройка, позволяющая переопределить типы генерируемых документов по
умолчанию на заданный список типов. Если значение равно null (по умолчанию),
то используется список типов по умолчанию
[DefaultTypes](P_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentType_DefaultTypes.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public List<ScanDocumentType> DocumentTypesOverride { get; set; }
VB __Копировать
     Public Property DocumentTypesOverride As List(Of ScanDocumentType)
    	Get
    	Set
C++ __Копировать
     public:
    property List<ScanDocumentType^>^ DocumentTypesOverride {
    	List<ScanDocumentType^>^ get ();
    	void set (List<ScanDocumentType^>^ value);
    }
F# __Копировать
     member DocumentTypesOverride : List<ScanDocumentType> with get, set
#### Значение свойства
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[ScanDocumentType](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentType.htm)>
##  __См. также
#### Ссылки
[ScanFileDialogSettings -
](T_Tessa_Extensions_Platform_Client_Scanning_ScanFileDialogSettings.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
