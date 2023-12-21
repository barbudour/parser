# PdfGeneratorContext.TemporaryFolders - свойство
Список временных папок, которые будут гарантированно удалены после завершения
метода.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public List<ITempFolder> TemporaryFolders { get; }
VB __Копировать
     Public ReadOnly Property TemporaryFolders As List(Of ITempFolder)
    	Get
C++ __Копировать
     public:
    virtual property List<ITempFolder^>^ TemporaryFolders {
    	List<ITempFolder^>^ get () sealed;
    }
F# __Копировать
     abstract TemporaryFolders : List<ITempFolder> with get
    override TemporaryFolders : List<ITempFolder> with get
#### Значение свойства
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[ITempFolder](T_Tessa_Platform_IO_ITempFolder.htm)>
#### Реализации
[IPdfGeneratorContext.TemporaryFolders](P_Tessa_Extensions_Platform_Client_Scanning_IPdfGeneratorContext_TemporaryFolders.htm)  
##  __См. также
#### Ссылки
[PdfGeneratorContext -
](T_Tessa_Extensions_Platform_Client_Scanning_PdfGeneratorContext.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
