# PdfGeneratorContext.PngPageFiles - свойство
Файлы изображений в формате PNG со страницами в порядке их добавления. В одном
файле содержится изображение для одной страницы.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public List<ITempFile> PngPageFiles { get; }
VB __Копировать
     Public ReadOnly Property PngPageFiles As List(Of ITempFile)
    	Get
C++ __Копировать
     public:
    virtual property List<ITempFile^>^ PngPageFiles {
    	List<ITempFile^>^ get () sealed;
    }
F# __Копировать
     abstract PngPageFiles : List<ITempFile> with get
    override PngPageFiles : List<ITempFile> with get
#### Значение свойства
[List](https://learn.microsoft.com/dotnet/api/system.collections.generic.list-1)<[ITempFile](T_Tessa_Platform_IO_ITempFile.htm)>
#### Реализации
[IPdfGeneratorContext.PngPageFiles](P_Tessa_Extensions_Platform_Client_Scanning_IPdfGeneratorContext_PngPageFiles.htm)  
##  __См. также
#### Ссылки
[PdfGeneratorContext -
](T_Tessa_Extensions_Platform_Client_Scanning_PdfGeneratorContext.htm)
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
