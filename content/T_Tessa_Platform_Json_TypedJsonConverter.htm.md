# TypedJsonConverter - класс
##  __Definition
 **Пространство имён:** [Tessa.Platform.Json](N_Tessa_Platform_Json.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class TypedJsonConverter : JsonConverter, 
    	ISealable
VB __Копировать
     Public Class TypedJsonConverter
    	Inherits JsonConverter
    	Implements ISealable
C++ __Копировать
     public ref class TypedJsonConverter : public JsonConverter, 
    	ISealable
F# __Копировать
     type TypedJsonConverter = 
        class
            inherit JsonConverter
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ JsonConverter __ TypedJsonConverter
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Конструкторы
[TypedJsonConverter](M_Tessa_Platform_Json_TypedJsonConverter__ctor.htm)|
Инициализирует новый экземпляр класса TypedJsonConverter  
---|---  
##  __Свойства
[ContentReadingFailedList](P_Tessa_Platform_Json_TypedJsonConverter_ContentReadingFailedList.htm)|
Список контента, который по какой-либо причине не удалось получить.  
---|---  
[ContentSubDirectorySource](P_Tessa_Platform_Json_TypedJsonConverter_ContentSubDirectorySource.htm)|
Провайдер источника для внешнего контента.  
[ConvertKeysCamelToPascalCasing](P_Tessa_Platform_Json_TypedJsonConverter_ConvertKeysCamelToPascalCasing.htm)|
Преобразует регистр ключей из camelCasing в PascalCasing.  
[ConvertKeysIdentifierCasing](P_Tessa_Platform_Json_TypedJsonConverter_ConvertKeysIdentifierCasing.htm)|
Преобразует регистр для строки "id" в "ID". Рекомендуется использовать
совместно с
[ConvertKeysCamelToPascalCasing](P_Tessa_Platform_Json_TypedJsonConverter_ConvertKeysCamelToPascalCasing.htm).  
[DeserializedTypedInfo](P_Tessa_Platform_Json_TypedJsonConverter_DeserializedTypedInfo.htm)|
Признак того, что был десериализован хотя бы один ключ с информацией по типам
вида ::type  
[IsSealed](P_Tessa_Platform_Json_TypedJsonConverter_IsSealed.htm)| Признак
того, что объект был защищён от изменений.  
[StorageContentList](P_Tessa_Platform_Json_TypedJsonConverter_StorageContentList.htm)|
Хранит список путей storage-контента. Для того чтобы вызывающий код имел к ним
доступ. Например, это необходимо, чтобы сделать проверку на лишние файлы в
поддиректории после импорта карточки.  
## __Методы
[CanConvert](M_Tessa_Platform_Json_TypedJsonConverter_CanConvert.htm)|  
(Переопределяет JsonConverter.CanConvert(Type))  
---|---  
[CheckSealed](M_Tessa_Platform_Json_TypedJsonConverter_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
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
[PackNameWithType](M_Tessa_Platform_Json_TypedJsonConverter_PackNameWithType.htm)|  
[ReadJson](M_Tessa_Platform_Json_TypedJsonConverter_ReadJson.htm)|  
(Переопределяет JsonConverter.ReadJson(JsonReader, Type, Object,
JsonSerializer))  
[Seal](M_Tessa_Platform_Json_TypedJsonConverter_Seal.htm)| Защищает объект от
изменений.  
[SealInternal](M_Tessa_Platform_Json_TypedJsonConverter_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[TryGetExtendedType](M_Tessa_Platform_Json_TypedJsonConverter_TryGetExtendedType.htm)|  
[TryGetExtendedTypeToken](M_Tessa_Platform_Json_TypedJsonConverter_TryGetExtendedTypeToken.htm)|  
[TryGetType](M_Tessa_Platform_Json_TypedJsonConverter_TryGetType.htm)|  
[TryGetTypeToken](M_Tessa_Platform_Json_TypedJsonConverter_TryGetTypeToken.htm)|  
[UnpackNameWithType](M_Tessa_Platform_Json_TypedJsonConverter_UnpackNameWithType.htm)|  
[WriteJson](M_Tessa_Platform_Json_TypedJsonConverter_WriteJson.htm)|  
(Переопределяет JsonConverter.WriteJson(JsonWriter, Object, JsonSerializer))  
##  __Поля
[ArrayToken](F_Tessa_Platform_Json_TypedJsonConverter_ArrayToken.htm)|  
---|---  
[BinaryContentReferenceToken](F_Tessa_Platform_Json_TypedJsonConverter_BinaryContentReferenceToken.htm)|  
[BooleanToken](F_Tessa_Platform_Json_TypedJsonConverter_BooleanToken.htm)|  
[ExtraTypes](F_Tessa_Platform_Json_TypedJsonConverter_ExtraTypes.htm)|  Типы
данных, которые десериализуются с суффиксами в дополнение к
[Types](F_Tessa_Platform_Json_TypedJsonConverter_Types.htm).  
[ExtraTypeTokens](F_Tessa_Platform_Json_TypedJsonConverter_ExtraTypeTokens.htm)|
Суффиксы типов данных, которые десериализуются в дополнение к
[TypeTokens](F_Tessa_Platform_Json_TypedJsonConverter_TypeTokens.htm).  
[LongToken](F_Tessa_Platform_Json_TypedJsonConverter_LongToken.htm)|  
[ObjectToken](F_Tessa_Platform_Json_TypedJsonConverter_ObjectToken.htm)|  
[SingleTypeKey](F_Tessa_Platform_Json_TypedJsonConverter_SingleTypeKey.htm)|  
[StringToken](F_Tessa_Platform_Json_TypedJsonConverter_StringToken.htm)|  
[TextContentReferenceToken](F_Tessa_Platform_Json_TypedJsonConverter_TextContentReferenceToken.htm)|  
[TextpartToken](F_Tessa_Platform_Json_TypedJsonConverter_TextpartToken.htm)|  
[Types](F_Tessa_Platform_Json_TypedJsonConverter_Types.htm)|  Типы данных,
которые сериализуются и десериализуются с суффиксами.  
[TypesKey](F_Tessa_Platform_Json_TypedJsonConverter_TypesKey.htm)|  
[TypeTokens](F_Tessa_Platform_Json_TypedJsonConverter_TypeTokens.htm)|
Суффиксы типов данных, которые сериализуются и десериализуются.  
[UnknownToken](F_Tessa_Platform_Json_TypedJsonConverter_UnknownToken.htm)|  
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
