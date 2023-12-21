# PdfGeneratorContext.TemporaryFiles - свойство
Список временных файлов, которые будут гарантированно удалены после завершения
метода.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public List<ITempFile> TemporaryFiles { get; }
VB __Копировать
     Public ReadOnly Property TemporaryFiles As List(Of ITempFile)
    	Get
C++ __Копировать
     public:
    virtual property List<ITempFile^>^ TemporaryFiles {
    	List<ITempFile^>^ get () sealed;
    }
F# __Копировать
     abstract TemporaryFiles : List<ITempFile> with get
    override TemporaryFiles : List<ITempFile> with get
#### Значение свойства
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[ITempFile](T_Tessa_Platform_IO_ITempFile.htm)>
#### Реализации
[IPdfGeneratorContext.TemporaryFiles](P_Tessa_Extensions_Platform_Client_Scanning_IPdfGeneratorContext_TemporaryFiles.htm)  
##  __См. также
#### Ссылки
[PdfGeneratorContext -
](T_Tessa_Extensions_Platform_Client_Scanning_PdfGeneratorContext.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
