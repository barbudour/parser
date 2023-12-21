# ILdapAuthSettings - интерфейс
Настройки подключения к LDAP.
## __Definition
 **Пространство имён:** [Tessa.Platform](N_Tessa_Platform.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ILdapAuthSettings : ILdapSettings
VB __Копировать
     Public Interface ILdapAuthSettings
    	Inherits ILdapSettings
C++ __Копировать
     public interface class ILdapAuthSettings : ILdapSettings
F# __Копировать
     type ILdapAuthSettings = 
        interface
            interface ILdapSettings
        end
Implements
    [ILdapSettings](T_Tessa_Platform_ILdapSettings.htm)
##  __Свойства
[BindCredentials](P_Tessa_Platform_ILdapSettings_BindCredentials.htm)|  Пароль
пользователя, от которого выполняется подключение к службам LDAP для поиска
сотрудника с его последующей авторизацией.  
(Унаследован от [ILdapSettings](T_Tessa_Platform_ILdapSettings.htm))  
---|---  
[BindDn](P_Tessa_Platform_ILdapSettings_BindDn.htm)|  Имя пользователя (DN),
от которого выполняется подключение к службам LDAP для поиска сотрудника с его
последующей авторизацией.  
(Унаследован от [ILdapSettings](T_Tessa_Platform_ILdapSettings.htm))  
[ConnectionAttemptCount](P_Tessa_Platform_ILdapSettings_ConnectionAttemptCount.htm)|
Количество попыток соединения с реферальными серверами. По умолчанию 10.  
(Унаследован от [ILdapSettings](T_Tessa_Platform_ILdapSettings.htm))  
[ConnectionAttemptPeriod](P_Tessa_Platform_ILdapSettings_ConnectionAttemptPeriod.htm)|
Пауза между попытками соединения в секундах. По умолчанию 10.  
(Унаследован от [ILdapSettings](T_Tessa_Platform_ILdapSettings.htm))  
[IsEnabled](P_Tessa_Platform_ILdapAuthSettings_IsEnabled.htm)| Признак того,
что подключение к LDAP по указанным настройкам разрешено.  
[Port](P_Tessa_Platform_ILdapSettings_Port.htm)|  Порт, по которому
выполняется подключение. Если значение равно 0 или отрицательное число, то
используется порт по умолчанию в зависимости от свойства
[ILdapSettings.UseSsl]: если true, то порт 636; если false, то порт 389.  
(Унаследован от [ILdapSettings](T_Tessa_Platform_ILdapSettings.htm))  
[SearchBase](P_Tessa_Platform_ILdapAuthSettings_SearchBase.htm)| Каталог, в
котором выполняется поиск сотрудника для его авторизации.  
[SearchFilter](P_Tessa_Platform_ILdapAuthSettings_SearchFilter.htm)|  Строка с
фильтром, используемая для поиска сотрудника. Вместо {0} в строку
подставляется поле "Аккаунт" из карточки сотрудника.  
[SkipReferral](P_Tessa_Platform_ILdapSettings_SkipReferral.htm)| Отключение
поиска по всем реферальным серверам.  
(Унаследован от [ILdapSettings](T_Tessa_Platform_ILdapSettings.htm))  
[SkipReferralList](P_Tessa_Platform_ILdapSettings_SkipReferralList.htm)|
Отключение поиска по списку реферальных серверов.  
(Унаследован от [ILdapSettings](T_Tessa_Platform_ILdapSettings.htm))  
[SkipSystemPartitions](P_Tessa_Platform_ILdapSettings_SkipSystemPartitions.htm)|
Отключение поиска по реферальным серверов, таким как ForestDnsZones,
DomainDnsZones, Configuration  
(Унаследован от [ILdapSettings](T_Tessa_Platform_ILdapSettings.htm))  
[TimeoutMilliseconds](P_Tessa_Platform_ILdapSettings_TimeoutMilliseconds.htm)|
Таймаут подключения в миллисекундах. Если значение равно 0 или отрицательное
число, то используется таймаут по умолчанию в зависимости от сервера LDAP
(обычно около 5 секунд).  
(Унаследован от [ILdapSettings](T_Tessa_Platform_ILdapSettings.htm))  
[Url](P_Tessa_Platform_ILdapSettings_Url.htm)| Адрес подключения к службам
LDAP.  
(Унаследован от [ILdapSettings](T_Tessa_Platform_ILdapSettings.htm))  
[UseSsl](P_Tessa_Platform_ILdapSettings_UseSsl.htm)| Признак того, что
используется защищённое подключение по протоколу SSL.  
(Унаследован от [ILdapSettings](T_Tessa_Platform_ILdapSettings.htm))  
##  __См. также
#### Ссылки
[Tessa.Platform - пространство имён](N_Tessa_Platform.htm)
