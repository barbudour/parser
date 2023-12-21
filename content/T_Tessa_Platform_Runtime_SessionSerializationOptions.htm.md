# SessionSerializationOptions - класс
Настройки сериализации объектов
[ISessionSerializableObject](T_Tessa_Platform_Runtime_ISessionSerializableObject.htm).
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SessionSerializationOptions : IEquatable<SessionSerializationOptions>, 
    	ISealable
VB __Копировать
     Public NotInheritable Class SessionSerializationOptions
    	Implements IEquatable(Of SessionSerializationOptions), ISealable
C++ __Копировать
     public ref class SessionSerializationOptions sealed : IEquatable<SessionSerializationOptions^>, 
    	ISealable
F# __Копировать
     [<SealedAttribute>]
    type SessionSerializationOptions = 
        class
            interface IEquatable<SessionSerializationOptions>
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SessionSerializationOptions
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<SessionSerializationOptions>, [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Конструкторы
[SessionSerializationOptions](M_Tessa_Platform_Runtime_SessionSerializationOptions__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
##  __Свойства
[Auth](P_Tessa_Platform_Runtime_SessionSerializationOptions_Auth.htm)|  Объект
с настройками для передачи на сервер для аутентификации.  
---|---  
[Default](P_Tessa_Platform_Runtime_SessionSerializationOptions_Default.htm)|
Объект с настройками по умолчанию.  
[IsSealed](P_Tessa_Platform_Runtime_SessionSerializationOptions_IsSealed.htm)|
Признак того, что объект был защищён от изменений.  
[Mode](P_Tessa_Platform_Runtime_SessionSerializationOptions_Mode.htm)|  Способ
сериализации объектов
[ISessionSerializableObject](T_Tessa_Platform_Runtime_ISessionSerializableObject.htm).
По умолчанию принимается значение
[Full](T_Tessa_Platform_Runtime_SessionSerializationMode.htm).  
## __Методы
[Equals(Object)](M_Tessa_Platform_Runtime_SessionSerializationOptions_Equals.htm)|
Сравнивает текущий объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
---|---  
[Equals(SessionSerializationOptions)](M_Tessa_Platform_Runtime_SessionSerializationOptions_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Platform_Runtime_SessionSerializationOptions_GetHashCode.htm)|
Возвращает хеш-код объекта.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
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
[Seal](M_Tessa_Platform_Runtime_SessionSerializationOptions_Seal.htm)|
Защищает объект от изменений.  
[ToString](M_Tessa_Platform_Runtime_SessionSerializationOptions_ToString.htm)|
Возвращает строковое представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
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
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
