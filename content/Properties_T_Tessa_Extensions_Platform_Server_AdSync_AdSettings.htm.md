# AdSettings - свойства
##  __Свойства
[BindCredentials](P_Tessa_Extensions_Platform_Server_AdSync_AdSettings_BindCredentials.htm)|
Пароль пользователя, от которого выполняется подключение к службам LDAP для
поиска сотрудника с его последующей авторизацией.  
---|---  
[BindDn](P_Tessa_Extensions_Platform_Server_AdSync_AdSettings_BindDn.htm)|
Имя пользователя (DN), от которого выполняется подключение к службам LDAP для
поиска сотрудника с его последующей авторизацией.  
[ConnectionAttemptCount](P_Tessa_Extensions_Platform_Server_AdSync_AdSettings_ConnectionAttemptCount.htm)|
Количество попыток соединения с реферальными серверами. По умолчанию 10.  
[ConnectionAttemptPeriod](P_Tessa_Extensions_Platform_Server_AdSync_AdSettings_ConnectionAttemptPeriod.htm)|
Пауза между попытками соединения в секундах. По умолчанию 10.  
[DisableStaticRoleRename](P_Tessa_Extensions_Platform_Server_AdSync_AdSettings_DisableStaticRoleRename.htm)|
Отключить переименование статических ролей.  
[OURoots](P_Tessa_Extensions_Platform_Server_AdSync_AdSettings_OURoots.htm)|
Корни синхронизации.  
[OURootsSR](P_Tessa_Extensions_Platform_Server_AdSync_AdSettings_OURootsSR.htm)|
Корни синхронизации для статических ролей.  
[Port](P_Tessa_Extensions_Platform_Server_AdSync_AdSettings_Port.htm)|  Порт,
по которому выполняется подключение. Если значение равно 0 или отрицательное
число, то используется порт по умолчанию в зависимости от свойства
[ILdapSettings.UseSsl]: если true, то порт 636; если false, то порт 389.  
[SkipReferral](P_Tessa_Extensions_Platform_Server_AdSync_AdSettings_SkipReferral.htm)|
Отключение поиска по всем реферальным серверам.  
[SkipReferralList](P_Tessa_Extensions_Platform_Server_AdSync_AdSettings_SkipReferralList.htm)|
Отключение поиска по списку реферальных серверов.  
[SkipSystemPartitions](P_Tessa_Extensions_Platform_Server_AdSync_AdSettings_SkipSystemPartitions.htm)|
Отключение поиска по реферальным серверов, таким как ForestDnsZones,
DomainDnsZones, Configuration  
[TimeoutMilliseconds](P_Tessa_Extensions_Platform_Server_AdSync_AdSettings_TimeoutMilliseconds.htm)|
Таймаут подключения в миллисекундах. Если значение равно 0 или отрицательное
число, то используется таймаут по умолчанию в зависимости от сервера LDAP
(обычно около 5 секунд).  
[Url](P_Tessa_Extensions_Platform_Server_AdSync_AdSettings_Url.htm)| Адрес
подключения к службам LDAP.  
[UseGroupMembership](P_Tessa_Extensions_Platform_Server_AdSync_AdSettings_UseGroupMembership.htm)|
Использование атрибута groupMembership вместо memberOf.  
[UseLdapIntegerUid](P_Tessa_Extensions_Platform_Server_AdSync_AdSettings_UseLdapIntegerUid.htm)|
Использование числа, как uid для LDAP, не имеющих GUID.  
[UserGroup](P_Tessa_Extensions_Platform_Server_AdSync_AdSettings_UserGroup.htm)|
Группа синхронизации.  
[UseSsl](P_Tessa_Extensions_Platform_Server_AdSync_AdSettings_UseSsl.htm)|
Признак того, что используется защищённое подключение по протоколу SSL.  
##  __См. также
#### Ссылки
[AdSettings - ](T_Tessa_Extensions_Platform_Server_AdSync_AdSettings.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
