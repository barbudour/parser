# OpenSessionRequest - класс
Запрос на открытие сессии. Содержит учётные данные для входа и параметры
открываемой сессии, включая информацию о приложении и о клиенте.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public class OpenSessionRequest : SessionClientParameters
VB __Копировать
    <SerializableAttribute>
    <DataContractAttribute>
    Public Class OpenSessionRequest
    	Inherits SessionClientParameters
C++ __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public ref class OpenSessionRequest : public SessionClientParameters
F# __Копировать
     [<SerializableAttribute>]
    [<DataContractAttribute>]
    type OpenSessionRequest = 
        class
            inherit SessionClientParameters
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm) __[SessionClientParameters](T_Tessa_Platform_Runtime_SessionClientParameters.htm) __ OpenSessionRequest
##  __Конструкторы
[OpenSessionRequest](M_Tessa_Platform_Runtime_OpenSessionRequest__ctor.htm)|
Инициализирует новый экземпляр класса OpenSessionRequest  
---|---  
##  __Свойства
[ApplicationID](P_Tessa_Platform_Runtime_OpenSessionRequest_ApplicationID.htm)|
Идентификатор приложения, для которого выполняется вход. Доступные
идентификаторы перечислены в классе
[ApplicationIdentifiers](T_Tessa_Platform_Runtime_ApplicationIdentifiers.htm).
Если указано null, то используется
[Other](F_Tessa_Platform_Runtime_ApplicationIdentifiers_Other.htm).  
---|---  
[Client64Bit](P_Tessa_Platform_Runtime_SessionClientParameters_Client64Bit.htm)|
Признак того, что клиентское приложение является 64-битным. true \- 64-битное
приложение, false \- 32-битное приложение, null \- разрядность неизвестна.  
(Унаследован от
[SessionClientParameters](T_Tessa_Platform_Runtime_SessionClientParameters.htm))  
[Client64BitOS](P_Tessa_Platform_Runtime_SessionClientParameters_Client64BitOS.htm)|
Признак того, что операционная система клиента является 64-битной. true \-
64-битная ОС, false \- 32-битная ОС, null \- разрядность неизвестна.  
(Унаследован от
[SessionClientParameters](T_Tessa_Platform_Runtime_SessionClientParameters.htm))  
[CultureLCID](P_Tessa_Platform_Runtime_SessionClientParameters_CultureLCID.htm)|
Идентификатор региональных настроек
[LCID](https://learn.microsoft.com/dotnet/api/system.globalization.cultureinfo.lcid#system-
globalization-cultureinfo-lcid) или 0, если используются текущие настройки.  
(Унаследован от
[SessionClientParameters](T_Tessa_Platform_Runtime_SessionClientParameters.htm))  
[DeviceType](P_Tessa_Platform_Runtime_SessionClientParameters_DeviceType.htm)|
Тип устройства [DeviceType](T_Tessa_Platform_Runtime_DeviceType.htm), которое
пользователь использует для подключения к серверу.  
(Унаследован от
[SessionClientParameters](T_Tessa_Platform_Runtime_SessionClientParameters.htm))  
[EncodeBase64](P_Tessa_Platform_Runtime_OpenSessionRequest_EncodeBase64.htm)|
Признак того, что логин и пароль передаются с кодированием base-64. В
противном случае они передаются в исходном виде.  
[Login](P_Tessa_Platform_Runtime_OpenSessionRequest_Login.htm)|  Логин
пользователя в формате строки base-64. Используйте методы
[GetLoginAndPassword()](M_Tessa_Platform_Runtime_OpenSessionRequest_GetLoginAndPassword.htm)
и [SetLoginAndPassword(String,
String)](M_Tessa_Platform_Runtime_OpenSessionRequest_SetLoginAndPassword.htm)
для установки и проверки значений с учётом кодирования. Если логин
[Login](P_Tessa_Platform_Runtime_OpenSessionRequest_Login.htm) или пароль
[Password](P_Tessa_Platform_Runtime_OpenSessionRequest_Password.htm) равны
null или пустой строке, то используется Windows-аутентификация. Это можно
проверить в методе
[HasLoginAndPassword()](M_Tessa_Platform_Runtime_OpenSessionRequest_HasLoginAndPassword.htm).  
[OSName](P_Tessa_Platform_Runtime_SessionClientParameters_OSName.htm)|
Название операционной системы, используемой на устройстве пользователя, или
null, если ОС неизвестна.  
(Унаследован от
[SessionClientParameters](T_Tessa_Platform_Runtime_SessionClientParameters.htm))  
[Password](P_Tessa_Platform_Runtime_OpenSessionRequest_Password.htm)|  Пароль
пользователя в формате строки base-64. Используйте методы
[GetLoginAndPassword()](M_Tessa_Platform_Runtime_OpenSessionRequest_GetLoginAndPassword.htm)
и [SetLoginAndPassword(String,
String)](M_Tessa_Platform_Runtime_OpenSessionRequest_SetLoginAndPassword.htm)
для установки и проверки значений с учётом кодирования. Если логин
[Login](P_Tessa_Platform_Runtime_OpenSessionRequest_Login.htm) или пароль
[Password](P_Tessa_Platform_Runtime_OpenSessionRequest_Password.htm) равны
null или пустой строке, то используется Windows-аутентификация. Это можно
проверить в методе
[HasLoginAndPassword()](M_Tessa_Platform_Runtime_OpenSessionRequest_HasLoginAndPassword.htm).  
[ServiceType](P_Tessa_Platform_Runtime_OpenSessionRequest_ServiceType.htm)|
Тип сессии, который определяется типом веб-приложения.  
[UICultureLCID](P_Tessa_Platform_Runtime_SessionClientParameters_UICultureLCID.htm)|
Идентификатор языка интерфейса
[LCID](https://learn.microsoft.com/dotnet/api/system.globalization.cultureinfo.lcid#system-
globalization-cultureinfo-lcid) или 0, если используются текущие настройки.  
(Унаследован от
[SessionClientParameters](T_Tessa_Platform_Runtime_SessionClientParameters.htm))  
[UserAgent](P_Tessa_Platform_Runtime_SessionClientParameters_UserAgent.htm)|
Строка UserAgent браузера, который подключается к серверу, или null, если для
подключения используется не браузер.  
(Унаследован от
[SessionClientParameters](T_Tessa_Platform_Runtime_SessionClientParameters.htm))  
[UtcOffsetMinutes](P_Tessa_Platform_Runtime_SessionClientParameters_UtcOffsetMinutes.htm)|
Количество минут смещения в часовой зоне пользователя относительно UTC. Если
указано null, то используется смещение в карточке сотрудника, или смещение во
временной зоне по умолчанию (если в карточке сотрудника отсутствует), или
смещение на сервере приложений (если карточка настроек отсутствует, это обычно
в процессе установки системы).  
(Унаследован от
[SessionClientParameters](T_Tessa_Platform_Runtime_SessionClientParameters.htm))  
##  __Методы
[Deserialize(BinaryReader)](M_Tessa_Platform_Runtime_OpenSessionRequest_Deserialize.htm)|
Десериализует объект из бинарной формы.  
(Переопределяет
[SessionClientParameters.Deserialize(BinaryReader)](M_Tessa_Platform_Runtime_SessionClientParameters_Deserialize.htm))  
---|---  
[Deserialize(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_Deserialize.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[DeserializeAndGetCore](M_Tessa_Platform_Storage_StorageSerializable_DeserializeAndGetCore.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[DeserializeCore](M_Tessa_Platform_Runtime_OpenSessionRequest_DeserializeCore.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Переопределяет [SessionClientParameters.DeserializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Runtime_SessionClientParameters_DeserializeCore.htm))  
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
[GetLoginAndPassword](M_Tessa_Platform_Runtime_OpenSessionRequest_GetLoginAndPassword.htm)|
Возвращает логин и пароль пользователя после декодирования.  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[HasLoginAndPassword](M_Tessa_Platform_Runtime_OpenSessionRequest_HasLoginAndPassword.htm)|
Возвращает признак того, что заданы непустые логин или пароль.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Serialize(BinaryWriter)](M_Tessa_Platform_Runtime_OpenSessionRequest_Serialize.htm)|
Сериализует объект в бинарной форме.  
(Переопределяет
[SessionClientParameters.Serialize(BinaryWriter)](M_Tessa_Platform_Runtime_SessionClientParameters_Serialize.htm))  
[Serialize(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_Serialize.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[SerializeCore](M_Tessa_Platform_Runtime_OpenSessionRequest_SerializeCore.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Переопределяет [SessionClientParameters.SerializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Runtime_SessionClientParameters_SerializeCore.htm))  
[SetLoginAndPassword](M_Tessa_Platform_Runtime_OpenSessionRequest_SetLoginAndPassword.htm)|
Устанавливает логин и пароль пользователя, при этом выполняется их
кодирование.  
[SetParameters](M_Tessa_Platform_Runtime_OpenSessionRequest_SetParameters.htm)|
Устанавливает свойства текущего объекта по заданным параметрам.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
