# MediaTypes - класс
Часто используемые типы MediaType для передачи запросов к сервисам Web API.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class MediaTypes
VB __Копировать
     Public NotInheritable Class MediaTypes
C++ __Копировать
     public ref class MediaTypes abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type MediaTypes = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ MediaTypes
##  __Поля
[Binary](F_Tessa_Platform_Runtime_MediaTypes_Binary.htm)|  Бинарный объект,
т.е. поток или массив байт.  
---|---  
[Json](F_Tessa_Platform_Runtime_MediaTypes_Json.htm)|  Объект, сериализованный
в JSON.  
[MultipartByteRanges](F_Tessa_Platform_Runtime_MediaTypes_MultipartByteRanges.htm)|
Контент multipart/byteranges, который может использоваться для передачи одного
или нескольких бинарных файлов с дополнительным содержимым.  
[MultipartFormData](F_Tessa_Platform_Runtime_MediaTypes_MultipartFormData.htm)|
Контент multipart/form-data, который может использоваться для передачи
параметров формы совместно с одним или несколькими бинарными файлами.  
[PlainText](F_Tessa_Platform_Runtime_MediaTypes_PlainText.htm)|  Простой
текст, доступный в виде строки.  
[TessaBson](F_Tessa_Platform_Runtime_MediaTypes_TessaBson.htm)|  Объект,
сериализованный в бинарный JSON с использованием правил сериализации TESSA.  
[TessaBsonDeflate](F_Tessa_Platform_Runtime_MediaTypes_TessaBsonDeflate.htm)|
Объект, сериализованный в бинарный JSON с использованием правил сериализации
TESSA, для которого затем выполняется deflate-сжатие.  
[TessaBsonDeflateName](F_Tessa_Platform_Runtime_MediaTypes_TessaBsonDeflateName.htm)|
Имя объекта, сериализованного в бинарный JSON с использованием правил
сериализации TESSA, для которого затем выполняется deflate-сжатие.  
[TessaBsonName](F_Tessa_Platform_Runtime_MediaTypes_TessaBsonName.htm)|  Имя
объекта, сериализованного в бинарный JSON с использованием правил сериализации
TESSA.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
