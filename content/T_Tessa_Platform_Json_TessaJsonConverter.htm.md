# TessaJsonConverter - класс
Конвертер JSON, выполняющий сериализацию объектов с поддержкой интерфейсов
[IJsonSerializable](T_Tessa_Platform_IJsonSerializable.htm) и
[IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm). Для бинарной
сериализации выполняется преобразование в объект, в котором по ключу
[Base64Key](F_Tessa_Platform_Json_TessaJsonConverter_Base64Key.htm) содержится
бинарное представление в виде base64-строки. Конвертер используется, например,
для обмена данными с веб-сервисами ASP.NET Core. Чтобы задействовать
сериализатор по умолчанию с этим конвертером рекомендуется использовать
свойство [Json](P_Tessa_Platform_Json_TessaSerializer_Json.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Json](N_Tessa_Platform_Json.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class TessaJsonConverter : JsonConverter
VB __Копировать
     Public Class TessaJsonConverter
    	Inherits JsonConverter
C++ __Копировать
     public ref class TessaJsonConverter : public JsonConverter
F# __Копировать
     type TessaJsonConverter = 
        class
            inherit JsonConverter
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ JsonConverter __ TessaJsonConverter
##  __Конструкторы
[TessaJsonConverter](M_Tessa_Platform_Json_TessaJsonConverter__ctor.htm)|
Инициализирует новый экземпляр класса TessaJsonConverter  
---|---  
##  __Методы
[CanConvert](M_Tessa_Platform_Json_TessaJsonConverter_CanConvert.htm)|  
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
[ReadBinaryObjectFromBase64](M_Tessa_Platform_Json_TessaJsonConverter_ReadBinaryObjectFromBase64.htm)|  
[ReadJson](M_Tessa_Platform_Json_TessaJsonConverter_ReadJson.htm)|  
(Переопределяет JsonConverter.ReadJson(JsonReader, Type, Object,
JsonSerializer))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[WriteBinaryObjectAsBase64](M_Tessa_Platform_Json_TessaJsonConverter_WriteBinaryObjectAsBase64.htm)|  
[WriteJson](M_Tessa_Platform_Json_TessaJsonConverter_WriteJson.htm)|  
(Переопределяет JsonConverter.WriteJson(JsonWriter, Object, JsonSerializer))  
##  __Поля
[Base64Key](F_Tessa_Platform_Json_TessaJsonConverter_Base64Key.htm)|  Ключ, по
которому бинарный объект
[IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm) сериализуется
в текстовый JSON.  
---|---  
## __Методы расширения
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
