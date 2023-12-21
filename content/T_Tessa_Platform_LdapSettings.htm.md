# LdapSettings - класс
Настройки подключения к LDAP.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class LdapSettings : ILdapAuthSettings, 
    	ILdapSettings
VB __Копировать
     Public Class LdapSettings
    	Implements ILdapAuthSettings, ILdapSettings
C++ __Копировать
     public ref class LdapSettings : ILdapAuthSettings, 
    	ILdapSettings
F# __Копировать
     type LdapSettings = 
        class
            interface ILdapAuthSettings
            interface ILdapSettings
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ LdapSettings
Implements
    [ILdapAuthSettings](T_Tessa_Platform_ILdapAuthSettings.htm), [ILdapSettings](T_Tessa_Platform_ILdapSettings.htm)
##  __Заметки
Наследники класса могут добавлять дополнительные свойства.
## __Конструкторы
[LdapSettings](M_Tessa_Platform_LdapSettings__ctor.htm)| Инициализирует новый
экземпляр класса LdapSettings  
---|---  
##  __Свойства
[BindCredentials](P_Tessa_Platform_LdapSettings_BindCredentials.htm)|  Пароль
пользователя, от которого выполняется подключение к службам LDAP для поиска
сотрудника с его последующей авторизацией.  
---|---  
[BindDn](P_Tessa_Platform_LdapSettings_BindDn.htm)|  Имя пользователя (DN), от
которого выполняется подключение к службам LDAP для поиска сотрудника с его
последующей авторизацией.  
[ConnectionAttemptCount](P_Tessa_Platform_LdapSettings_ConnectionAttemptCount.htm)|
Количество попыток соединения с реферальными серверами. По умолчанию 10.  
[ConnectionAttemptPeriod](P_Tessa_Platform_LdapSettings_ConnectionAttemptPeriod.htm)|
Пауза между попытками соединения в секундах. По умолчанию 10.  
[IsEnabled](P_Tessa_Platform_LdapSettings_IsEnabled.htm)| Признак того, что
вход через LDAP включён.  
[Port](P_Tessa_Platform_LdapSettings_Port.htm)|  Порт, по которому выполняется
подключение. Если значение равно 0 или отрицательное число, то используется
порт по умолчанию в зависимости от свойства [ILdapSettings.UseSsl]: если true,
то порт 636; если false, то порт 389.  
[SearchBase](P_Tessa_Platform_LdapSettings_SearchBase.htm)|  Узел каталога или
домена, относительно которого выполняется поиск, например: dc=example,dc=com.  
[SearchFilter](P_Tessa_Platform_LdapSettings_SearchFilter.htm)|  Строка
фильтра, которая используется для поиска в каталоге или домене, например:
(&(objectClass=person)(cn={0})).  
[SkipReferral](P_Tessa_Platform_LdapSettings_SkipReferral.htm)| Отключение
поиска по всем реферальным серверам.  
[SkipReferralList](P_Tessa_Platform_LdapSettings_SkipReferralList.htm)|
Отключение поиска по списку реферальных серверов.  
[SkipSystemPartitions](P_Tessa_Platform_LdapSettings_SkipSystemPartitions.htm)|
Отключение поиска по реферальным серверов, таким как ForestDnsZones,
DomainDnsZones, Configuration  
[TimeoutMilliseconds](P_Tessa_Platform_LdapSettings_TimeoutMilliseconds.htm)|
Таймаут подключения в миллисекундах. Если значение равно 0 или отрицательное
число, то используется таймаут по умолчанию в зависимости от сервера LDAP
(обычно около 5 секунд).  
[Url](P_Tessa_Platform_LdapSettings_Url.htm)| Адрес подключения к службам
LDAP.  
[UseSsl](P_Tessa_Platform_LdapSettings_UseSsl.htm)| Признак того, что
используется защищённое подключение по протоколу SSL.  
##  __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[SetFromConfig](M_Tessa_Platform_LdapSettings_SetFromConfig.htm)|
Устанавливает значения свойств из секции конфигурации.  
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
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
