# ILoginService - интерфейс
Сервис, обеспечивающий аутентификацию пользователей.
## __Definition
 **Пространство имён:** [Tessa.Platform.Runtime](N_Tessa_Platform_Runtime.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ILoginService
VB __Копировать
     Public Interface ILoginService
C++ __Копировать
     public interface class ILoginService
F# __Копировать
     type ILoginService = interface end
##  __Методы
[OpenSessionAsync](M_Tessa_Platform_Runtime_ILoginService_OpenSessionAsync.htm)|
Выполняет аутентификацию пользователя, используя анонимную аутентификацию по
учётной записи Windows и по заданным параметрам логин/пароль/доменное имя, или
используя аутентификацию для пользователя Tessa. Открывает сессию и возвращает
её токен [Tessa.Platform.Runtime.SessionToken], сериализованный в формате XML.  
---|---  
[OpenSessionWindowsAuthAsync](M_Tessa_Platform_Runtime_ILoginService_OpenSessionWindowsAuthAsync.htm)|
Выполняет аутентификацию пользователя по учётной записи Windows. Открывает
сессию и возвращает её токен [Tessa.Platform.Runtime.SessionToken],
сериализованный в формате XML.  
## __См. также
#### Ссылки
[Tessa.Platform.Runtime - пространство имён](N_Tessa_Platform_Runtime.htm)
