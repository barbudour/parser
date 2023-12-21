# IAdSettings - свойства
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
[DisableStaticRoleRename](P_Tessa_Extensions_Platform_Server_AdSync_IAdSettings_DisableStaticRoleRename.htm)|
Отключить переименование статических ролей.  
[OURoots](P_Tessa_Extensions_Platform_Server_AdSync_IAdSettings_OURoots.htm)|
Корни синхронизации.  
[OURootsSR](P_Tessa_Extensions_Platform_Server_AdSync_IAdSettings_OURootsSR.htm)|
Корни синхронизации для статических ролей.  
[Port](P_Tessa_Platform_ILdapSettings_Port.htm)|  Порт, по которому
выполняется подключение. Если значение равно 0 или отрицательное число, то
используется порт по умолчанию в зависимости от свойства
[ILdapSettings.UseSsl]: если true, то порт 636; если false, то порт 389.  
(Унаследован от [ILdapSettings](T_Tessa_Platform_ILdapSettings.htm))  
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
[UseGroupMembership](P_Tessa_Extensions_Platform_Server_AdSync_IAdSettings_UseGroupMembership.htm)|
Использование атрибута groupMembership вместо memberOf.  
[UseLdapIntegerUid](P_Tessa_Extensions_Platform_Server_AdSync_IAdSettings_UseLdapIntegerUid.htm)|
Использование числа, как uid для LDAP, не имеющих GUID.  
[UserGroup](P_Tessa_Extensions_Platform_Server_AdSync_IAdSettings_UserGroup.htm)|
Группа синхронизации.  
[UseSsl](P_Tessa_Platform_ILdapSettings_UseSsl.htm)| Признак того, что
используется защищённое подключение по протоколу SSL.  
(Унаследован от [ILdapSettings](T_Tessa_Platform_ILdapSettings.htm))  
##  __См. также
#### Ссылки
[IAdSettings - ](T_Tessa_Extensions_Platform_Server_AdSync_IAdSettings.htm)
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
