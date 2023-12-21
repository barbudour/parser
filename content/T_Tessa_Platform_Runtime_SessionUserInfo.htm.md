# SessionUserInfo - класс
Информация по пользователю, доступная из справочника сотрудников.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class SessionUserInfo : ISessionUserInfo
VB __Копировать
     Public NotInheritable Class SessionUserInfo
    	Implements ISessionUserInfo
C++ __Копировать
     public ref class SessionUserInfo sealed : ISessionUserInfo
F# __Копировать
     [<SealedAttribute>]
    type SessionUserInfo = 
        class
            interface ISessionUserInfo
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SessionUserInfo
Implements
    [ISessionUserInfo](T_Tessa_Platform_Runtime_ISessionUserInfo.htm)
##  __Конструкторы
[SessionUserInfo](M_Tessa_Platform_Runtime_SessionUserInfo__ctor.htm)|
Создаёт экземпляр класса с указанием значений его свойства.  
---|---  
## __Свойства
[AccessLevel](P_Tessa_Platform_Runtime_SessionUserInfo_AccessLevel.htm)|
Уровень доступа пользователя.  
---|---  
[Blocked](P_Tessa_Platform_Runtime_SessionUserInfo_Blocked.htm)|  Признак
того, что вход для пользователя заблокирован. Если признак установлен, то
пользователь не может войти в систему, даже если его поле "Тип входа" отлично
от "Вход запрещён".  
[BlockedDueDate](P_Tessa_Platform_Runtime_SessionUserInfo_BlockedDueDate.htm)|
Дата/время снятия блокировки, если пользователь был заблокирован временно, или
null, если пользователь не был заблокирован или был заблокирован постоянно.  
[LanguageCode](P_Tessa_Platform_Runtime_SessionUserInfo_LanguageCode.htm)|
Код языка интерфейса для пользователя или null, если язык интерфейса
неизвестен.  
[Login](P_Tessa_Platform_Runtime_SessionUserInfo_Login.htm)|  Логин (аккаунт)
пользователя, фактически прописанный в справочнике (в точности до регистра
символов). Может быть равен null или пустой строке.  
[LoginType](P_Tessa_Platform_Runtime_SessionUserInfo_LoginType.htm)| Тип
аутентификации, выполненный для пользователя.  
[PasswordChanged](P_Tessa_Platform_Runtime_SessionUserInfo_PasswordChanged.htm)|
Дата/время изменения пароля для типа входа "Пользователь Tessa", или null,
если тип входа отличается от "Пользователь Tessa" или дата/время неизвестны
(например, пароль был установлен скриптом).  
[PasswordHash](P_Tessa_Platform_Runtime_SessionUserInfo_PasswordHash.htm)|
Хеш от пароля сотрудника, используемый для проверки пароля пользователя с
типом входа "Tessa", или null, если пароль не задан, например, тип входа
отличен от "Tessa".  
[PasswordKey](P_Tessa_Platform_Runtime_SessionUserInfo_PasswordKey.htm)|  Ключ
сотрудника, используемый для проверки пароля пользователя с типом входа
"Tessa", или null, если пароль не задан, например, тип входа отличен от
"Tessa".  
[TimeZoneUtcOffset](P_Tessa_Platform_Runtime_SessionUserInfo_TimeZoneUtcOffset.htm)|
Смещение для временной зоны пользователя, заданное в карточке или 0, если не
заданно.  
[UserID](P_Tessa_Platform_Runtime_SessionUserInfo_UserID.htm)| Идентификатор
пользователя.  
[UserName](P_Tessa_Platform_Runtime_SessionUserInfo_UserName.htm)| Имя
пользователя. Не равно null или пустой строке.  
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
