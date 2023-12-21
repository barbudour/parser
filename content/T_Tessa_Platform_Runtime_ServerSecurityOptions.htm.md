# ServerSecurityOptions - класс
Объект с настройками безопасности сервера.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class ServerSecurityOptions : IServerSecurityOptions, 
    	ISealable
VB __Копировать
     Public NotInheritable Class ServerSecurityOptions
    	Implements IServerSecurityOptions, ISealable
C++ __Копировать
     public ref class ServerSecurityOptions sealed : IServerSecurityOptions, 
    	ISealable
F# __Копировать
     [<SealedAttribute>]
    type ServerSecurityOptions = 
        class
            interface IServerSecurityOptions
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ ServerSecurityOptions
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm), [IServerSecurityOptions](T_Tessa_Platform_Runtime_IServerSecurityOptions.htm)
##  __Конструкторы
[ServerSecurityOptions](M_Tessa_Platform_Runtime_ServerSecurityOptions__ctor.htm)|
Инициализирует новый экземпляр класса ServerSecurityOptions  
---|---  
##  __Свойства
[BlockedSeriesDueDateTime](P_Tessa_Platform_Runtime_ServerSecurityOptions_BlockedSeriesDueDateTime.htm)|
Количество часов, на которое выполняется блокировка при превышении неудачных
попыток MaxFailedLoginAttemptsInSeries. По умолчанию: 15 минут.  
---|---  
[BlockWindowsAndLdapUsers](P_Tessa_Platform_Runtime_ServerSecurityOptions_BlockWindowsAndLdapUsers.htm)|
Признак того, что для сотрудников с типом входа "Windows" или "LDAP" будет
выполняться блокировка при нескольких неудачных попытках аутентификации по тем
же правилам, что и для сотрудников с типом входа "Пользователь TESSA". По
умолчанию false.  
[EnforceStrongPasswords](P_Tessa_Platform_Runtime_ServerSecurityOptions_EnforceStrongPasswords.htm)|
Признак того, что пароль, вводимый пользователем, должен содержать спец.
символы, цифры и разные регистры символов. Проверяется при изменении пароля
пользователем (не администратором). По умолчанию false.  
[FailedLoginAttemptsSeriesTime](P_Tessa_Platform_Runtime_ServerSecurityOptions_FailedLoginAttemptsSeriesTime.htm)|
Максимальное время между неудачными попытками, чтобы считать их частью серии.
По умолчанию 5 минут: 00:05:00.  
[Info](P_Tessa_Platform_Runtime_ServerSecurityOptions_Info.htm)|
Дополнительная информация для расширений.  
[IsSealed](P_Tessa_Platform_Runtime_ServerSecurityOptions_IsSealed.htm)|
Признак того, что объект был защищён от изменений.  
[MaxFailedLoginAttemptsBeforeBlocked](P_Tessa_Platform_Runtime_ServerSecurityOptions_MaxFailedLoginAttemptsBeforeBlocked.htm)|
Максимальное число разрешённых неудачных попыток входа до того, как произойдёт
блокировка пользователя (поля Blocked, BlockedDueDate в карточке сотрудника).
По умолчанию 0 \- проверка отключена.  
[MaxFailedLoginAttemptsInSeries](P_Tessa_Platform_Runtime_ServerSecurityOptions_MaxFailedLoginAttemptsInSeries.htm)|
Максимальное число разрешённых неудачных попыток входа в серии (промежуток
времени между попытками меньше заданного) до того, как произойдёт блокировка
пользователя (поля Blocked, BlockedDueDate в карточке сотрудника). По
умолчанию 0 \- проверка отключена.  
[MinPasswordLength](P_Tessa_Platform_Runtime_ServerSecurityOptions_MinPasswordLength.htm)|
Минимальная длина пароля, вводимого пользователем. Проверяется при изменении
пароля пользователем (не администратором). По умолчанию: 4.  
[PasswordExpirationNotificationTime](P_Tessa_Platform_Runtime_ServerSecurityOptions_PasswordExpirationNotificationTime.htm)|
Количество дней, оставшихся до окончания срока действия паролей у
пользователей, которым отправляются уведомления с рекомендацией сменить
пароль. По умолчанию null \- уведомления отключены.  
[PasswordExpirationTime](P_Tessa_Platform_Runtime_ServerSecurityOptions_PasswordExpirationTime.htm)|
Количество дней, в течение которых пароль действует с момента установки пароля
(поле PersonalRoles.PasswordChanged). Если пароль прекращает действовать, то
при входе в систему возвращается исключение. По умолчанию null \- проверка
отключена.  
[SessionInactivityTime](P_Tessa_Platform_Runtime_ServerSecurityOptions_SessionInactivityTime.htm)|
Время неактивности сессии в часах, проверяемое каждый раз при выполнении
запроса, связанного с сессией. Если с даты последней активности до текущей
даты прошло время больше заданного, то возвращается исключение. По умолчанию
null \- время неактивности неограничено.  
[UniquePasswordCount](P_Tessa_Platform_Runtime_ServerSecurityOptions_UniquePasswordCount.htm)|
Количество паролей пользователя, для которых проверяется, что они уникальны
(не повторяются). Проверяется при изменении пароля пользователем. По умолчанию
1.  
## __Методы
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
[Seal](M_Tessa_Platform_Runtime_ServerSecurityOptions_Seal.htm)| Защищает
объект от изменений.  
[ToString](M_Tessa_Platform_Runtime_ServerSecurityOptions_ToString.htm)|
Возвращает строковое представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
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
