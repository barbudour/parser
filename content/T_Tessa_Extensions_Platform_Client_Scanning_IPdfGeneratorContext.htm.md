# IPdfGeneratorContext - интерфейс
Контекст операции по генерации PDF из изображений со страницами. Используется
совместно с
[IPdfGenerator](T_Tessa_Extensions_Platform_Client_Scanning_IPdfGenerator.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPdfGeneratorContext
VB __Копировать
     Public Interface IPdfGeneratorContext
C++ __Копировать
     public interface class IPdfGeneratorContext
F# __Копировать
     type IPdfGeneratorContext = interface end
##  __Свойства
[AddStamp](P_Tessa_Extensions_Platform_Client_Scanning_IPdfGeneratorContext_AddStamp.htm)|
Признак того, что для документа требуется вывести штамп. При этом формирование
штампа обычно выполняется посредством расширений.  
---|---  
[ExternalContext](P_Tessa_Extensions_Platform_Client_Scanning_IPdfGeneratorContext_ExternalContext.htm)|
Контекст, в пределах которого выполняется формирование PDF. Например, может
быть контекстом
[IFileControlExtensionContext](T_Tessa_UI_Files_IFileControlExtensionContext.htm)
или null, если контекст неизвестен.  
[GeneratorInfo](P_Tessa_Extensions_Platform_Client_Scanning_IPdfGeneratorContext_GeneratorInfo.htm)|
Информация для расширений, заданная в генераторе, обычно это объект
[ScanDocumentGenerator](T_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentGenerator.htm).
Информация недоступна для изменений.  
[Info](P_Tessa_Extensions_Platform_Client_Scanning_IPdfGeneratorContext_Info.htm)|
Информация для расширений, существующая в рамках запроса по генерации.  
[PngPageFiles](P_Tessa_Extensions_Platform_Client_Scanning_IPdfGeneratorContext_PngPageFiles.htm)|
Файлы изображений в формате PNG со страницами в порядке их добавления. В одном
файле содержится изображение для одной страницы.  
[TemporaryFiles](P_Tessa_Extensions_Platform_Client_Scanning_IPdfGeneratorContext_TemporaryFiles.htm)|
Список временных файлов, которые будут гарантированно удалены после завершения
метода.  
[TemporaryFolders](P_Tessa_Extensions_Platform_Client_Scanning_IPdfGeneratorContext_TemporaryFolders.htm)|
Список временных папок, которые будут гарантированно удалены после завершения
метода.  
## __Методы
[ReportProgressAsync](M_Tessa_Extensions_Platform_Client_Scanning_IPdfGeneratorContext_ReportProgressAsync.htm)|
Отображает пользователю текущий прогресс операции.  
---|---  
## __См. также
#### Ссылки
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
