# ScanDocumentHelper - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.Scanning](N_Tessa_Extensions_Platform_Client_Scanning.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public static class ScanDocumentHelper
VB __Копировать
     Public NotInheritable Class ScanDocumentHelper
C++ __Копировать
     public ref class ScanDocumentHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type ScanDocumentHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ScanDocumentHelper
##  __Методы
[EncodeInJpegAsync(Stream, String,
Int32)](M_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentHelper_EncodeInJpegAsync.htm)|
Выполняет кодирование изображения любого допустимого формата из потока
sourceStream в формат JPEG, совместимый с PDF.  
---|---  
[EncodeInJpegAsync(String, String,
Int32)](M_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentHelper_EncodeInJpegAsync_1.htm)|
Выполняет кодирование изображения любого допустимого формата из файла
sourceName в формат JPEG, совместимый с PDF.  
[EncodeInPngAsync(Stream,
String)](M_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentHelper_EncodeInPngAsync.htm)|  
[EncodeInPngAsync(String,
String)](M_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentHelper_EncodeInPngAsync_1.htm)|  
[GetPageFileName](M_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentHelper_GetPageFileName.htm)|
Возвращает имя файла со страницей по умолчанию, доступной по индексу,
отсчитываемому от нуля.  
[GetPageName](M_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentHelper_GetPageName.htm)|
Возвращает имя страницы по умолчанию, доступной по индексу, отсчитываемому от
нуля. Для того, чтобы получить имя файла со страницей, добавьте расширение с
ведущей точкой (обычно используется метод
[GetPageFileName(Int32)](M_Tessa_Extensions_Platform_Client_Scanning_ScanDocumentHelper_GetPageFileName.htm)).  
## __См. также
#### Ссылки
[Tessa.Extensions.Platform.Client.Scanning - пространство
имён](N_Tessa_Extensions_Platform_Client_Scanning.htm)
