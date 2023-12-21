# SessionClientParameters - класс
Параметры сессии, полученные с клиента в процессе открытия сессии.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public class SessionClientParameters : StorageSerializable, 
    	IBinarySerializable
VB __Копировать
    <SerializableAttribute>
    <DataContractAttribute>
    Public Class SessionClientParameters
    	Inherits StorageSerializable
    	Implements IBinarySerializable
C++ __Копировать
    [SerializableAttribute]
    [DataContractAttribute]
    public ref class SessionClientParameters : public StorageSerializable, 
    	IBinarySerializable
F# __Копировать
     [<SerializableAttribute>]
    [<DataContractAttribute>]
    type SessionClientParameters = 
        class
            inherit StorageSerializable
            interface IBinarySerializable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm) __ SessionClientParameters
Derived
[Tessa.Platform.Runtime.OpenSessionRequest](T_Tessa_Platform_Runtime_OpenSessionRequest.htm)
Implements
    [IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm)
##  __Конструкторы
[SessionClientParameters](M_Tessa_Platform_Runtime_SessionClientParameters__ctor.htm)|
Инициализирует новый экземпляр класса SessionClientParameters  
---|---  
##  __Свойства
[Client64Bit](P_Tessa_Platform_Runtime_SessionClientParameters_Client64Bit.htm)|
Признак того, что клиентское приложение является 64-битным. true \- 64-битное
приложение, false \- 32-битное приложение, null \- разрядность неизвестна.  
---|---  
[Client64BitOS](P_Tessa_Platform_Runtime_SessionClientParameters_Client64BitOS.htm)|
Признак того, что операционная система клиента является 64-битной. true \-
64-битная ОС, false \- 32-битная ОС, null \- разрядность неизвестна.  
[CultureLCID](P_Tessa_Platform_Runtime_SessionClientParameters_CultureLCID.htm)|
Идентификатор региональных настроек
[LCID](https://learn.microsoft.com/dotnet/api/system.globalization.cultureinfo.lcid#system-
globalization-cultureinfo-lcid) или 0, если используются текущие настройки.  
[DeviceType](P_Tessa_Platform_Runtime_SessionClientParameters_DeviceType.htm)|
Тип устройства [DeviceType](T_Tessa_Platform_Runtime_DeviceType.htm), которое
пользователь использует для подключения к серверу.  
[OSName](P_Tessa_Platform_Runtime_SessionClientParameters_OSName.htm)|
Название операционной системы, используемой на устройстве пользователя, или
null, если ОС неизвестна.  
[UICultureLCID](P_Tessa_Platform_Runtime_SessionClientParameters_UICultureLCID.htm)|
Идентификатор языка интерфейса
[LCID](https://learn.microsoft.com/dotnet/api/system.globalization.cultureinfo.lcid#system-
globalization-cultureinfo-lcid) или 0, если используются текущие настройки.  
[UserAgent](P_Tessa_Platform_Runtime_SessionClientParameters_UserAgent.htm)|
Строка UserAgent браузера, который подключается к серверу, или null, если для
подключения используется не браузер.  
[UtcOffsetMinutes](P_Tessa_Platform_Runtime_SessionClientParameters_UtcOffsetMinutes.htm)|
Количество минут смещения в часовой зоне пользователя относительно UTC. Если
указано null, то используется смещение в карточке сотрудника, или смещение во
временной зоне по умолчанию (если в карточке сотрудника отсутствует), или
смещение на сервере приложений (если карточка настроек отсутствует, это обычно
в процессе установки системы).  
## __Методы
[CreateCurrent](M_Tessa_Platform_Runtime_SessionClientParameters_CreateCurrent.htm)|
Создаёт параметры сессии на основании текущих настроек пользователя.  
---|---  
[Deserialize(BinaryReader)](M_Tessa_Platform_Runtime_SessionClientParameters_Deserialize.htm)|
Десериализует объект из бинарной формы.  
[Deserialize(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_Deserialize.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[DeserializeAndGetCore](M_Tessa_Platform_Storage_StorageSerializable_DeserializeAndGetCore.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[DeserializeCore](M_Tessa_Platform_Runtime_SessionClientParameters_DeserializeCore.htm)|
Выполняет десериализацию полей объекта из заданного хранилища.  
(Переопределяет [StorageSerializable.DeserializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_DeserializeCore.htm))  
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
[Serialize(BinaryWriter)](M_Tessa_Platform_Runtime_SessionClientParameters_Serialize.htm)|
Сериализует объект в бинарной форме.  
[Serialize(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_Serialize.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Унаследован от
[StorageSerializable](T_Tessa_Platform_Storage_StorageSerializable.htm))  
[SerializeCore](M_Tessa_Platform_Runtime_SessionClientParameters_SerializeCore.htm)|
Выполняет сериализацию полей объекта в заданное хранилище.  
(Переопределяет [StorageSerializable.SerializeCore(Dictionary<String,
Object>)](M_Tessa_Platform_Storage_StorageSerializable_SerializeCore.htm))  
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
