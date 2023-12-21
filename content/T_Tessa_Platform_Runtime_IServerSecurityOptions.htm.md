# IServerSecurityOptions - интерфейс
Объект с настройками безопасности сервера.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IServerSecurityOptions
VB __Копировать
     Public Interface IServerSecurityOptions
C++ __Копировать
     public interface class IServerSecurityOptions
F# __Копировать
     type IServerSecurityOptions = interface end
##  __Свойства
[BlockedSeriesDueDateTime](P_Tessa_Platform_Runtime_IServerSecurityOptions_BlockedSeriesDueDateTime.htm)|
Количество часов, на которое выполняется блокировка при превышении неудачных
попыток MaxFailedLoginAttemptsInSeries. По умолчанию: 15 минут.  
---|---  
[BlockWindowsAndLdapUsers](P_Tessa_Platform_Runtime_IServerSecurityOptions_BlockWindowsAndLdapUsers.htm)|
Признак того, что для сотрудников с типом входа "Windows" или "LDAP" будет
выполняться блокировка при нескольких неудачных попытках аутентификации по тем
же правилам, что и для сотрудников с типом входа "Пользователь TESSA". По
умолчанию false.  
[EnforceStrongPasswords](P_Tessa_Platform_Runtime_IServerSecurityOptions_EnforceStrongPasswords.htm)|
Признак того, что пароль, вводимый пользователем, должен содержать спец.
символы, цифры и разные регистры символов. Проверяется при изменении пароля
пользователем (не администратором). По умолчанию false.  
[FailedLoginAttemptsSeriesTime](P_Tessa_Platform_Runtime_IServerSecurityOptions_FailedLoginAttemptsSeriesTime.htm)|
Максимальное время между неудачными попытками, чтобы считать их частью серии.
По умолчанию 5 минут: 00:05:00.  
[Info](P_Tessa_Platform_Runtime_IServerSecurityOptions_Info.htm)|
Дополнительная информация для расширений.  
[MaxFailedLoginAttemptsBeforeBlocked](P_Tessa_Platform_Runtime_IServerSecurityOptions_MaxFailedLoginAttemptsBeforeBlocked.htm)|
Максимальное число разрешённых неудачных попыток входа до того, как произойдёт
блокировка пользователя (поля Blocked, BlockedDueDate в карточке сотрудника).
По умолчанию 0 \- проверка отключена.  
[MaxFailedLoginAttemptsInSeries](P_Tessa_Platform_Runtime_IServerSecurityOptions_MaxFailedLoginAttemptsInSeries.htm)|
Максимальное число разрешённых неудачных попыток входа в серии (промежуток
времени между попытками меньше заданного) до того, как произойдёт блокировка
пользователя (поля Blocked, BlockedDueDate в карточке сотрудника). По
умолчанию 0 \- проверка отключена.  
[MinPasswordLength](P_Tessa_Platform_Runtime_IServerSecurityOptions_MinPasswordLength.htm)|
Минимальная длина пароля, вводимого пользователем. Проверяется при изменении
пароля пользователем (не администратором). По умолчанию: 4.  
[PasswordExpirationNotificationTime](P_Tessa_Platform_Runtime_IServerSecurityOptions_PasswordExpirationNotificationTime.htm)|
Количество дней, оставшихся до окончания срока действия паролей у
пользователей, которым отправляются уведомления с рекомендацией сменить
пароль. По умолчанию null \- уведомления отключены.  
[PasswordExpirationTime](P_Tessa_Platform_Runtime_IServerSecurityOptions_PasswordExpirationTime.htm)|
Количество дней, в течение которых пароль действует с момента установки пароля
(поле PersonalRoles.PasswordChanged). Если пароль прекращает действовать, то
при входе в систему возвращается исключение. По умолчанию null \- проверка
отключена.  
[SessionInactivityTime](P_Tessa_Platform_Runtime_IServerSecurityOptions_SessionInactivityTime.htm)|
Время неактивности сессии в часах, проверяемое каждый раз при выполнении
запроса, связанного с сессией. Если с даты последней активности до текущей
даты прошло время больше заданного, то возвращается исключение. По умолчанию
null \- время неактивности неограничено.  
[UniquePasswordCount](P_Tessa_Platform_Runtime_IServerSecurityOptions_UniquePasswordCount.htm)|
Количество паролей пользователя, для которых проверяется, что они уникальны
(не повторяются). Проверяется при изменении пароля пользователем. По умолчанию
1.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
