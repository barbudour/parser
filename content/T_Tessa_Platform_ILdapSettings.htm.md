# ILdapSettings - интерфейс
Настройки подключения к LDAP.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ILdapSettings
VB __Копировать
     Public Interface ILdapSettings
C++ __Копировать
     public interface class ILdapSettings
F# __Копировать
     type ILdapSettings = interface end
##  __Свойства
[BindCredentials](P_Tessa_Platform_ILdapSettings_BindCredentials.htm)|  Пароль
пользователя, от которого выполняется подключение к службам LDAP для поиска
сотрудника с его последующей авторизацией.  
---|---  
[BindDn](P_Tessa_Platform_ILdapSettings_BindDn.htm)|  Имя пользователя (DN),
от которого выполняется подключение к службам LDAP для поиска сотрудника с его
последующей авторизацией.  
[ConnectionAttemptCount](P_Tessa_Platform_ILdapSettings_ConnectionAttemptCount.htm)|
Количество попыток соединения с реферальными серверами. По умолчанию 10.  
[ConnectionAttemptPeriod](P_Tessa_Platform_ILdapSettings_ConnectionAttemptPeriod.htm)|
Пауза между попытками соединения в секундах. По умолчанию 10.  
[Port](P_Tessa_Platform_ILdapSettings_Port.htm)|  Порт, по которому
выполняется подключение. Если значение равно 0 или отрицательное число, то
используется порт по умолчанию в зависимости от свойства
[ILdapSettings.UseSsl]: если true, то порт 636; если false, то порт 389.  
[SkipReferral](P_Tessa_Platform_ILdapSettings_SkipReferral.htm)| Отключение
поиска по всем реферальным серверам.  
[SkipReferralList](P_Tessa_Platform_ILdapSettings_SkipReferralList.htm)|
Отключение поиска по списку реферальных серверов.  
[SkipSystemPartitions](P_Tessa_Platform_ILdapSettings_SkipSystemPartitions.htm)|
Отключение поиска по реферальным серверов, таким как ForestDnsZones,
DomainDnsZones, Configuration  
[TimeoutMilliseconds](P_Tessa_Platform_ILdapSettings_TimeoutMilliseconds.htm)|
Таймаут подключения в миллисекундах. Если значение равно 0 или отрицательное
число, то используется таймаут по умолчанию в зависимости от сервера LDAP
(обычно около 5 секунд).  
[Url](P_Tessa_Platform_ILdapSettings_Url.htm)| Адрес подключения к службам
LDAP.  
[UseSsl](P_Tessa_Platform_ILdapSettings_UseSsl.htm)| Признак того, что
используется защищённое подключение по протоколу SSL.  
##  __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
