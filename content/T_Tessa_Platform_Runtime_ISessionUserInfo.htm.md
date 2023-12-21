# ISessionUserInfo - интерфейс
Информация по пользователю, доступная из справочника сотрудников.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISessionUserInfo
VB __Копировать
     Public Interface ISessionUserInfo
C++ __Копировать
     public interface class ISessionUserInfo
F# __Копировать
     type ISessionUserInfo = interface end
##  __Свойства
[AccessLevel](P_Tessa_Platform_Runtime_ISessionUserInfo_AccessLevel.htm)|
Уровень доступа пользователя.  
---|---  
[Blocked](P_Tessa_Platform_Runtime_ISessionUserInfo_Blocked.htm)|  Признак
того, что вход для пользователя заблокирован. Если признак установлен, то
пользователь не может войти в систему, даже если его поле "Тип входа" отлично
от "Вход запрещён".  
[BlockedDueDate](P_Tessa_Platform_Runtime_ISessionUserInfo_BlockedDueDate.htm)|
Дата/время снятия блокировки, если пользователь был заблокирован временно, или
null, если пользователь не был заблокирован или был заблокирован постоянно.  
[LanguageCode](P_Tessa_Platform_Runtime_ISessionUserInfo_LanguageCode.htm)|
Код языка интерфейса для пользователя или null, если язык интерфейса
неизвестен.  
[Login](P_Tessa_Platform_Runtime_ISessionUserInfo_Login.htm)|  Логин (аккаунт)
пользователя, фактически прописанный в справочнике (в точности до регистра
символов). Может быть равен null или пустой строке.  
[LoginType](P_Tessa_Platform_Runtime_ISessionUserInfo_LoginType.htm)| Тип
аутентификации, выполненный для пользователя.  
[PasswordChanged](P_Tessa_Platform_Runtime_ISessionUserInfo_PasswordChanged.htm)|
Дата/время изменения пароля для типа входа "Пользователь Tessa", или null,
если тип входа отличается от "Пользователь Tessa" или дата/время неизвестны
(например, пароль был установлен скриптом).  
[PasswordHash](P_Tessa_Platform_Runtime_ISessionUserInfo_PasswordHash.htm)|
Хеш от пароля сотрудника, используемый для проверки пароля пользователя с
типом входа "Tessa", или null, если пароль не задан, например, тип входа
отличен от "Tessa".  
[PasswordKey](P_Tessa_Platform_Runtime_ISessionUserInfo_PasswordKey.htm)|
Ключ сотрудника, используемый для проверки пароля пользователя с типом входа
"Tessa", или null, если пароль не задан, например, тип входа отличен от
"Tessa".  
[TimeZoneUtcOffset](P_Tessa_Platform_Runtime_ISessionUserInfo_TimeZoneUtcOffset.htm)|
Смещение для временной зоны пользователя, заданное в карточке или 0, если не
заданно.  
[UserID](P_Tessa_Platform_Runtime_ISessionUserInfo_UserID.htm)| Идентификатор
пользователя.  
[UserName](P_Tessa_Platform_Runtime_ISessionUserInfo_UserName.htm)| Имя
пользователя. Не равно null или пустой строке.  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
