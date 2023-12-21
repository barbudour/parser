# IPdfPageExtractorContext - интерфейс
Контекст операции по разбору файла PDF на страницы. Используется совместно с
[IPdfPageExtractor](T_Tessa_Extensions_Platform_Client_Scanning_IPdfPageExtractor.htm).
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IPdfPageExtractorContext
VB __Копировать
     Public Interface IPdfPageExtractorContext
C++ __Копировать
     public interface class IPdfPageExtractorContext
F# __Копировать
     type IPdfPageExtractorContext = interface end
##  __Свойства
[PdfFilePath](P_Tessa_Extensions_Platform_Client_Scanning_IPdfPageExtractorContext_PdfFilePath.htm)|
Полный путь к файлу PDF.  
---|---  
[PngPageFiles](P_Tessa_Extensions_Platform_Client_Scanning_IPdfPageExtractorContext_PngPageFiles.htm)|
Массив объектов, которые описывают все извлечённые страницы в виде изображений
PNG.  
[Settings](P_Tessa_Extensions_Platform_Client_Scanning_IPdfPageExtractorContext_Settings.htm)|
Настройки диалога сканирования, для которых вызывается извлечение страниц.
Может быть равны null, если настройки неизвестны.  
## __Методы
[ReportProgressAsync](M_Tessa_Extensions_Platform_Client_Scanning_IPdfPageExtractorContext_ReportProgressAsync.htm)|
Отображает пользователю текущий прогресс операции.  
---|---  
## __См. также
#### Ссылки
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
