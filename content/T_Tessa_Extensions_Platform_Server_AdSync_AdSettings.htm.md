# AdSettings - класс
##  __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Server.AdSync](N_Tessa_Extensions_Platform_Server_AdSync.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class AdSettings : IAdSettings, ILdapSettings
VB __Копировать
     Public Class AdSettings
    	Implements IAdSettings, ILdapSettings
C++ __Копировать
     public ref class AdSettings : IAdSettings, 
    	ILdapSettings
F# __Копировать
     type AdSettings = 
        class
            interface IAdSettings
            interface ILdapSettings
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ AdSettings
Implements
    [IAdSettings](T_Tessa_Extensions_Platform_Server_AdSync_IAdSettings.htm), [ILdapSettings](T_Tessa_Platform_ILdapSettings.htm)
##  __Конструкторы
[AdSettings](M_Tessa_Extensions_Platform_Server_AdSync_AdSettings__ctor.htm)|
Инициализирует новый экземпляр класса AdSettings.  
---|---  
## __Свойства
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
[SetFromConfigAsync](M_Tessa_Extensions_Platform_Server_AdSync_AdSettings_SetFromConfigAsync.htm)|
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
[Tessa.Extensions.Platform.Server.AdSync - пространство
имён](N_Tessa_Extensions_Platform_Server_AdSync.htm)
