# SessionToken - класс
Токен, содержащий информацию по сессии.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class SessionToken : SessionSerializableObject, 
    	ISessionToken, ISessionSerializableObject, IBinarySerializable, IBsonSerializable, IJsonSerializable
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class SessionToken
    	Inherits SessionSerializableObject
    	Implements ISessionToken, ISessionSerializableObject, IBinarySerializable, IBsonSerializable, 
    	IJsonSerializable
C++ __Копировать
    [SerializableAttribute]
    public ref class SessionToken sealed : public SessionSerializableObject, 
    	ISessionToken, ISessionSerializableObject, IBinarySerializable, IBsonSerializable, IJsonSerializable
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type SessionToken = 
        class
            inherit SessionSerializableObject
            interface ISessionToken
            interface ISessionSerializableObject
            interface IBinarySerializable
            interface IBsonSerializable
            interface IJsonSerializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm) __ SessionToken
Implements
    [IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm), [IBsonSerializable](T_Tessa_Platform_IBsonSerializable.htm), [IJsonSerializable](T_Tessa_Platform_IJsonSerializable.htm), [ISessionSerializableObject](T_Tessa_Platform_Runtime_ISessionSerializableObject.htm), [ISessionToken](T_Tessa_Platform_Runtime_ISessionToken.htm)
