# GuidConverter - класс
Конвертер используемый только для записи Guid при сериализации c помощью
JsonSerializer. Преобразует Guid из xxxx-xxxxxx-xxxxx-xxxx в
xxxxxxxxxxxxxxxxxxxx. Для обратной конвертации используется следует
исползовать стандартный конвертер.
## __Definition
 **Пространство имён:** [Tessa.Platform.Json](N_Tessa_Platform_Json.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class GuidConverter : JsonConverter
VB __Копировать
     Public Class GuidConverter
    	Inherits JsonConverter
C++ __Копировать
     public ref class GuidConverter : public JsonConverter
F# __Копировать
     type GuidConverter = 
        class
            inherit JsonConverter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ JsonConverter __ GuidConverter
##  __Конструкторы
[GuidConverter](M_Tessa_Platform_Json_GuidConverter__ctor.htm)| Инициализирует
новый экземпляр класса GuidConverter  
---|---  
##  __Свойства
[CanRead](P_Tessa_Platform_Json_GuidConverter_CanRead.htm)|  Gets a value
indicating whether this JsonConverter can read JSON.  
(Переопределяет JsonConverter.CanRead)  
---|---  
[CanWrite](P_Tessa_Platform_Json_GuidConverter_CanWrite.htm)|  Gets a value
indicating whether this JsonConverter can write JSON.  
(Переопределяет JsonConverter.CanWrite)  
##  __Методы
[CanConvert](M_Tessa_Platform_Json_GuidConverter_CanConvert.htm)|  Determines
whether this instance can convert the specified object type.  
(Переопределяет JsonConverter.CanConvert(Type))  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[ReadJson](M_Tessa_Platform_Json_GuidConverter_ReadJson.htm)|  Reads the JSON
representation of the object.  
(Переопределяет JsonConverter.ReadJson(JsonReader, Type, Object,
JsonSerializer))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[WriteJson](M_Tessa_Platform_Json_GuidConverter_WriteJson.htm)|  Writes the
JSON representation of the object.  
(Переопределяет JsonConverter.WriteJson(JsonWriter, Object, JsonSerializer))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Json - пространство имён](N_Tessa_Platform_Json.htm)
