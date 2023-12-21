# ISessionToken - интерфейс
Токен, содержащий информацию по сессии.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISessionToken : ISessionSerializableObject, 
    	IBinarySerializable, IBsonSerializable, IJsonSerializable
VB __Копировать
     Public Interface ISessionToken
    	Inherits ISessionSerializableObject, IBinarySerializable, IBsonSerializable, IJsonSerializable
C++ __Копировать
     public interface class ISessionToken : ISessionSerializableObject, 
    	IBinarySerializable, IBsonSerializable, IJsonSerializable
F# __Копировать
     type ISessionToken = 
        interface
            interface ISessionSerializableObject
            interface IBinarySerializable
            interface IBsonSerializable
            interface IJsonSerializable
        end
Implements
    [IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm), [IBsonSerializable](T_Tessa_Platform_IBsonSerializable.htm), [IJsonSerializable](T_Tessa_Platform_IJsonSerializable.htm), [ISessionSerializableObject](T_Tessa_Platform_Runtime_ISessionSerializableObject.htm)
##  __Свойства
[AccessLevel](P_Tessa_Platform_Runtime_ISessionToken_AccessLevel.htm)| Уровень
доступа пользователя.  
---|---  
[ApplicationID](P_Tessa_Platform_Runtime_ISessionToken_ApplicationID.htm)|
Идентификатор приложения, которое открыло сессию.  
[Client64Bit](P_Tessa_Platform_Runtime_ISessionToken_Client64Bit.htm)|
Признак того, что клиентское приложение является 64-битным. true \- 64-битное
приложение, false \- 32-битное приложение, null \- разрядность неизвестна.  
[Client64BitOS](P_Tessa_Platform_Runtime_ISessionToken_Client64BitOS.htm)|
Признак того, что операционная система клиента является 64-битной. true \-
64-битная ОС, false \- 32-битная ОС, null \- разрядность неизвестна.  
[Created](P_Tessa_Platform_Runtime_ISessionToken_Created.htm)| Дата и время
создания токена.  
[Culture](P_Tessa_Platform_Runtime_ISessionToken_Culture.htm)| Региональные
настройки для пользователя.  
[DeviceType](P_Tessa_Platform_Runtime_ISessionToken_DeviceType.htm)| Тип
устройства, которое пользователь использует для подключения к серверу.  
[Expires](P_Tessa_Platform_Runtime_ISessionToken_Expires.htm)| Дата и время,
когда действие токена истекает, и он должен быть повторно сформирован.  
[HostIP](P_Tessa_Platform_Runtime_ISessionToken_HostIP.htm)|  IP-адрес
клиента, запрашивающего вход в систему, или null, если IP-адрес неизвестен.  
[HostName](P_Tessa_Platform_Runtime_ISessionToken_HostName.htm)|  Имя хоста
для клиента, запрашивающего вход в систему, или null, если имя хоста
неизвестно. В качестве имени хоста часто выступает имя компьютера клиента.  
[InstanceName](P_Tessa_Platform_Runtime_ISessionToken_InstanceName.htm)| Имя
экземпляра сервера.  
[IsActive](P_Tessa_Platform_Runtime_ISessionToken_IsActive.htm)|  Признак
того, что сессия является активной, т.е. обращение к ней не приведёт к
ошибкам. По умолчанию значение равно true. Значение не передаётся при
сериализации/десериализации, и оно всегда равно true, если объект токена не
создан с явным указанием значения false.  
[LicenseType](P_Tessa_Platform_Runtime_ISessionToken_LicenseType.htm)| Тип
лицензии, в соответствии с которой открыта сессия.  
[LoginType](P_Tessa_Platform_Runtime_ISessionToken_LoginType.htm)| Тип
аутентификации, выполненный для пользователя.  
[OSName](P_Tessa_Platform_Runtime_ISessionToken_OSName.htm)|  Название
операционной системы, используемой на устройстве пользователя, или null, если
ОС неизвестна.  
[ServerCode](P_Tessa_Platform_Runtime_ISessionToken_ServerCode.htm)| Код
сервера.  
[ServiceType](P_Tessa_Platform_Runtime_ISessionToken_ServiceType.htm)|  Тип
сессии, которые определяются типом веб-сервиса: для desktop- или для Web-
клиентов, или веб-сервис отсутствует (прямое взаимодействие с БД).  
[SessionID](P_Tessa_Platform_Runtime_ISessionToken_SessionID.htm)|
Идентификатор сессии, которая была создана в процессе аутентификации.  
[Signature](P_Tessa_Platform_Runtime_ISessionToken_Signature.htm)| Подпись
токена, подтверждающая его подлинность.  
[TimeZoneUtcOffset](P_Tessa_Platform_Runtime_ISessionToken_TimeZoneUtcOffset.htm)|
Смещение для временной зоны пользователя, заданное в карточке.  
[UICulture](P_Tessa_Platform_Runtime_ISessionToken_UICulture.htm)| Язык
интерфейса для пользователя.  
[UserAgent](P_Tessa_Platform_Runtime_ISessionToken_UserAgent.htm)|  Строка
UserAgent браузера, который подключается к серверу, или null, если для
подключения используется не браузер.  
[UserID](P_Tessa_Platform_Runtime_ISessionToken_UserID.htm)| Идентификатор
пользователя.  
[UserLogin](P_Tessa_Platform_Runtime_ISessionToken_UserLogin.htm)|  Логин
пользователя, в т.ч. аккаунт Windows или логин пользователя Tessa, или null,
если сессия не связана с действительным сотрудником системы.  
[UserName](P_Tessa_Platform_Runtime_ISessionToken_UserName.htm)| Имя
пользователя.  
[UtcOffset](P_Tessa_Platform_Runtime_ISessionToken_UtcOffset.htm)| Смещение
для пользователя относительно UTC.  
##  __Методы
[Deserialize(BinaryReader)](M_Tessa_Platform_IBinarySerializable_Deserialize.htm)|
Десериализует объект из бинарной формы.  
(Унаследован от
[IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm))  
---|---  
[Deserialize(BsonReader)](M_Tessa_Platform_IBsonSerializable_Deserialize.htm)|
Выполняет десериализацию объекта из бинарного JSON.  
(Унаследован от [IBsonSerializable](T_Tessa_Platform_IBsonSerializable.htm))  
[Deserialize(JsonReader)](M_Tessa_Platform_IJsonSerializable_Deserialize.htm)|
Выполняет десериализацию объекта из JSON.  
(Унаследован от [IJsonSerializable](T_Tessa_Platform_IJsonSerializable.htm))  
[Serialize(BinaryWriter)](M_Tessa_Platform_IBinarySerializable_Serialize.htm)|
Сериализует объект в бинарной форме.  
(Унаследован от
[IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm))  
[Serialize(BsonWriter)](M_Tessa_Platform_IBsonSerializable_Serialize.htm)|
Выполняет сериализацию объекта в бинарный JSON. Возвращает строку текста,
содержащую сериализованный объект.  
(Унаследован от [IBsonSerializable](T_Tessa_Platform_IBsonSerializable.htm))  
[Serialize(JsonWriter)](M_Tessa_Platform_IJsonSerializable_Serialize.htm)|
Выполняет сериализацию объекта в JSON. Возвращает строку текста, содержащую
сериализованный объект.  
(Унаследован от [IJsonSerializable](T_Tessa_Platform_IJsonSerializable.htm))  
[SerializeToBase64](M_Tessa_Platform_Runtime_ISessionSerializableObject_SerializeToBase64.htm)|
Выполняет сериализацию объекта в виде base64-строки.  
(Унаследован от
[ISessionSerializableObject](T_Tessa_Platform_Runtime_ISessionSerializableObject.htm))  
[SerializeToBinary(SessionSerializationOptions)](M_Tessa_Platform_Runtime_ISessionSerializableObject_SerializeToBinary_1.htm)|
Выполняет сериализацию объекта в виде массива байт.  
(Унаследован от
[ISessionSerializableObject](T_Tessa_Platform_Runtime_ISessionSerializableObject.htm))  
[SerializeToBinary(BinaryWriter,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_ISessionSerializableObject_SerializeToBinary.htm)|
Выполняет сериализацию объекта в бинарном виде, используя указанный объект для
записи.  
(Унаследован от
[ISessionSerializableObject](T_Tessa_Platform_Runtime_ISessionSerializableObject.htm))  
[SerializeToStorage(SessionSerializationOptions)](M_Tessa_Platform_Runtime_ISessionSerializableObject_SerializeToStorage_1.htm)|
Выполняет сериализацию объекта в сериализуемое хранилище Dictionary<string,
object>. Может использоваться для сериализации в Bson.  
(Унаследован от
[ISessionSerializableObject](T_Tessa_Platform_Runtime_ISessionSerializableObject.htm))  
[SerializeToStorage(Dictionary<String, Object>,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_ISessionSerializableObject_SerializeToStorage.htm)|
Выполняет сериализацию объекта в заданное сериализуемое хранилище
Dictionary<string, object>. Может использоваться для сериализации в Bson.  
(Унаследован от
[ISessionSerializableObject](T_Tessa_Platform_Runtime_ISessionSerializableObject.htm))  
[SerializeToXml(SessionSerializationOptions)](M_Tessa_Platform_Runtime_ISessionSerializableObject_SerializeToXml_2.htm)|
Возвращает строку, которая содержит сериализованный в XML объект.  
(Унаследован от
[ISessionSerializableObject](T_Tessa_Platform_Runtime_ISessionSerializableObject.htm))  
[SerializeToXml(Stream,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_ISessionSerializableObject_SerializeToXml.htm)|
Выполняет сериализацию объекта в XML в заданный поток.  
(Унаследован от
[ISessionSerializableObject](T_Tessa_Platform_Runtime_ISessionSerializableObject.htm))  
[SerializeToXml(XmlWriter,
SessionSerializationOptions)](M_Tessa_Platform_Runtime_ISessionSerializableObject_SerializeToXml_1.htm)|
Выполняет сериализацию текущего объекта и всех его дочерних объектов в элемент
XML.  
(Унаследован от
[ISessionSerializableObject](T_Tessa_Platform_Runtime_ISessionSerializableObject.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
