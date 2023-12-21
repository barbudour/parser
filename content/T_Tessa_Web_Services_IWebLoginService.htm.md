# IWebLoginService - интерфейс
##  __Definition
 **Пространство имён:** [Tessa.Web.Services](N_Tessa_Web_Services.htm)  
 **Сборка:** Tessa.Web (в Tessa.Web.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IWebLoginService : ILoginService
VB __Копировать
     Public Interface IWebLoginService
    	Inherits ILoginService
C++ __Копировать
     public interface class IWebLoginService : ILoginService
F# __Копировать
     type IWebLoginService = 
        interface
            interface ILoginService
        end
Implements
    [ILoginService](T_Tessa_Platform_Runtime_ILoginService.htm)
##  __Методы
[OpenSessionAsync](M_Tessa_Platform_Runtime_ILoginService_OpenSessionAsync.htm)|
Выполняет аутентификацию пользователя, используя анонимную аутентификацию по
учётной записи Windows и по заданным параметрам логин/пароль/доменное имя, или
используя аутентификацию для пользователя Tessa. Открывает сессию и возвращает
её токен [Tessa.Platform.Runtime.SessionToken], сериализованный в формате XML.  
(Унаследован от [ILoginService](T_Tessa_Platform_Runtime_ILoginService.htm))  
---|---  
[OpenSessionWindowsAuthAsync](M_Tessa_Platform_Runtime_ILoginService_OpenSessionWindowsAuthAsync.htm)|
Выполняет аутентификацию пользователя по учётной записи Windows. Открывает
сессию и возвращает её токен [Tessa.Platform.Runtime.SessionToken],
сериализованный в формате XML.  
(Унаследован от [ILoginService](T_Tessa_Platform_Runtime_ILoginService.htm))  
##  __См. также
#### Ссылки
[Tessa.Web.Services - пространство имён](N_Tessa_Web_Services.htm)
