# ISessionCredentials - интерфейс
Настройки входа, используемые для открытия сессии.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ISessionCredentials
VB __Копировать
     Public Interface ISessionCredentials
C++ __Копировать
     public interface class ISessionCredentials
F# __Копировать
     type ISessionCredentials = interface end
##  __Свойства
[IsCancelled](P_Tessa_Platform_Runtime_ISessionCredentials_IsCancelled.htm)|
Признак того, что авторизация считается отменённой, т.к. логин или пароль не
являются корректными для текущего типа авторизации.  
---|---  
[Login](P_Tessa_Platform_Runtime_ISessionCredentials_Login.htm)|  Логин для
входа. Может быть равен null или пустой строке.  
[LoginType](P_Tessa_Platform_Runtime_ISessionCredentials_LoginType.htm)| Тип
авторизации в системе.  
[Password](P_Tessa_Platform_Runtime_ISessionCredentials_Password.htm)|  Пароль
для входа. Может быть равен null или пустой строке.  
## __Методы
[CreateCopy](M_Tessa_Platform_Runtime_ISessionCredentials_CreateCopy.htm)|
Создаёт копию текущего объекта с указанием другого типа авторизации.  
---|---  
##  __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
