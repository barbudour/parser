# TessaJsonSerializationContext - класс
Контекст операции для сериализации/десериализации с учетом
[JsonTextPart](T_Tessa_Platform_Json_JsonTextPart.htm)
##  __Definition
 **Пространство имён:** [Tessa.Platform.Json](N_Tessa_Platform_Json.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class TessaJsonSerializationContext : ITessaJsonSerializationContext
VB __Копировать
     Public Class TessaJsonSerializationContext
    	Implements ITessaJsonSerializationContext
C++ __Копировать
     public ref class TessaJsonSerializationContext : ITessaJsonSerializationContext
F# __Копировать
     type TessaJsonSerializationContext = 
        class
            interface ITessaJsonSerializationContext
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ TessaJsonSerializationContext
Implements
    [ITessaJsonSerializationContext](T_Tessa_Platform_Json_ITessaJsonSerializationContext.htm)
##  __Конструкторы
[TessaJsonSerializationContext](M_Tessa_Platform_Json_TessaJsonSerializationContext__ctor.htm)|
Инициализирует новый экземпляр класса TessaJsonSerializationContext  
---|---  
##  __Свойства
[Current](P_Tessa_Platform_Json_TessaJsonSerializationContext_Current.htm)|
Текущий контекст
[ITessaJsonSerializationContext](T_Tessa_Platform_Json_ITessaJsonSerializationContext.htm).  
---|---  
[DefaultNamespaces](P_Tessa_Platform_Json_TessaJsonSerializationContext_DefaultNamespaces.htm)|  
[HasCurrent](P_Tessa_Platform_Json_TessaJsonSerializationContext_HasCurrent.htm)|
Признак того, что текущий код выполняется внутри операции с контекстом
[ITessaJsonSerializationContext](T_Tessa_Platform_Json_ITessaJsonSerializationContext.htm),
а свойство
[Current](P_Tessa_Platform_Json_TessaJsonSerializationContext_Current.htm)
ссылается на действительный контекст.  
[TextParts](P_Tessa_Platform_Json_TessaJsonSerializationContext_TextParts.htm)|  
[Unknown](P_Tessa_Platform_Json_TessaJsonSerializationContext_Unknown.htm)|
Неизвестный контекст
[ITessaJsonSerializationContext](T_Tessa_Platform_Json_ITessaJsonSerializationContext.htm).  
## __Методы
[Create](M_Tessa_Platform_Json_TessaJsonSerializationContext_Create.htm)|
Создаёт область операции, в которой заданный контекст будет являться текущим.  
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
[Register](M_Tessa_Platform_Json_TessaJsonSerializationContext_Register.htm)|
Регистрация TextPart-а.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Поля
[Version](F_Tessa_Platform_Json_TessaJsonSerializationContext_Version.htm)|  
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
