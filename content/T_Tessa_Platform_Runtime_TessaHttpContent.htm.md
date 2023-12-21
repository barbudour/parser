# TessaHttpContent - класс
Вспомогательные методы для создания объектов
[HttpContent](https://learn.microsoft.com/dotnet/api/system.net.http.httpcontent).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class TessaHttpContent
VB __Копировать
     Public NotInheritable Class TessaHttpContent
C++ __Копировать
     public ref class TessaHttpContent abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type TessaHttpContent = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TessaHttpContent
##  __Свойства
[DefaultStreamingBufferSize](P_Tessa_Platform_Runtime_TessaHttpContent_DefaultStreamingBufferSize.htm)|
Размер буфера в байтах по умолчанию, который используется для потоковой
передачи. Обычно равен 1 Мб.  
---|---  
## __Методы
[FromBinary](M_Tessa_Platform_Runtime_TessaHttpContent_FromBinary.htm)|
Возвращает контент с двоичными данными, тип
[Binary](F_Tessa_Platform_Runtime_MediaTypes_Binary.htm).  
---|---  
[FromJson](M_Tessa_Platform_Runtime_TessaHttpContent_FromJson.htm)|
Возвращает контент с JSON-объектом, тип
[Json](F_Tessa_Platform_Runtime_MediaTypes_Json.htm).  
[FromJsonObject](M_Tessa_Platform_Runtime_TessaHttpContent_FromJsonObject.htm)|
Возвращает контент с JSON-объектом, тип
[Json](F_Tessa_Platform_Runtime_MediaTypes_Json.htm).  
[FromStream](M_Tessa_Platform_Runtime_TessaHttpContent_FromStream.htm)|
Возвращает контент из потока двоичных данных, тип
[Binary](F_Tessa_Platform_Runtime_MediaTypes_Binary.htm).  
[FromTessaBson(Byte[],
Boolean)](M_Tessa_Platform_Runtime_TessaHttpContent_FromTessaBson.htm)|
Возвращает контент с двоичными данными, тип
[TessaBson](F_Tessa_Platform_Runtime_MediaTypes_TessaBson.htm).  
[FromTessaBson(MemoryStream,
Boolean)](M_Tessa_Platform_Runtime_TessaHttpContent_FromTessaBson_1.htm)|
Возвращает контент с двоичными данными из буфера, тип
[TessaBson](F_Tessa_Platform_Runtime_MediaTypes_TessaBson.htm).  
[FromText](M_Tessa_Platform_Runtime_TessaHttpContent_FromText.htm)|
Возвращает контент с текстом, тип
[PlainText](F_Tessa_Platform_Runtime_MediaTypes_PlainText.htm).  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