##  __Конструкторы
[SessionToken(ISessionToken)](M_Tessa_Platform_Runtime_SessionToken__ctor_2.htm)|
Создаёт экземпляр класса, заполняя свойства создаваемого объекта по свойствам
заданного объекта.  
---|---  
[SessionToken(Guid, String, UserAccessLevel, String, String, String,
Nullable<Guid>, Nullable<Guid>, Nullable<DeviceType>, CultureInfo,
CultureInfo, Nullable<TimeSpan>, Nullable<TimeSpan>, Nullable<Boolean>,
Nullable<Boolean>,
Boolean)](M_Tessa_Platform_Runtime_SessionToken__ctor_1.htm)|  Создаёт
экземпляр класса с указанием основных параметров сессии. Рекомендуется для
указания фиктивной сессии, например, сессии системы
[CreateSystemSession(SessionType,
ITessaServerSettings)](M_Tessa_Platform_Runtime_Session_CreateSystemSession.htm).
Для большинства параметров подходят значения по умолчанию.  
[SessionToken(Guid, Guid, String, String, String, DateTime, DateTime,
SessionLicenseType, SessionServiceType, UserLoginType, UserAccessLevel,
DeviceType, Guid, String, String, String, String, String, String, CultureInfo,
CultureInfo, TimeSpan, TimeSpan, Nullable<Boolean>, Nullable<Boolean>,
Boolean)](M_Tessa_Platform_Runtime_SessionToken__ctor.htm)|  Создаёт экземпляр
класса с указанием значений его свойств.  
## __Свойства
[AccessLevel](P_Tessa_Platform_Runtime_SessionToken_AccessLevel.htm)| Уровень
доступа пользователя.  
---|---  
[ApplicationID](P_Tessa_Platform_Runtime_SessionToken_ApplicationID.htm)|
Идентификатор приложения, которое открыло сессию.  
[Client64Bit](P_Tessa_Platform_Runtime_SessionToken_Client64Bit.htm)|  Признак
того, что клиентское приложение является 64-битным. true \- 64-битное
приложение, false \- 32-битное приложение, null \- разрядность неизвестна.  
[Client64BitOS](P_Tessa_Platform_Runtime_SessionToken_Client64BitOS.htm)|
Признак того, что операционная система клиента является 64-битной. true \-
64-битная ОС, false \- 32-битная ОС, null \- разрядность неизвестна.  
[Created](P_Tessa_Platform_Runtime_SessionToken_Created.htm)| Дата и время
создания токена.  
[Culture](P_Tessa_Platform_Runtime_SessionToken_Culture.htm)| Региональные
настройки для пользователя.  
[DeviceType](P_Tessa_Platform_Runtime_SessionToken_DeviceType.htm)| Тип
устройства, которое пользователь использует для подключения к серверу.  
[Expires](P_Tessa_Platform_Runtime_SessionToken_Expires.htm)| Дата и время,
когда действие токена истекает, и он должен быть повторно сформирован.  
[HostIP](P_Tessa_Platform_Runtime_SessionToken_HostIP.htm)|  IP-адрес клиента,
запрашивающего вход в систему, или null, если IP-адрес неизвестен.  
[HostName](P_Tessa_Platform_Runtime_SessionToken_HostName.htm)|  Имя хоста для
клиента, запрашивающего вход в систему, или null, если имя хоста неизвестно. В
качестве имени хоста часто выступает имя компьютера клиента.  
[InstanceName](P_Tessa_Platform_Runtime_SessionToken_InstanceName.htm)| Имя
экземпляра сервера.  
[IsActive](P_Tessa_Platform_Runtime_SessionToken_IsActive.htm)|  Признак того,
что сессия является активной, т.е. обращение к ней не приведёт к ошибкам. По
умолчанию значение равно true. Значение не передаётся при
сериализации/десериализации, и оно всегда равно true, если объект токена не
создан с явным указанием значения false.  
[IsSealed](P_Tessa_Platform_Runtime_SessionSerializableObject_IsSealed.htm)|
Признак того, что объект был защищён от изменений.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
[LicenseType](P_Tessa_Platform_Runtime_SessionToken_LicenseType.htm)| Тип
лицензии, в соответствии с которой открыта сессия.  
[LoginType](P_Tessa_Platform_Runtime_SessionToken_LoginType.htm)| Тип
аутентификации, выполненный для пользователя.  
[OSName](P_Tessa_Platform_Runtime_SessionToken_OSName.htm)|  Название
операционной системы, используемой на устройстве пользователя, или null, если
ОС неизвестна.  
[ServerCode](P_Tessa_Platform_Runtime_SessionToken_ServerCode.htm)| Код
сервера.  
[ServiceType](P_Tessa_Platform_Runtime_SessionToken_ServiceType.htm)|  Тип
сессии, которые определяются типом веб-сервиса: для desktop- или для Web-
клиентов, или веб-сервис отсутствует (прямое взаимодействие с БД).  
[SessionID](P_Tessa_Platform_Runtime_SessionToken_SessionID.htm)|
Идентификатор сессии, которая была создана в процессе аутентификации.  
[Signature](P_Tessa_Platform_Runtime_SessionToken_Signature.htm)| Подпись
токена, подтверждающая его подлинность.  
[TimeZoneUtcOffset](P_Tessa_Platform_Runtime_SessionToken_TimeZoneUtcOffset.htm)|
Смещение для временной зоны пользователя, заданное в карточке.  
[UICulture](P_Tessa_Platform_Runtime_SessionToken_UICulture.htm)| Язык
интерфейса для пользователя.  
[UserAgent](P_Tessa_Platform_Runtime_SessionToken_UserAgent.htm)|  Строка
UserAgent браузера, который подключается к серверу, или null, если для
подключения используется не браузер.  
[UserID](P_Tessa_Platform_Runtime_SessionToken_UserID.htm)| Идентификатор
пользователя.  
[UserLogin](P_Tessa_Platform_Runtime_SessionToken_UserLogin.htm)|  Логин
пользователя, в т.ч. аккаунт Windows или логин пользователя Tessa, или null,
если сессия не связана с действительным сотрудником системы.  
[UserName](P_Tessa_Platform_Runtime_SessionToken_UserName.htm)| Имя
пользователя.  
[UtcOffset](P_Tessa_Platform_Runtime_SessionToken_UtcOffset.htm)| Смещение для
пользователя относительно UTC.  
[XmlElementName](P_Tessa_Platform_Runtime_SessionToken_XmlElementName.htm)|
Имя элемента XML для сериализуемого объекта сессии.  
(Переопределяет
[SessionSerializableObject.XmlElementName](P_Tessa_Platform_Runtime_SessionSerializableObject_XmlElementName.htm))  
##  __Методы
[CheckSealed](M_Tessa_Platform_Runtime_SessionSerializableObject_CheckSealed.htm)|
Выбрасывает исключение [Tessa.Platform.ObjectSealedException], если объект был
защищён от изменений.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
---|---  
[DeserializeAttributeFromXmlCore](M_Tessa_Platform_Runtime_SessionToken_DeserializeAttributeFromXmlCore.htm)|
Выполняется для каждого атрибута десериализуемого атрибута.  
(Переопределяет
[SessionSerializableObject.DeserializeAttributeFromXmlCore(String,
String)](M_Tessa_Platform_Runtime_SessionSerializableObject_DeserializeAttributeFromXmlCore.htm))  
[DeserializeElementFromXmlCore](M_Tessa_Platform_Runtime_SessionSerializableObject_DeserializeElementFromXmlCore.htm)|
Выполняется для каждого элемента десериализуемого объекта.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
[DeserializeFromBase64](M_Tessa_Platform_Runtime_SessionToken_DeserializeFromBase64.htm)|
Выполняет десериализацию объекта, сериализованного в бинарном виде, используя
указанную base64-строку с сериализованным объектом.  
[DeserializeFromBase64Core](M_Tessa_Platform_Runtime_SessionSerializableObject_DeserializeFromBase64Core.htm)|
Выполняет десериализацию объекта, сериализованного в виде base64-строки в
указанном массиве байт.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
[DeserializeFromBinary(BinaryReader)](M_Tessa_Platform_Runtime_SessionToken_DeserializeFromBinary_1.htm)|
Выполняет десериализацию объекта, сериализованного в бинарном виде, используя
указанный объект для чтения.  
[DeserializeFromBinary(Byte[])](M_Tessa_Platform_Runtime_SessionToken_DeserializeFromBinary.htm)|
Выполняет десериализацию объекта, сериализованного в бинарном виде, используя
указанный массив байт с сериализованным объектом.  
[DeserializeFromBinaryCore(BinaryReader)](M_Tessa_Platform_Runtime_SessionToken_DeserializeFromBinaryCore.htm)|
Выполняет десериализацию объекта, сериализованного в бинарном виде, используя
указанный объект для чтения.  
(Переопределяет
[SessionSerializableObject.DeserializeFromBinaryCore(BinaryReader)](M_Tessa_Platform_Runtime_SessionSerializableObject_DeserializeFromBinaryCore_1.htm))  
[DeserializeFromBinaryCore(Byte[])](M_Tessa_Platform_Runtime_SessionSerializableObject_DeserializeFromBinaryCore.htm)|
Выполняет десериализацию объекта, сериализованного в бинарном виде в указанном
массиве байт.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
[DeserializeFromStorage](M_Tessa_Platform_Runtime_SessionToken_DeserializeFromStorage.htm)|
Выполняет десериализацию объекта из заданного сериализуемого хранилища
Dictionary<string, object>.  
[DeserializeFromStorageCore](M_Tessa_Platform_Runtime_SessionToken_DeserializeFromStorageCore.htm)|
Выполняет десериализацию объекта из заданного сериализуемого хранилища
Dictionary<string, object>.  
(Переопределяет
[SessionSerializableObject.DeserializeFromStorageCore(Dictionary<String,
Object>)](M_Tessa_Platform_Runtime_SessionSerializableObject_DeserializeFromStorageCore.htm))  
[DeserializeFromXml(Stream)](M_Tessa_Platform_Runtime_SessionToken_DeserializeFromXml.htm)|
Выполняет десериализацию объекта из XML из заданного потока.  
[DeserializeFromXml(String)](M_Tessa_Platform_Runtime_SessionToken_DeserializeFromXml_1.htm)|
Выполняет десериализацию объекта из XML, заданного посредством строки.  
[DeserializeFromXml(XmlReader)](M_Tessa_Platform_Runtime_SessionToken_DeserializeFromXml_2.htm)|
Выполняет десериализацию объекта и всех его дочерних объектов из элемента XML.  
[DeserializeFromXmlCore(Stream)](M_Tessa_Platform_Runtime_SessionSerializableObject_DeserializeFromXmlCore.htm)|
Выполняет десериализацию объекта из XML из заданного потока.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
[DeserializeFromXmlCore(String)](M_Tessa_Platform_Runtime_SessionSerializableObject_DeserializeFromXmlCore_1.htm)|
Выполняет десериализацию объекта из XML, заданного посредством строки.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
[DeserializeFromXmlCore(XmlReader)](M_Tessa_Platform_Runtime_SessionSerializableObject_DeserializeFromXmlCore_2.htm)|
Выполняет десериализацию объекта и всех его дочерних объектов из элемента XML.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
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
[InvalidateSerializationCache](M_Tessa_Platform_Runtime_SessionSerializableObject_InvalidateSerializationCache.htm)|
Сбрасывает кэш сериализованных данных, которые ускоряют повторную
сериализацию. Требуется вызывать этот метод после любого изменения свойств.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnDeserializing](M_Tessa_Platform_Runtime_SessionToken_OnDeserializing.htm)|
Выполняется перед десериализацией объекта. В методе рекомендуется заполнить
значения полей по умолчанию.  
(Переопределяет
[SessionSerializableObject.OnDeserializing()](M_Tessa_Platform_Runtime_SessionSerializableObject_OnDeserializing.htm))  
[Seal](M_Tessa_Platform_Runtime_SessionSerializableObject_Seal.htm)| Защищает
объект от изменений.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
[SealInternal](M_Tessa_Platform_Runtime_SessionSerializableObject_SealInternal.htm)|
Защищает объект от изменений.
Метод может быть переопределён в классах-наследниках.
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
[SerializeAttributesToXmlCore](M_Tessa_Platform_Runtime_SessionToken_SerializeAttributesToXmlCore.htm)|
Выполняет сериализацию текущего объекта в атрибуты XML.  
(Переопределяет
[SessionSerializableObject.SerializeAttributesToXmlCore(XmlWriter,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeAttributesToXmlCore.htm))  
[SerializeElementsToXmlCore](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeElementsToXmlCore.htm)|
Выполняет сериализацию всех дочерних объектов для текущего объекта в элементы
XML.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
[SerializeToBase64](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToBase64.htm)|
Выполняет сериализацию объекта в виде base64-строки.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
[SerializeToBinary(SessionSerializationOptions)](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToBinary_1.htm)|
Выполняет сериализацию объекта в виде массива байт.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
[SerializeToBinary(BinaryWriter,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToBinary.htm)|
Выполняет сериализацию объекта в бинарном виде, используя указанный объект для
записи.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
[SerializeToBinaryCore](M_Tessa_Platform_Runtime_SessionToken_SerializeToBinaryCore.htm)|
Выполняет сериализацию объекта в бинарном виде, используя указанный объект для
записи.  
(Переопределяет [SessionSerializableObject.SerializeToBinaryCore(BinaryWriter,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToBinaryCore.htm))  
[SerializeToStorage(SessionSerializationOptions)](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToStorage_1.htm)|
Выполняет сериализацию объекта в сериализуемое хранилище Dictionary<string,
object>. Может использоваться для сериализации в Bson.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
[SerializeToStorage(Dictionary<String, Object>,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToStorage.htm)|
Выполняет сериализацию объекта в заданное сериализуемое хранилище
Dictionary<string, object>. Может использоваться для сериализации в Bson.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
[SerializeToStorageCore](M_Tessa_Platform_Runtime_SessionToken_SerializeToStorageCore.htm)|
Выполняет сериализацию объекта в заданное сериализуемое хранилище
Dictionary<string, object>. Может использоваться для сериализации в Bson.  
(Переопределяет
[SessionSerializableObject.SerializeToStorageCore(Dictionary<String, Object>,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToStorageCore.htm))  
[SerializeToXml(SessionSerializationOptions)](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToXml_2.htm)|
Возвращает строку, которая содержит сериализованный в XML объект.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
[SerializeToXml(Stream,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToXml.htm)|
Выполняет сериализацию объекта в XML в заданный поток.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
[SerializeToXml(XmlWriter,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_SessionSerializableObject_SerializeToXml_1.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в элемент
XML.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
[ToString](M_Tessa_Platform_Runtime_SessionSerializableObject_ToString.htm)|
Возвращает строковое представление объекта.  
(Унаследован от
[SessionSerializableObject](T_Tessa_Platform_Runtime_SessionSerializableObject.htm))  
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
