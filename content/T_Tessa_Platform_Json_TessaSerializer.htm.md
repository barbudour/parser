# TessaSerializer - класс
##  __Definition
 **Пространство имён:** [Tessa.Platform.Json](N_Tessa_Platform_Json.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class TessaSerializer
VB __Копировать
     Public Class TessaSerializer
C++ __Копировать
     public ref class TessaSerializer
F# __Копировать
     type TessaSerializer = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TessaSerializer
##  __Конструкторы
[TessaSerializer](M_Tessa_Platform_Json_TessaSerializer__ctor.htm)|
Инициализирует новый экземпляр класса TessaSerializer  
---|---  
##  __Свойства
[Instance](P_Tessa_Platform_Json_TessaSerializer_Instance.htm)| Экземпляр
класса.  
---|---  
[Json](P_Tessa_Platform_Json_TessaSerializer_Json.htm)|  Объект, выполняющий
сериализацию с использованием конвертера
[TessaJsonConverter](T_Tessa_Platform_Json_TessaJsonConverter.htm),
поддерживающего интерфейсы
[IJsonSerializable](T_Tessa_Platform_IJsonSerializable.htm) и
[IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm). Возвращаемый
объект безопасно использовать в том потоке, в котором он был получен.
Рекомендуется каждый раз после конструкции await получать значение заново.  
[JsonTyped](P_Tessa_Platform_Json_TessaSerializer_JsonTyped.htm)|  Объект,
выполняющий сериализацию с использованием конвертера
[TypedJsonConverter](T_Tessa_Platform_Json_TypedJsonConverter.htm), который
обеспечивает преобразование Dictionary<string, object> в текстовый формат JSON
с учётом типобезопасности, т.е. при десериализации будет восстановлена
информация по типам, если это сериализуемые типы в структуре карточки или
других подобных объектов. Возвращаемый объект безопасно использовать в том
потоке, в котором он был получен. Рекомендуется каждый раз после конструкции
await получать значение заново.  
## __Методы
[Create(Action<JsonSerializerSettings>)](M_Tessa_Platform_Json_TessaSerializer_Create_1.htm)|  
---|---  
[Create(JsonSerializerSettings)](M_Tessa_Platform_Json_TessaSerializer_Create.htm)|  
[CreateDefaultSettings](M_Tessa_Platform_Json_TessaSerializer_CreateDefaultSettings.htm)|  
[CreateTyped(Action<JsonSerializerSettings>)](M_Tessa_Platform_Json_TessaSerializer_CreateTyped_1.htm)|  
[CreateTyped(JsonSerializerSettings,
Boolean)](M_Tessa_Platform_Json_TessaSerializer_CreateTyped.htm)|  
[Deserialize](M_Tessa_Platform_Json_TessaSerializer_Deserialize.htm)|
Десериализует текст в формате JSON.  
[DeserializeJson](M_Tessa_Platform_Json_TessaSerializer_DeserializeJson.htm)|  
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
[SerializeJson(Dictionary<String, Object>,
Boolean)](M_Tessa_Platform_Json_TessaSerializer_SerializeJson_1.htm)|  
[SerializeJson(JsonWriter, Dictionary<String,
Object>)](M_Tessa_Platform_Json_TessaSerializer_SerializeJson.htm)|  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[JsonMaxDepth](F_Tessa_Platform_Json_TessaSerializer_JsonMaxDepth.htm)|
Максимальная глубина вложенности JSON, допустимая для чтения стандартными
средствами платформы.  
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
